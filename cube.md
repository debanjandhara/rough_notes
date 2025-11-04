
"Cube" is a multi-agent live trading system, designed to operate like an AI-driven investment firm. Here's a thorough explanation of the codebase structure, key components, and workflow based on the README and directory listing:

---

# Overview

- Cube runs specialized agents (analysts and traders) for multiple symbols (e.g., BTCUSD, GOOG).
- Each agent produces typed outputs using Pydantic models.
- The system trades equities, cryptocurrencies, and commodities via MetaTrader 5 using the MetaAPI platform.
- It maintains continuous research and trading cycles with persistent context stored in a PostgreSQL database.
- Observability and tracing are handled by Logfire.

---

# Directory and File Structure

- [.git/](cci:7://file:///d:/Debanjan/Projects/Fivver/cube/.git:0:0-0:0) and [.gitignore](cci:7://file:///d:/Debanjan/Projects/Fivver/cube/.gitignore:0:0-0:0): Git version control files.
- [Dockerfile](cci:7://file:///d:/Debanjan/Projects/Fivver/cube/Dockerfile:0:0-0:0): Containerization setup for the application.
- [README.md](cci:7://file:///d:/Debanjan/Projects/Fivver/cube/README.md:0:0-0:0): Detailed project documentation.
- [__init__.py](cci:7://file:///d:/Debanjan/Projects/Fivver/cube/__init__.py:0:0-0:0): Marks the root package (likely empty).
- [cube/](cci:7://file:///d:/Debanjan/Projects/Fivver/cube:0:0-0:0): Main application source directory.
- [main.py](cci:7://file:///d:/Debanjan/Projects/Fivver/cube/main.py:0:0-0:0): Entry point script that orchestrates the trading system.
- [pyproject.toml](cci:7://file:///d:/Debanjan/Projects/Fivver/cube/pyproject.toml:0:0-0:0): Python project configuration and dependencies.
- [uv.lock](cci:7://file:///d:/Debanjan/Projects/Fivver/cube/uv.lock:0:0-0:0): Dependency lock file for the `uv` package manager.

---

# Key Components Inside [cube/](cci:7://file:///d:/Debanjan/Projects/Fivver/cube:0:0-0:0)

- `cube/shared/`:
  - `database.py`: Handles PostgreSQL database persistence for analyst and trading reports.
  - `terminal.py`: Manages symbol-specific trading terminal state (positions, orders, account).
  - `models/`: Contains Pydantic models defining data schemas for analyst reports, trading reports, and shared fields.
- `cube/integrations/`:
  - `eodhd.py`: Market data provider integration (quotes, fundamentals, technicals).
  - `metaapi.py`: Trading execution integration with MetaTrader 5.
  - `perplexity_search.py`: Web search integration for market intelligence.
- `cube/teams/core/`: Implements core team logic for analysts and trading leads per symbol.

---

# Entry Point: [main.py](cci:7://file:///d:/Debanjan/Projects/Fivver/cube/main.py:0:0-0:0)

- Orchestrates parallel execution of core teams for multiple symbols.
- Fetches analyst reports from the database.
- Runs analysts and trader agents in parallel.
- Synthesizes reports and executes trading decisions.
- Persists updated reports back to the database.
- Fully instrumented with Logfire for observability and tracing.

---

# Workflow Summary

1. For each symbol, three analysts (fundamental, macro, quantitative) run in parallel.
2. Analysts update research reports and respond to trader requests.
3. The trading lead synthesizes analyst reports, current positions, and trading history.
4. The trader makes execution decisions and issues new research requests.
5. All reports and decisions are saved to the database.
6. The cycle repeats continuously.

---

# Data Models

- Analyst Reports (`cube/shared/models/analyst.py`):
  - `SymbolAnalystReport`: Persistent research report per analyst and symbol.
- Trading Reports (`cube/shared/models/trading.py`):
  - `TradingSessionReport`: Daily snapshot of trading decisions and session state.
  - `ResearchRequest`: Explicit research tasks from trader to analysts.

---

# Observability

- Uses Logfire for structured logging, tracing, and spans.
- All agents are instrumented automatically.
- Execution traces and logs are accessible via Logfire's platform.

---

# Setup and Running

- Requires Python 3.12 and `uv` package manager.
- Environment variables for API keys, database URL, and configuration must be set in a `.env` file.
- Database tables are created by running `cube/shared/database.py`.
- Run the system with `uv run python main.py`.

---

If you want, I can now explore specific files or folders to explain their contents in detail or clarify any part of the system. Let me know how you want to proceed.
