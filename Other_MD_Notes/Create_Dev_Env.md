## ✅ Step-by-Step: Set Up CI/CD from GitHub to Cloud Run (via GUI)

### 🔁 Repeat these steps once for **Frontend** and once for **Backend**

### **Step 1: Connect Your GitHub Repo**

1. Go to: **Cloud Build > Triggers**
   👉 [https://console.cloud.google.com/cloud-build/triggers](https://console.cloud.google.com/cloud-build/triggers)
2. Click **“Connect Repository”**
3. Choose **GitHub (Cloud Build GitHub App)**
4. Authorize and select your GitHub account
5. Choose the **repo (frontend/backend)** `(one at a time)` and click **Connect**

---

### **Step 2: Create a Cloud Build Trigger (from GUI)**

1. After connecting the repo, click **"Create Trigger"**
2. Fill details:

   * **Name:** `frontend-deploy` or `backend-deploy`
   * **Event:** *Push to a branch*
   * **Branch:** `^develop$`
   * **Repository:** Select the one you connected
3. **Configuration**:

   * Choose **Cloud Build configuration: "Buildpack (no Dockerfile required)"**
   * Choose the **directory** of your app (usually `.`)
   * Select **Region** (e.g., `us-central1`)
   * Set **Service Name** (e.g., `frontend-dev`, `backend-dev`)
   * ✅ Check "Deploy to Cloud Run"

---

### **Step 4: Configure Deployment Settings**

In the same trigger form:

* **Cloud Run Service Settings**:

  * Region: `us-central1` (or as per your location)
  * Allow unauthenticated invocations: ✅ Yes
  * Platform: Cloud Run (fully managed)
  * Project: (select current project)

> Cloud Build will **automatically create a container** using Google Buildpacks — no Dockerfile needed.

---

### ✅ DONE!

You now have automatic deployment to Cloud Run whenever code is pushed to `develop`.

---
