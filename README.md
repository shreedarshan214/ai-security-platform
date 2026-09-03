````markdown
<div align="center">

# 🛡️ AI SECURITY PLATFORM

### AI-Powered SOC Automation & Threat Intelligence Pipeline

<p>
  <b>Detect Threats • Analyze Risk • Automate Response</b>
</p>

<p>
  A modular cybersecurity platform that combines network scanning,
  threat intelligence, risk analysis, and SOC automation.
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-REST%20API-black?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Nmap-Network%20Scanning-2E8B57?style=for-the-badge&logo=linux&logoColor=white" />
  <img src="https://img.shields.io/badge/VirusTotal-Threat%20Intelligence-394EFF?style=for-the-badge&logo=virustotal&logoColor=white" />
  <img src="https://img.shields.io/badge/n8n-SOC%20Automation-EA4B71?style=for-the-badge&logo=n8n&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

</div>

---

## 📑 Contents

- [Overview](#-overview)
- [Architecture](#-architecture)
- [Project Workflow](#-project-workflow)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [n8n Automation Workflow](#-n8n-automation-workflow)
- [Security Monitoring Dashboard](#-security-monitoring-dashboard)
- [Security Event Fields](#-security-event-fields)
- [Future Enhancements](#-future-enhancements)
- [Responsible Use](#-responsible-use)
- [Project Status](#-project-status)
- [License](#-license)

---

## ⚡ Overview

**AI Security Platform** is a modular cybersecurity project designed to support
security assessment, threat intelligence enrichment, risk prioritization,
and Security Operations Center automation.

The platform combines:

- Python-based network scanning
- VirusTotal threat intelligence
- Structured risk analysis
- Flask REST API integration
- n8n workflow automation
- Threat correlation
- Automated alerting
- Centralized event storage
- Dashboard-based security monitoring

The main objective is to transform raw security findings into structured,
prioritized, and actionable security events.

```text
Security Finding
       ↓
Threat Intelligence
       ↓
Risk Analysis
       ↓
Threat Correlation
       ↓
Risk-Based Decision
       ↓
Alerting and Event Storage
       ↓
Security Monitoring Dashboard
````

---

## 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │   SECURITY TARGET    │
                         │   IP / Domain / Host  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     NMAP SCANNER     │
                         │ Security Information │
                         │      Collection      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  VIRUSTOTAL API      │
                         │ Threat Intelligence  │
                         │     Enrichment       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    AI RISK ENGINE    │
                         │ Severity • Score     │
                         │ Priority • Confidence│
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    FLASK REST API    │
                         │ Structured Findings  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    N8N AUTOMATION    │
                         │ Correlation • Logic  │
                         │ Response Processing  │
                         └──────────┬───────────┘
                                    │
                  ┌─────────────────┼─────────────────┐
                  │                 │                 │
                  ▼                 ▼                 ▼
          ┌──────────────┐  ┌──────────────┐  ┌────────────────┐
          │   Telegram   │  │    Email     │  │ Google Sheets  │
          │    Alerts    │  │    Alerts    │  │  Event Storage │
          └──────────────┘  └──────────────┘  └───────┬────────┘
                                                      │
                                                      ▼
                                             ┌────────────────┐
                                             │ Looker Studio  │
                                             │   Dashboard    │
                                             └────────────────┘
```

---

## 🔄 Project Workflow

```text
01. Security Scan
        ↓
02. Collect Security Findings
        ↓
03. Threat Intelligence Enrichment
        ↓
04. AI-Assisted Risk Assessment
        ↓
05. Severity and Priority Assignment
        ↓
06. Threat Correlation
        ↓
07. Risk-Based Decision
        ↓
08. Alert or Response
        ↓
09. Event Storage
        ↓
10. Dashboard and Historical Analysis
```

---

## 🌟 Key Features

| Module                 | Description                                               |
| ---------------------- | --------------------------------------------------------- |
| 🔍 Network Scanning    | Collects security-related information using Nmap          |
| 🧠 Threat Intelligence | Enriches indicators using VirusTotal                      |
| 🧮 Risk Engine         | Calculates risk scores and severity levels                |
| 🎯 Risk Prioritization | Helps identify findings that require attention            |
| 🔗 Threat Correlation  | Combines repeated or related security events              |
| ⚙️ Flask REST API      | Provides structured integration with automation workflows |
| 🔄 n8n Automation      | Connects intelligence, analysis, decisions, and response  |
| 🚨 Automated Alerting  | Supports Telegram and email notifications                 |
| 📦 Event Storage       | Stores security records in Google Sheets                  |
| 📊 Dashboard Reporting | Displays security events and risk trends                  |
| 🧩 Modular Design      | Separates scanning, risk logic, and exception handling    |

---

## 🧠 Risk Analysis

The risk engine processes security findings and assigns a risk level based
on severity and structured decision logic.

Example severity weights:

```text
LOW       → 5 points
MEDIUM    → 15 points
HIGH      → 30 points
```

The risk analysis can consider:

* Finding severity
* Threat intelligence results
* Number of repeated events
* Confidence level
* Target information
* Attack pattern
* Security exposure

Example risk classification:

```text
┌──────────────┬────────────────────────────────┐
│ Risk Level   │ Description                    │
├──────────────┼────────────────────────────────┤
│ LOW          │ Limited or informational risk  │
│ MEDIUM       │ Requires further investigation │
│ HIGH         │ Significant security concern   │
│ CRITICAL     │ Immediate security attention   │
└──────────────┴────────────────────────────────┘
```

---

## 🛠️ Technology Stack

| Category                | Technologies               |
| ----------------------- | -------------------------- |
| Programming             | Python, JavaScript         |
| Backend                 | Flask, REST API            |
| Network Scanning        | Nmap                       |
| Threat Intelligence     | VirusTotal API             |
| Risk Analysis           | Python-based risk engine   |
| Automation              | n8n                        |
| Alerting                | Telegram, Email            |
| Event Storage           | Google Sheets              |
| Visualization           | Looker Studio              |
| Development Environment | Linux, Kali Linux, Windows |
| Version Control         | Git, GitHub                |

---

## 📁 Project Structure

```text
ai-security-platform/
│
├── app.py
├── scanner.py
├── risk_engine.py
├── exceptions.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── n8n-workflows/
│   └── ai-security-platform-workflow.json
│
├── screenshots/
│   └── security-dashboard.png
│
└── assets/
    └── banner.png
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shreedarshan214/ai-security-platform.git
cd ai-security-platform
```

### 2. Create a Virtual Environment

#### Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### Linux / Kali Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file if required by your local configuration.

```env
VT_API_KEY=your_virustotal_api_key
N8N_WEBHOOK_URL=your_n8n_webhook_url
```

> Never upload API keys, passwords, tokens, or other secrets to GitHub.

### 5. Run the Application

```bash
python app.py
```

---

## ▶️ Usage

The platform can be used to process security findings through the Flask
application and connected n8n workflow.

Example request:

```json
{
  "indicator": "example.com",
  "indicator_type": "domain"
}
```

Example structured result:

```json
{
  "status": "success",
  "risk_level": "high",
  "risk_score": 75,
  "severity": "high",
  "priority": "high",
  "findings": []
}
```

The exact request and response format may vary depending on the current
implementation.

---

## 🔄 n8n Automation Workflow

The exported n8n workflow is included in this repository for reference,
re-importing, testing, and academic demonstration.

### Workflow File

[View n8n Workflow JSON](n8n-workflows/ai-security-platform-workflow.json)

### Workflow Stages

```text
Security Finding
       ↓
Flask REST API
       ↓
Threat Intelligence
       ↓
Data Normalization
       ↓
AI Risk Analysis
       ↓
Threat Correlation
       ↓
IF Risk-Based Decision
       ├── High Risk → Alert / Response
       └── Normal    → Log / Store
```

### Import Instructions

1. Open your n8n instance.
2. Select **Import from File**.
3. Select:

```text
n8n-workflows/ai-security-platform-workflow.json
```

4. Configure your own API credentials.
5. Update the webhook and notification settings.
6. Test the workflow in an authorized environment.

> The exported workflow must not contain real API keys or private credentials.

---

## 📊 Security Monitoring Dashboard

<p align="center">
  <img
    src="screenshots/security-dashboard.png"
    alt="AI Security Platform Security Monitoring Dashboard"
    width="100%"
  />
</p>

The dashboard provides a visual summary of:

* Total security records
* Critical alerts
* High-risk findings
* Medium-severity events
* Low-severity events
* Record count trends
* Top targeted domains
* Severity distribution

> This repository contains a static dashboard screenshot for documentation.
> The live dashboard is not publicly shared.

---

## 🧾 Security Event Fields

The platform supports structured security event processing using fields such as:

```text
Target
Indicator
Indicator Type
Threat Intelligence Result
Risk Score
Risk Level
Severity
Priority
Attack Pattern
Repeat Count
Confidence
Timestamp
```

These fields can be used for:

* Alert generation
* Event correlation
* Historical analysis
* Risk prioritization
* Dashboard visualization
* Security reporting

---

## 📸 Project Screenshots

### Security Monitoring Dashboard

```markdown
![Security Monitoring Dashboard](screenshots/security-dashboard.png)
```

### n8n Workflow

Add your n8n screenshot to the `screenshots` folder and reference it as:

```markdown
![n8n Automation Workflow](screenshots/n8n-workflow.png)
```

### Flask Application

Add your Flask application screenshot as:

```markdown
![Flask Application](screenshots/flask-dashboard.png)
```

---

## 🔐 Responsible Use

This project is intended only for:

* Authorized security testing
* Academic research
* Defensive security monitoring
* Lab environments
* Security automation experiments
* Systems owned by the user or explicitly authorized for testing

Do not scan, test, or collect information from unauthorized systems.

The user is responsible for following all applicable laws, policies,
and testing-scope requirements.

---

## 🚧 Future Enhancements

* Advanced AI-based finding summarization
* Real-time SOC dashboard
* Additional threat intelligence integrations
* Improved threat correlation
* Historical risk comparison
* Asset prioritization
* Security report generation
* Docker deployment
* SIEM integration
* Incident ticket creation
* Role-based access control
* Improved authentication and authorization
* Production-level monitoring

---

## 🎓 Academic Relevance

This project demonstrates practical concepts in:

* Cybersecurity automation
* Threat intelligence
* Security orchestration
* Risk assessment
* Incident response
* Python application development
* REST API integration
* Workflow automation
* Security monitoring
* Modular software architecture

The platform can be extended as a foundation for an
**AI Autonomous Security Platform** research project.

---

## 🚦 Project Status

**Status:** Completed Prototype / Active Development

This project was developed as part of an M.E. Cybersecurity research and
practical security automation initiative.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

```bash
git checkout -b feature/your-feature
git add .
git commit -m "Add your feature"
git push origin feature/your-feature
```

Then create a pull request.

---

## 📜 License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.

---

<div align="center">

### Built for Cybersecurity Research and Defensive Automation

**AI Security Platform**

</div>
```
