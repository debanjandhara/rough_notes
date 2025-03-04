# Developer Notes: Automated Deployment System for sinesiAI

## Deployment Flow

1. A systemd **timer** triggers an update script every 60 seconds.
2. The update script:
   - Changes to the `/home/ubuntu/sinesiAI` directory.
   - Ensures it is on the `prod` branch.
   - Checks for updates via `git pull`.
   - If there are no changes, the script exits.
   - If there are changes, it checks:
     - **Frontend:** If `package.json` changed, runs `npm install` and restarts the frontend service.
     - **Backend:** If `requirements.txt` changed, rebuilds the virtual environment and restarts the backend service.

## Components

### 1. Frontend Deployment Service

Located at: `/etc/systemd/system/frontend-deployment.service`

```ini
[Unit]
Description=Frontend Deployment Service
After=network.target

[Service]
Type=simple
WorkingDirectory=/home/ubuntu/sinesiAI/frontend
ExecStart=/usr/bin/npm run dev -- --host 0.0.0.0 --port 3000
Restart=always
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

- Runs the frontend on port 3000.
- Automatically restarts in case of failure.
- Logs to systemd’s journal.

### 2. Backend Deployment Service

Located at: `/etc/systemd/system/backend-deployment.service`

```ini
[Unit]
Description=Backend Deployment Service
After=network.target

[Service]
Type=simple
WorkingDirectory=/home/ubuntu/sinesiAI/backend
ExecStart=/bin/bash -c 'source /home/ubuntu/sinesiAI/backend/venv/bin/activate && exec uvicorn server:app --host 0.0.0.0 --port 8000 --reload'
Restart=always
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

- Runs the backend on port 8000 using Uvicorn.
- Ensures old processes are properly stopped before restarting.

### 3. Deployment Update Script

Located at: `/usr/local/bin/deployment-update.sh` Make it executable:

```bash
sudo chmod +x /usr/local/bin/deployment-update.sh
```

#### Script Logic

```bash
#!/bin/bash
set -e

REPO_DIR="/home/ubuntu/sinesiAI"
FRONT_HASH_FILE="/tmp/frontend_package.hash"
BACK_HASH_FILE="/tmp/backend_requirements.hash"

cd "$REPO_DIR" || { echo "Repo directory not found"; exit 1; }

git checkout prod

OLD_FRONT_HASH=$( [ -f "$FRONT_HASH_FILE" ] && cat "$FRONT_HASH_FILE" || echo "" )
OLD_BACK_HASH=$( [ -f "$BACK_HASH_FILE" ] && cat "$BACK_HASH_FILE" || echo "" )

GIT_OUTPUT=$(git pull origin prod)
echo "$GIT_OUTPUT"

if echo "$GIT_OUTPUT" | grep -q "Already up to date"; then
    echo "No changes detected in the repository."
    exit 0
fi

if [ -f "frontend/package.json" ]; then
    NEW_FRONT_HASH=$(sha256sum frontend/package.json | awk '{print $1}')
    if [ "$OLD_FRONT_HASH" != "$NEW_FRONT_HASH" ]; then
        cd frontend || exit 1
        npm install
        cd ..
    fi
    systemctl restart frontend-deployment.service
    echo "$NEW_FRONT_HASH" > "$FRONT_HASH_FILE"
fi

if [ -f "backend/requirements.txt" ]; then
    NEW_BACK_HASH=$(sha256sum backend/requirements.txt | awk '{print $1}')
    if [ "$OLD_BACK_HASH" != "$NEW_BACK_HASH" ]; then
        cd backend || exit 1
        rm -rf venv
        python3 -m venv venv
        source venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt
        deactivate
        cd ..
    fi
    systemctl restart backend-deployment.service
    echo "$NEW_BACK_HASH" > "$BACK_HASH_FILE"
fi

exit 0
```

### 4. Deployment Update Service

Located at: `/etc/systemd/system/deployment-update.service`

```ini
[Unit]
Description=Deployment Update Service

[Service]
Type=oneshot
ExecStart=/usr/local/bin/deployment-update.sh
```

- Runs the update script when triggered.

### 5. Deployment Update Timer

Located at: `/etc/systemd/system/deployment-update.timer`

```ini
[Unit]
Description=Timer for Deployment Update Service

[Timer]
OnBootSec=30s
OnUnitActiveSec=60s

[Install]
WantedBy=timers.target
```

- Starts 30 seconds after boot.
- Runs every 60 seconds to check for updates.

## Enabling and Starting Services

After creating the files, enable and start the services:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now frontend-deployment.service
sudo systemctl enable --now backend-deployment.service
sudo systemctl enable --now deployment-update.timer
```

### Checking Logs

To view logs for each service:

```bash
journalctl -u frontend-deployment.service
journalctl -u backend-deployment.service
journalctl -u deployment-update.service
```

## Summary

- This system automatically updates the frontend and backend whenever changes are pushed.
- It minimizes downtime and ensures consistency across deployments.
- Uses systemd for process management and scheduling.
- Logs can be monitored using `journalctl`.

This setup ensures the `sinesiAI` project stays up to date without manual intervention, reducing deployment risks and improving reliability.

