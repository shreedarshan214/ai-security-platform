# 🛡️ AI Security Platform

### AI-Powered SOC Automation & Threat Intelligence Pipeline

<p align="center">
  <b>Detect Threats • Analyze Risk • Correlate Events • Automate Response</b>
</p>

<p align="center">
  A modular cybersecurity platform that combines network scanning,
  threat intelligence enrichment, risk scoring, Flask APIs, and n8n-based
  security automation.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-REST%20API-black?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Nmap-Network%20Scanning-2E8B57?style=for-the-badge&logo=linux&logoColor=white" />
  <img src="https://img.shields.io/badge/VirusTotal-Threat%20Intelligence-394EFF?style=for-the-badge&logo=virustotal&logoColor=white" />
  <img src="https://img.shields.io/badge/n8n-SOC%20Automation-EA4B71?style=for-the-badge&logo=n8n&logoColor=white" />
  <img src="https://img.shields.io/badge/Google%20Sheets-Event%20Storage-34A853?style=for-the-badge&logo=googlesheets&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

---

## 📑 Contents

* [Overview](#-overview)
* [Problem Statement](#-problem-statement)
* [Project Objectives](#-project-objectives)
* [Architecture](#-architecture)
* [Project Workflow](#-project-workflow)
* [Key Features](#-key-features)
* [Risk Analysis](#-risk-analysis)
* [Technology Stack](#-technology-stack)
* [Project Structure](#-project-structure)
* [Installation](#-installation)
* [Configuration](#-configuration)
* [Usage](#-usage)
* [n8n Automation Workflow](#-n8n-automation-workflow)
* [Security Monitoring Dashboard](#-security-monitoring-dashboard)
* [Sample Event Structure](#-sample-event-structure)
* [Advantages](#-advantages)
* [Limitations](#-limitations)
* [Future Enhancements](#-future-enhancements)
* [Responsible Use](#-responsible-use)
* [Project Status](#-project-status)
* [License](#-license)

---

## ⚡ Overview

**AI Security Platform** is a modular cybersecurity and Security Operations
Center automation project.

It is designed to collect security findings, enrich them with threat
intelligence, calculate risk, identify repeated or related events, and route
the results through automated response workflows.

The platform combines a Python-based backend with n8n automation to reduce
manual security analysis and improve the consistency of security event
processing.

```text
Security Target
      ↓
Network Scanning
      ↓
Threat Intelligence Enrichment
      ↓
Risk Analysis
      ↓
Threat Correlation
      ↓
Risk-Based Decision
      ↓
Alerting and Event Storage
      ↓
Security Dashboard
```

---

## 🎯 Problem Statement

Traditional security monitoring often requires analysts to manually:

* Collect security information
* Check IP addresses and domains
* Review threat intelligence
* Prioritize findings
* Compare repeated events
* Send alerts
* Store security records
* Prepare reports

This manual process can be time-consuming and may result in inconsistent
prioritization.

The AI Security Platform addresses this problem by creating an automated
pipeline for collecting, analyzing, prioritizing, and reporting security
events.

---

## 🚀 Project Objectives

The main objectives of this project are:

* Automate security finding collection
* Enrich indicators using threat intelligence
* Calculate structured risk scores
* Assign severity and priority levels
* Correlate repeated security events
* Trigger alerts based on risk
* Store security events centrally
* Provide dashboard-based monitoring
* Create a modular and extendable security architecture
* Support academic research and defensive security operations

---

## 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │    SECURITY TARGET   │
                         │   IP / Domain / Host │
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
                         │   VIRUSTOTAL API     │
                         │ Threat Intelligence  │
                         │      Enrichment      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     RISK ENGINE      │
                         │ Score • Severity     │
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
01. Receive Target or Security Indicator
02. Run Network or Security Scan
03. Collect Security Findings
04. Enrich Findings with Threat Intelligence
05. Normalize the Collected Data
06. Calculate Risk Score
07. Assign Severity and Priority
08. Correlate Repeated or Related Events
09. Apply Risk-Based Decision Logic
10. Send Alert or Store Event
11. Display Results in the Dashboard
```

---

## 🌟 Key Features

| Feature                    | Description                                        |
| -------------------------- | -------------------------------------------------- |
| 🔍 Network Scanning        | Collects security-related information using Nmap   |
| 🧠 Threat Intelligence     | Enriches indicators using VirusTotal               |
| 🧮 Risk Scoring            | Calculates structured risk scores                  |
| 🚦 Severity Classification | Categorizes findings into risk levels              |
| 🎯 Priority Assignment     | Helps identify important findings first            |
| 🔗 Threat Correlation      | Detects repeated or related security events        |
| ⚙️ Flask REST API          | Provides backend integration for automation        |
| 🔄 n8n Automation          | Connects analysis, decisions, and response actions |
| 🚨 Automated Alerting      | Supports Telegram and email notifications          |
| 📦 Event Storage           | Stores security records in Google Sheets           |
| 📊 Dashboard Monitoring    | Visualizes security events and risk trends         |
| 🧩 Modular Architecture    | Keeps the project easy to maintain and extend      |
| 🛠️ Custom Exceptions      | Provides structured error handling                 |
| 🔐 Secure Configuration    | Supports environment-based API configuration       |

---

## 🧠 Risk Analysis

The risk engine processes security findings and assigns a risk level using
structured decision logic.

Example severity weights:

```text
LOW       → 5 points
MEDIUM    → 15 points
HIGH      → 30 points
```

The risk score can be influenced by:

* Finding severity
* Threat intelligence results
* Number of repeated events
* Confidence level
* Target information
* Attack pattern
* Security exposure
* Historical event frequency

### Risk Classification

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

Risk scoring is intended to support analyst prioritization. It should not
replace manual validation or professional security investigation.

---

## 🛠️ Technology Stack

| Category             | Technologies               |
| -------------------- | -------------------------- |
| Programming Language | Python                     |
| Backend Framework    | Flask                      |
| API Style            | REST API                   |
| Network Scanning     | Nmap                       |
| Threat Intelligence  | VirusTotal API             |
| Risk Analysis        | Python-based risk engine   |
| Automation           | n8n                        |
| Alerting             | Telegram, Email            |
| Event Storage        | Google Sheets              |
| Visualization        | Looker Studio              |
| Operating Systems    | Windows, Linux, Kali Linux |
| Version Control      | Git, GitHub                |

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
│   ├── security-dashboard.png
│   ├── n8n-workflow.png
│   └── flask-dashboard.png
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

#### Linux or Kali Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Nmap

Install Nmap separately if it is not already available.

Verify the installation:

```bash
nmap --version
```

### 5. Configure Environment Variables

Create a `.env` file if required by your local configuration.

```env
VT_API_KEY=your_virustotal_api_key
N8N_WEBHOOK_URL=your_n8n_webhook_url
```

> Never commit API keys, passwords, tokens, cookies, or private credentials
> to GitHub.

### 6. Run the Application

```bash
python app.py
```

---

## ⚙️ Configuration

Before running the complete workflow, configure:

* VirusTotal API credentials
* n8n webhook URL
* Telegram bot credentials, if used
* Email credentials, if used
* Google Sheets connection
* Local scanner configuration
* Allowed target scope

Credentials should be stored using environment variables or the credential
management features of n8n.

---

## ▶️ Usage

The platform can receive security indicators through the Flask application
and connected automation workflow.

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
  "indicator": "example.com",
  "indicator_type": "domain",
  "risk_level": "high",
  "risk_score": 75,
  "severity": "high",
  "priority": "high",
  "confidence": 0.85,
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

[View the n8n Workflow JSON](n8n-workflows/ai-security-platform-workflow.json)

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
Risk Analysis
       ↓
Threat Correlation
       ↓
IF Risk-Based Decision
       ├── High Risk → Alert / Response
       └── Normal    → Log / Store
```

### Import the Workflow

1. Open your n8n instance.
2. Select **Import from File**.
3. Select:

```text
n8n-workflows/ai-security-platform-workflow.json
```

4. Configure your own credentials.
5. Update webhook and notification settings.
6. Test the workflow using an authorized target.
7. Activate the workflow after successful testing.

> The workflow JSON must not contain real API keys or private credentials.

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
* Historical security activity

> This repository contains a static dashboard screenshot for documentation.
> The live dashboard is not publicly shared.

---

## 🧾 Security Event Fields

The platform supports structured security event processing using fields such as:

```text
Event ID
Target
Indicator
Indicator Type
Source
Threat Intelligence Result
Risk Score
Risk Level
Severity
Priority
Attack Pattern
Repeat Count
Confidence
Timestamp
Response Status
```

These fields can be used for:

* Alert generation
* Threat correlation
* Historical analysis
* Risk prioritization
* Dashboard visualization
* Security reporting
* Incident investigation

---

## 📸 Project Screenshots

### Security Monitoring Dashboard

![Security Monitoring Dashboard](screenshots/security-dashboard.png)

### n8n Automation Workflow

![n8n Automation Workflow](screenshots/n8n-workflow.png)

### Flask Application

![Flask Application](screenshots/flask-dashboard.png)

---

## ✅ Advantages

### 1. Reduces Manual Analysis

The platform automates repeated security analysis tasks and reduces the time
required to review individual findings.

### 2. Improves Alert Prioritization

Risk scoring and severity classification help analysts focus on important
security events first.

### 3. Centralizes Security Information

Threat intelligence, risk scores, event details, and response information
can be processed through one unified workflow.

### 4. Supports Faster Response

n8n automation can trigger notifications and response actions immediately
after a high-risk event is detected.

### 5. Modular and Extendable

Each major component is separated into its own module, making it easier to
add new scanners, intelligence sources, and response integrations.

### 6. Useful for Academic Research

The project demonstrates practical concepts related to cybersecurity,
automation, threat intelligence, risk assessment, and incident response.

### 7. Supports Historical Analysis

Centralized event storage allows repeated events and historical security
patterns to be reviewed later.

### 8. Easy Integration

The Flask REST API allows the platform to connect with n8n and other
security tools or applications.

---

## ⚠️ Limitations

* Risk scoring is dependent on the quality of the collected findings.
* Threat intelligence services may have API limits.
* External integrations require valid credentials.
* Automated decisions should be reviewed before production use.
* Dashboard data depends on successful event storage.
* The platform is currently a prototype and may require additional security
  hardening before production deployment.

---

## 🚧 Future Enhancements

* Advanced AI-based finding summarization
* Real-time SOC dashboard
* Additional threat intelligence integrations
* Improved threat correlation
* Historical risk comparison
* Asset criticality scoring
* Security report generation
* Docker deployment
* SIEM integration
* Incident ticket creation
* Role-based access control
* Authentication and authorization
* Database integration
* Automated incident response playbooks
* PDF and CSV report generation
* Production-level monitoring and logging

---

## 🔐 Responsible Use

This project is intended only for:

* Authorized security testing
* Academic research
* Defensive security monitoring
* Lab environments
* Security automation experiments
* Systems owned by the user
* Systems for which explicit permission has been provided

Do not scan, test, or collect information from unauthorized systems.

The user is responsible for following all applicable laws, policies,
and testing-scope requirements.

---

## 🎓 Academic Relevance

This project demonstrates practical knowledge in:

* Cybersecurity automation
* Threat intelligence
* Security orchestration
* Risk assessment
* Incident response
* Network scanning
* REST API development
* Python application development
* Workflow automation
* Security monitoring
* Modular software architecture
* Security event correlation

The platform can be extended as a foundation for an
**AI Autonomous Security Operations Platform** research project.

---

## 🚦 Project Status

**Status:** Completed Prototype / Active Development

The current version demonstrates the core concept of collecting security
findings, enriching them with threat intelligence, calculating risk, and
processing events through an automated SOC workflow.

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
