    # AI Autonomous Security Platform

    > AI-powered SOC automation, threat intelligence, and attack-surface management pipeline.

    [![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
    [![Flask](https://img.shields.io/badge/Backend-Flask-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
    [![n8n](https://img.shields.io/badge/Workflow-n8n-EA4B71?logo=n8n&logoColor=white)](https://n8n.io/)
    [![Security](https://img.shields.io/badge/Focus-Cybersecurity-C43B3B)](https://owasp.org/)

    ## Overview

    The **AI Autonomous Security Platform** is a modular security-automation project that connects reconnaissance, threat-intelligence enrichment, AI-assisted analysis, risk scoring, and alert delivery into one workflow.

    The platform is designed to reduce repetitive SOC tasks and provide a consistent decision path:

    ```text
    Target / Webhook
        ↓
    Reconnaissance
        ↓
    AI-assisted analysis
        ↓
    Threat-intelligence enrichment
        ↓
    Correlation and risk scoring
        ↓
    Block / Monitor / Allow
        ↓
    Telegram alert + audit log
    ```

    ## Key capabilities

    - Automated scan triggering through a webhook
    - Attack-surface discovery and service enumeration
    - AI-assisted finding analysis and prioritization
    - VirusTotal-based indicator enrichment
    - Risk scoring and severity classification
    - Correlation of scan findings and threat intelligence
    - Decision outcomes: `BLOCK`, `MONITOR`, or `ALLOW`
    - Telegram notifications for security events
    - Google Sheets or equivalent audit logging
    - Modular Python/Flask backend
    - Interactive project showcase page

    ## Architecture

    | Layer | Technology | Purpose |
    |---|---|---|
    | API and backend | Python, Flask | Receives requests and exposes automation endpoints |
    | Reconnaissance | Nmap and compatible scanners | Discovers services and attack-surface information |
    | Orchestration | n8n | Connects the workflow stages |
    | Intelligence | VirusTotal API | Enriches indicators with reputation data |
    | Decision engine | AI agent + correlation rules | Converts findings into an actionable verdict |
    | Alerting | Telegram Bot API | Sends real-time security notifications |
    | Audit | Google Sheets | Stores findings and decisions for review |
    | Showcase | HTML, CSS, JavaScript | Presents the platform architecture and results |

    ## Example decision flow

    ```text
    Finding received
        ↓
    Normalize target, severity, and evidence
        ↓
    Calculate risk score
        ↓
    Enrich IP/domain/hash with threat intelligence
        ↓
    Correlate evidence
        ↓
    Generate explanation
        ↓
    Dispatch alert and save audit record
    ```

    ## Example alert

    ```text
    CRITICAL — BLOCK

    Target: scanme.nmap.org
    Risk Score: 100
    Threat: port scanning
    Attack Stage: reconnaissance

    Reason:
    Critical risk score indicates an immediate threat.
    The target is blocked to reduce potential exploitation risk.
    ```

    The values shown in the showcase are illustrative demonstration data unless they are connected to a live deployment.

    ## Project structure

    ```text
    .
    ├── app.py
    ├── requirements.txt
    ├── README.md
    ├── index.html
    ├── .env.example
    ├── config/
    │   └── settings.py
    ├── modules/
    │   ├── recon.py
    │   ├── enrichment.py
    │   ├── risk_engine.py
    │   ├── correlation.py
    │   └── alerting.py
    ├── workflows/
    │   └── n8n-workflow.json
    ├── templates/
    │   └── dashboard.html
    └── static/
        ├── css/
        └── js/
    ```

    > Rename or adjust the structure above to match the actual files in your repository.

    ## Requirements

    - Python 3.10 or newer
    - Flask
    - n8n
    - Nmap
    - VirusTotal API key
    - Telegram bot token and chat ID
    - Google Sheets credentials, if audit logging is enabled

    ## Installation

    ### 1. Clone the repository

    ```bash
    git clone https://github.com/<your-username>/<your-repository>.git
    cd <your-repository>
    ```

    ### 2. Create a virtual environment

    ```bash
    python -m venv .venv
    ```

    Linux/macOS:

    ```bash
    source .venv/bin/activate
    ```

    Windows:

    ```powershell
    .venv\Scripts\Activate.ps1
    ```

    ### 3. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

    ### 4. Configure environment variables

    Copy the example file:

    ```bash
    cp .env.example .env
    ```

    Example configuration:

    ```env
    FLASK_ENV=development
    FLASK_HOST=127.0.0.1
    FLASK_PORT=5000

    VIRUSTOTAL_API_KEY=your_virustotal_api_key

    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
    TELEGRAM_CHAT_ID=your_telegram_chat_id

    GOOGLE_SHEETS_ID=your_google_sheet_id
    ```

    Never commit `.env`, API keys, bot tokens, credentials, or private scan results.

    ### 5. Run the Flask application

    ```bash
    python app.py
    ```

    Open:

    ```text
    http://127.0.0.1:5000
    ```

    ### 6. Open the showcase

    The repository showcase is a standalone static page:

    ```bash
    python -m http.server 8000
    ```

    Then open:

    ```text
    http://127.0.0.1:8000/index.html
    ```

    ## API workflow

    A typical webhook request may look like this:

    ```bash
    curl -X POST http://127.0.0.1:5000/webhook   -H "Content-Type: application/json"   -d '{
        "target": "example.com",
        "scan_type": "full"
    }'
    ```

    The exact endpoint and request fields must match the implementation in your Flask application.

    ## Risk scoring model

    A risk engine can combine multiple signals:

    ```text
    Risk Score =
        severity weight
    + threat-intelligence score
    + exposed-service impact
    + correlation confidence
    + asset criticality
    ```

    Example severity weights:

    | Severity | Weight |
    |---|---:|
    | Low | 5 |
    | Medium | 15 |
    | High | 30 |
    | Critical | 50 |

    These values are configurable and should be calibrated against your own test data.

    ## Security and responsible use

    This project is intended for **authorized security testing, defensive research, and controlled lab environments**.

    Only scan systems that you own or have explicit permission to assess. Do not use the platform to disrupt services, bypass access controls, collect private data, or test third-party infrastructure without authorization.

    Recommended safeguards:

    - Add target allowlists
    - Require authentication for webhook endpoints
    - Rate-limit scan requests
    - Store secrets in environment variables
    - Log every automated decision
    - Add human approval for destructive actions
    - Run scanners with least-privilege permissions
    - Validate and sanitize all incoming targets
    - Keep third-party API keys out of source control

    ## Showcase

    The included `index.html` presents:

    - Pipeline architecture
    - Live-style severity dashboard
    - Target activity bars
    - Severity distribution
    - Automated alert examples
    - Technology stack

    The showcase is a visual demonstration and does not itself execute security scans.

    ## Roadmap

    - [ ] Add authentication and role-based access control
    - [ ] Add persistent database storage
    - [ ] Add background task processing
    - [ ] Add scan-result deduplication
    - [ ] Add CVE and asset criticality enrichment
    - [ ] Add analyst approval workflows
    - [ ] Add dashboard filters and export
    - [ ] Add unit and integration tests
    - [ ] Add Docker deployment
    - [ ] Add SIEM integrations
    - [ ] Add model evaluation and explainability reports

    ## Contributing

    1. Fork the repository.
    2. Create a feature branch.
    3. Add tests for new functionality.
    4. Run formatting and validation checks.
    5. Open a pull request with a clear description.

    ## License

    Add the license that applies to your project, such as MIT, Apache-2.0, or an institutional research license.

    ## Author

    **Shree Darshan**  
    M.E. Cyber Security

    ---

    If you find this project useful, consider starring the repository and sharing feedback.
