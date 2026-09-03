# 🛡️ AI Security Platform

> **AI-powered SOC automation and threat intelligence pipeline for detecting, analyzing, prioritizing, and responding to cybersecurity events.**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-REST%20API-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/n8n-SOC%20Automation-EA4B71?style=for-the-badge&logo=n8n&logoColor=white" alt="n8n">
  <img src="https://img.shields.io/badge/VirusTotal-Threat%20Intelligence-3949AB?style=for-the-badge" alt="VirusTotal">
  <img src="https://img.shields.io/badge/Nmap-Network%20Scanning-1F6FEB?style=for-the-badge" alt="Nmap">
  <img src="https://img.shields.io/badge/License-MIT-2EA44F?style=for-the-badge" alt="MIT License">
</p>

---

## 📌 Project Overview

The **AI Security Platform** is a modular cybersecurity automation project designed to support Security Operations Center activities.

It combines:

* Network scanning
* Security event collection
* Threat intelligence enrichment
* Risk scoring
* AI-assisted security analysis
* Automated alert generation
* SOC workflow orchestration
* Event storage and visualization

The platform helps security teams move from **manual investigation** to a more structured and automated detection-and-response process.

---

## 🎯 Project Objectives

The main objectives of this project are to:

1. Detect suspicious network and security activities.
2. Enrich security events using threat intelligence.
3. Calculate risk scores based on severity and impact.
4. Correlate security information from multiple sources.
5. Generate automated SOC alerts.
6. Support block, monitor, and allow decisions.
7. Store security events for future analysis.
8. Display security trends through dashboards.
9. Reduce repetitive manual SOC activities.
10. Provide a modular foundation for future AI-based security improvements.

---

## 🧠 Core Architecture

```text
                    ┌──────────────────────┐
                    │   Security Target    │
                    │ Domain / IP / Event  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Network Scanner      │
                    │ Nmap / Event Input   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Flask REST API       │
                    │ Event Processing     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Threat Intelligence  │
                    │ VirusTotal Enrichment│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Risk Engine          │
                    │ Severity + Scoring    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ n8n Automation       │
                    │ Correlation + Logic  │
                    └──────────┬───────────┘
                               │
                ┌──────────────┼──────────────┐
                ▼              ▼              ▼
          ┌──────────┐   ┌──────────┐   ┌─────────────┐
          │ Telegram │   │ Google   │   │ Dashboard   │
          │ Alerts   │   │ Sheets   │   │ Analytics   │
          └──────────┘   └──────────┘   └─────────────┘
```

---

## ✨ Key Features

### 🔍 Security Event Detection

The platform accepts security-related events such as:

* Suspicious IP addresses
* Domain-based security events
* Port scanning activity
* High-risk network findings
* Threat intelligence results
* Security monitoring events

### 🌐 Network Scanning

Network reconnaissance and service discovery can be integrated using Nmap.

The scanning layer can be extended to support:

* Host discovery
* Port scanning
* Service detection
* Version detection
* Network exposure analysis

Only scan systems that you own or have explicit permission to test.

### 🦠 Threat Intelligence Enrichment

The platform integrates with VirusTotal to enrich security events with reputation information.

Example enrichment fields include:

* Malicious detection count
* Suspicious detection count
* Threat reputation
* Target information
* Intelligence-based context

### 🧮 Risk Scoring

The risk engine calculates a risk score using security severity and event information.

Example severity levels:

| Severity | Meaning                              |
| -------- | ------------------------------------ |
| Low      | Limited risk or informational event  |
| Medium   | Suspicious activity requiring review |
| High     | Significant security concern         |
| Critical | Immediate attention required         |

The risk score supports automated decisions such as:

* `allow`
* `monitor`
* `block`

### 🤖 AI-Assisted Analysis

The workflow can use AI-based analysis to:

* Interpret security events
* Explain the reason behind a risk score
* Identify the likely attack stage
* Recommend an appropriate response
* Generate human-readable SOC alerts

### ⚙️ n8n SOC Automation

The n8n workflow connects different security and automation components.

The workflow includes stages such as:

* Webhook event intake
* Event preparation
* AI analysis
* VirusTotal enrichment
* Result parsing
* Risk-based branching
* Alert generation
* Event storage
* Notification delivery

### 🚨 Automated Alerts

The platform generates structured security alerts containing:

* Target
* Priority
* Severity
* Risk score
* AI decision
* Threat type
* Attack stage
* Threat intelligence result
* Recommended action
* Event timestamp

### 📊 Security Dashboard

The project includes dashboard visualizations for:

* Total record count
* Critical alerts
* High-severity alerts
* Medium-severity alerts
* Low-severity alerts
* Severity distribution
* Record count over time
* Top targets
* Target-based event analysis

---

## 🗂️ Project Structure

```text
ai-security-platform/
│
├── app.py
├── scanner.py
├── risk_engine.py
├── exceptions.py
├── requirements.txt
├── LICENSE
├── README.md
├── .gitignore
│
├── n8n-workflows/
│   ├── N8N-Workflow.json
│   │
│   └── screenshots/
│       ├── Screenshot 2026-09-03 160239.png
│       ├── Screenshot 2026-09-03 160754.png
│       ├── Screenshot 2026-09-03 160804.png
│       ├── Screenshot 2026-09-03 160903.png
│       ├── Screenshot 2026-09-03 160918.png
│       ├── Screenshot 2026-09-03 160942.png
│       └── Screenshot 2026-09-03 163400.png
│
└── __pycache__/
    └── Excluded through .gitignore
```

---

## 🧩 Main Components

### `app.py`

Contains the Flask application and REST API logic.

Responsibilities:

* Receive security events
* Validate incoming data
* Process events
* Return structured responses
* Connect the API layer with the risk engine

### `scanner.py`

Contains network scanning and security discovery functionality.

Responsibilities:

* Execute authorized network scans
* Collect network information
* Identify open ports and services
* Prepare scan results for further analysis

### `risk_engine.py`

Contains risk scoring and response decision logic.

Responsibilities:

* Evaluate severity
* Calculate risk scores
* Generate risk summaries
* Recommend monitoring or blocking actions

### `exceptions.py`

Contains custom exceptions used by the platform.

This improves error handling and makes the application easier to maintain.

### `N8N-Workflow.json`

Contains the exported n8n automation workflow used to connect the security processing pipeline.

---

## 🔄 Workflow Execution

```text
1. Security event is received
2. Event data is validated
3. AI analysis is performed
4. Threat intelligence is collected
5. Intelligence results are parsed
6. Risk score is calculated
7. Event is classified by severity
8. Automation decides allow, monitor, or block
9. Alert is sent to the notification channel
10. Event is stored for reporting
11. Dashboard is updated
```

---

## 📨 Example Security Alert

```text
🚨 AI SECURITY ALERT 🚨

Target: example.com

AI Decision: block
Priority: P1
Severity: critical

Risk Score: 100

Reason:
Critical risk score indicates immediate threat.
The event requires urgent investigation and response.

Automation Status:
Block: true
Notify: true
Ticket: true

Automated SOC System
```

---

## 📸 Project Screenshots

### 1. n8n SOC Automation Workflow

<img src="n8n-workflows/screenshots/Screenshot%202026-09-03%20160239.png" alt="n8n SOC automation workflow" width="100%">

### 2. n8n Workflow Execution

<img src="n8n-workflows/screenshots/Screenshot%202026-09-03%20160754.png" alt="n8n workflow execution" width="100%">

### 3. Security Alert Notification

<img src="n8n-workflows/screenshots/Screenshot%202026-09-03%20160804.png" alt="Security alert notification" width="100%">

### 4. Automated SOC Alert

<img src="n8n-workflows/screenshots/Screenshot%202026-09-03%20160903.png" alt="Automated SOC alert" width="100%">

### 5. Security Event Detection

<img src="n8n-workflows/screenshots/Screenshot%202026-09-03%20160918.png" alt="Security event detected alert" width="100%">

### 6. Security Analytics Dashboard

<img src="n8n-workflows/screenshots/Screenshot%202026-09-03%20160942.png" alt="Security analytics dashboard" width="100%">

### 7. SOC Monitoring Report

<img src="n8n-workflows/screenshots/Screenshot%202026-09-03%20163400.png" alt="SOC monitoring report dashboard" width="100%">

---

## 🛠️ Technology Stack

| Technology    | Purpose                             |
| ------------- | ----------------------------------- |
| Python        | Core application development        |
| Flask         | REST API backend                    |
| Nmap          | Network scanning                    |
| VirusTotal    | Threat intelligence enrichment      |
| n8n           | Workflow automation                 |
| AI Model      | Event analysis and decision support |
| Telegram      | Security alert notifications        |
| Google Sheets | Event storage                       |
| Looker Studio | Security analytics and reporting    |
| GitHub        | Source code management              |

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shreedarshan214/ai-security-platform.git
cd ai-security-platform
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```powershell
venv\Scripts\activate
```

#### Linux or Kali Linux

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file if your implementation requires API credentials.

Example:

```env
VIRUSTOTAL_API_KEY=your_api_key
N8N_WEBHOOK_URL=your_webhook_url
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

Never upload real API keys, tokens, passwords, or private credentials to GitHub.

### 6. Run the Flask Application

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

---

## 🔌 Example API Request

```bash
curl -X POST http://127.0.0.1:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "target": "example.com",
    "severity": "high",
    "threat_type": "port_scanning"
  }'
```

The exact endpoint may vary depending on the implementation in `app.py`.

---

## 🔐 Security and Ethical Use

This project is intended for:

* Educational research
* Authorized security testing
* Defensive security monitoring
* SOC automation experiments
* Laboratory environments
* Systems owned by the user or organization

Do not use this project to scan, attack, disrupt, or monitor systems without proper authorization.

The project does not guarantee complete threat detection or automatic prevention of every attack. All automated blocking decisions should be tested carefully before being used in a production environment.

---

## 📈 Advantages

### 1. Reduces Manual Work

Automates repetitive security event processing and notification tasks.

### 2. Faster Detection

Processes events and enriches them with threat intelligence more quickly than a fully manual workflow.

### 3. Consistent Risk Decisions

Uses structured severity and risk-scoring logic to support consistent responses.

### 4. Modular Design

Each component can be developed, tested, and improved independently.

### 5. Better Visibility

Stores security events and displays them through analytical dashboards.

### 6. Easy Integration

The platform can be extended with additional APIs, scanners, notification channels, databases, and AI models.

### 7. Research-Friendly

The architecture can support future research in:

* AI-based threat detection
* Security event correlation
* Automated incident response
* Risk prediction
* Attack-surface monitoring
* Explainable security analytics

---

## 🔮 Future Enhancements

Planned improvements may include:

* Authentication and role-based access control
* PostgreSQL or MongoDB event storage
* Real-time dashboard updates
* More threat intelligence providers
* Automated ticket creation
* Advanced attack correlation
* MITRE ATT&CK mapping
* Vulnerability scanning integration
* Cloud asset discovery
* Subdomain monitoring
* Security header analysis
* Machine-learning-based anomaly detection
* Explainable AI security decisions
* Docker deployment
* Production-grade logging and monitoring

---

## 🧪 Testing

Before using the platform in a real environment, test:

* API input validation
* Risk-score calculation
* Severity classification
* Threat intelligence response handling
* Failed API requests
* Missing fields
* Invalid targets
* Notification failures
* Workflow branching
* Duplicate event handling

---

## 📚 Research Relevance

This project is relevant to cybersecurity research areas such as:

* Security Operations Center automation
* Threat intelligence
* AI-assisted incident response
* Network security monitoring
* Risk-based alert prioritization
* Security event correlation
* Automated cyber defense
* Security analytics and visualization

---

## 👨‍💻 Author

**Shree Darshan**
M.E. Cybersecurity

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

---

## ⭐ Support the Project

If you find this project useful:

* Star the repository
* Fork the project
* Suggest improvements
* Report issues
* Share feedback
* Contribute new security modules

<p align="center">

**Built for cybersecurity learning, research, and defensive automation.**

</p>
