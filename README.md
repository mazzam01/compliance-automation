
# 🔐 Automated Compliance Reporting for SOC 2 / ISO 27001

![AWS](https://img.shields.io/badge/AWS-CloudTrail%20%7C%20Config%20%7C%20S3-orange?logo=amazon-aws)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

## 📌 What is this project?

An automated pipeline that continuously collects compliance evidence from AWS and generates audit-ready reports for **SOC 2 Type II** and **ISO 27001** — reducing audit preparation from months to days.

---

## 🚨 Problem

Manual evidence collection for compliance audits is slow, error-prone, and expensive. Security teams spend weeks gathering screenshots and logs across hundreds of systems before every audit.

## ✅ Solution

Automate evidence collection using AWS-native tools + Python scripts, so evidence is always current and reports are always ready.

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| AWS CloudTrail | Audit log of all API activity |
| AWS Config Rules | Continuous compliance checks (MFA, encryption, etc.) |
| Amazon S3 | Immutable evidence storage |
| Python (boto3) | Evidence collection & report generation |
| GitHub | Source control + access log evidence |

---

## 📁 Project Structure

```
compliance-automation/
│
├── README.md
├── .gitignore
│
├── cloudtrail/
│   └── setup.md              # CloudTrail configuration steps
│
├── config-rules/
│   └── rules.md              # AWS Config Rules used
│
├── scripts/
│   └── evidence_collector.py # Main Python script
│
├── reports/
│   └── sample_report.html    # Sample audit report output
│
└── docs/
    └── architecture.md       # How the pipeline works
```

---

## 🚀 Getting Started

### Prerequisites
- AWS Account (Free Tier works)
- Python 3.10+
- AWS CLI configured

### Step 1 — Enable CloudTrail
```bash
# Done via AWS Console → CloudTrail → Create Trail
# Trail name: compliance-trail
# S3 bucket: compliance-evidence-[yourname]
# Log file validation: ENABLED ✅
```

### Step 2 — Enable AWS Config
```bash
# Done via AWS Console → AWS Config → Get Started
# Record: All resources
# S3 bucket: same as above
```

### Step 3 — Run Evidence Collector
```bash
pip install boto3
python scripts/evidence_collector.py
```

---

## 📊 Controls Covered (SOC 2)

- [ ] MFA enabled for all IAM users
- [ ] S3 public access blocked
- [ ] EBS encryption at rest enabled
- [ ] CloudTrail enabled with log file validation
- [ ] Access reviews (quarterly)

---

## 📈 Progress

- [x] CloudTrail enabled ✅
- [x] AWS Config enabled ✅
- [x] Config Rules defined (MFA, S3, EBS) ✅
- [x] Fixed: S3 public access blocked ✅
- [x] MFA enabled for azzam-admin ✅
- [x] Evidence collector script ✅
- [x] Automated HTML report generation ✅
- [x] Daily cron job (runs every day at 9AM) ✅
- [x] Slack alerts for failing controls

---

## 👤 Author

**[Momen Alazzam]**  
DevOps & Security Enthusiast | Building in public 🚀  

---
## 📸 Screenshots

![Compliance Report](docs/Screenshot%20from%202026-04-26%2020-55-39.png)
> ⚠️ This is a learning project built for portfolio purposes. Not intended for production use without review.
