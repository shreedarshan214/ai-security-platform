# AI Security Platform

**AI-Powered SOC Automation & Threat Intelligence Pipeline**

An AI-assisted security automation platform that combines network scanning, threat intelligence enrichment, risk analysis, and automated response workflows.

## Overview

AI Security Platform is a modular cybersecurity project designed to support security assessment and SOC automation. It integrates Python-based scanning, VirusTotal threat intelligence, an AI-driven risk engine, and n8n workflows to transform security findings into structured, prioritized alerts.

The platform also supports centralized event storage and dashboard-based analysis for security monitoring and historical review.

## Key Features

* **Network scanning** using Nmap to collect security-related information.
* **Threat intelligence enrichment** using the VirusTotal API.
* **AI-assisted risk analysis** to classify findings and assign severity.
* **Risk prioritization** using structured decision logic.
* **n8n SOC automation** for alert processing and response workflows.
* **Correlation-based analysis** to identify repeated security events.
* **Automated alerting** through Telegram and email.
* **Centralized event storage** using Google Sheets.
* **Security dashboard** using Looker Studio for monitoring and analysis.
* **Flask REST API** for integrating security analysis into automation workflows.

## Architecture

```text
                    ┌─────────────────────┐
                    │   Security Target   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Nmap Scanner      │
                    │  Security Findings  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  VirusTotal API     │
                    │ Threat Intelligence │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   AI Risk Engine    │
                    │ Severity & Priority │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Flask REST API   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   n8n Automation    │
                    │ Correlation & Logic │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┼─────────────┐
                 ▼             ▼             ▼
          ┌──────────┐  ┌──────────┐  ┌──────────────┐
          │ Telegram │  │  Email   │  │ Google Sheets│
          │  Alerts  │  │  Alerts  │  │ Event Store  │
          └──────────┘  └──────────┘  └──────┬───────┘
                                             │
                                             ▼
                                      ┌──────────────┐
                                      │ Looker Studio│
                                      │  Dashboard   │
                                      └──────────────┘
```

## Project Workflow

```text
Scan
  ↓
Threat Intelligence Enrichment
  ↓
AI Risk Assessment
  ↓
Severity & Priority Assignment
  ↓
Correlation
  ↓
Alert / Response
  ↓
Event Storage
  ↓
Dashboard & Reporting
```

## Tech Stack

| Category             | Technologies                 |
| -------------------- | ---------------------------- |
| Programming          | Python, JavaScript           |
| Backend              | Flask, REST APIs             |
| Scanning             | Nmap                         |
| Threat Intelligence  | VirusTotal API               |
| AI                   | OpenRouter / LLM integration |
| Automation           | n8n                          |
| Alerting             | Telegram, Email              |
| Data Storage         | Google Sheets                |
| Visualization        | Looker Studio                |
| Security Environment | Linux / Kali Linux           |

## Project Structure

```text
ai-security-platform/
│
├── app.py
├── scanner.py
├── risk_engine.py
├── exceptions.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/shreedarshan214/ai-security-platform.git
cd ai-security-platform
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux / Kali Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file if required by your local configuration.

```env
VT_API_KEY=your_virustotal_api_key
```

**Never commit API keys or other secrets to GitHub.**

### 5. Run the application

```bash
python app.py
```

## n8n Integration

The platform is designed to integrate with n8n for security automation.

Example workflow:

```text
Security Finding
      ↓
Flask API
      ↓
AI Risk Analysis
      ↓
Correlation
      ↓
IF Decision
      ├── Attack → Alert / Response
      └── Safe   → Log / Store
```

## Security Monitoring

The platform supports structured security event processing, including:

* Target information
* Threat intelligence results
* Risk score
* Risk level
* Severity
* Priority
* Attack pattern
* Repeat count
* Confidence
* Timestamp

These fields can be used for alerting, historical analysis, and dashboard visualization.

## Dashboard

The project includes a Looker Studio dashboard for visualizing security events and risk trends.

Example dashboard views:

* Security event count
* Severity distribution
* Critical alert count
* Risk trends
* Target-based analysis

## Project Status

**Status:** Completed prototype / Active development

This project was developed as part of an M.E. Cybersecurity research and practical security automation initiative.

## Disclaimer

This project is intended for authorized security testing, educational purposes, and defensive security research. Only use it against systems you own or have permission to assess.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
