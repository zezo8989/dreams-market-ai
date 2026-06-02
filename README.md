# Dreams Market AI Settlement Platform

Enterprise Financial Reconciliation & AI Audit System

## Overview

Automatically reconcile POS settlement reports against official bank statements with AI-powered auditing, anomaly detection, discrepancy investigation, reporting, and executive insights.

## Key Features

- **Automated Reconciliation**: Match POS settlements with bank deposits
- **AI Anomaly Detection**: Detect unusual patterns and discrepancies
- **Premium Dashboard**: Executive-grade reporting and visualization
- **Multi-Bank Support**: Egyptian banks (Banque Misr, NBE, AAIB)
- **PDF & Excel Export**: Professional reporting capabilities
- **Role-Based Security**: JWT authentication with RBAC
- **Audit Trail**: Complete action logging for compliance

## Tech Stack

### Backend
- Python 3.12
- FastAPI
- SQLAlchemy 2.x
- PostgreSQL
- Alembic

### Frontend
- HTML5
- Tailwind CSS (CDN)
- Chart.js

### Data Processing
- pandas
- numpy
- openpyxl
- pdfplumber

### AI/ML
- scikit-learn
- numpy

### Reporting
- reportlab

## Project Structure

```
dreams-market-ai/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── parsers/
│   │   ├── reconciliation/
│   │   ├── anomaly_detection/
│   │   ├── reporting/
│   │   ├── security/
│   │   └── utils/
│   ├── migrations/
│   ├── tests/
│   ├── requirements.txt
│   └── alembic.ini
├── frontend/
│   ├── static/
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── manage.html
│   │   ├── login.html
│   │   └── reports.html
│   └── styles/
├── docker-compose.yml
├── Dockerfile
├── .env.example
├── .gitignore
└── startup.sh
```

## Installation

### Prerequisites
- Docker & Docker Compose
- Python 3.12
- PostgreSQL 15+

### Quick Start

1. Clone the repository
```bash
git clone https://github.com/zezo8989/dreams-market-ai.git
cd dreams-market-ai
```

2. Configure environment
```bash
cp .env.example .env
# Edit .env with your settings
```

3. Start with Docker Compose
```bash
docker-compose up -d
```

4. Run migrations
```bash
docker-compose exec backend alembic upgrade head
```

5. Access dashboard
```
http://localhost:8000
```

## API Documentation

Once running, visit:
- **API Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

## Database Tables

- **Branches**: Regional branch information
- **Terminals**: POS terminal configuration
- **POS_Settlements**: Settlement batch records
- **Bank_Statements**: Bank transaction records
- **Reconciliation_Results**: Matching results and discrepancies
- **Audit_Logs**: Complete action audit trail
- **Users**: User accounts and permissions

## Reconciliation Engine

### Matching Logic
1. Settlement amount matching
2. Settlement date verification
3. Batch number validation
4. MID matching
5. TID matching
6. Configurable tolerance levels

### Status Codes
- `MATCHED`: Successfully reconciled
- `MISSING_BANK_DEPOSIT`: Settlement not found in bank statement
- `MISMATCHED_AMOUNT`: Amount discrepancy detected
- `DUPLICATE_BATCH`: Duplicate batch detected
- `UNMATCHED`: No matching bank deposit

## AI Anomaly Detection

Detects:
- **Settlement Volume Drop**: Z-score < -2 over 14-day moving average
- **Abnormal Spikes**: Unusual transaction volume increases
- **Duplicate Patterns**: Recurring batch duplications
- **Settlement Delays**: Delayed deposits by branch

## Security

- JWT token-based authentication
- Bcrypt password hashing
- Role-Based Access Control (Admin, Auditor, Viewer)
- CSRF protection
- Rate limiting
- Secure file upload validation
- Complete audit logging

## User Roles

- **Admin**: Full system access, user management, settings
- **Auditor**: Create uploads, view reports, manage terminals
- **Viewer**: Read-only dashboard access

## Reporting

### Executive PDF Report
- Executive summary
- Settlement totals
- Deposit totals
- Discrepancy analysis
- Anomaly detection results
- Branch rankings
- Professional charts and layouts

### Excel Export
- Styled workbooks
- Conditional formatting
- Auto-filters
- Frozen panes
- Summary sheets
- Branch-specific data
- Automatic formulas

## Production Deployment

### Requirements
- Kubernetes cluster or VM with Docker
- PostgreSQL 15+ database
- SSL/TLS certificates
- SMTP service for notifications
- Backup strategy

### Environment Variables
See `.env.example` for complete configuration

### Database Backups
```bash
docker-compose exec postgres pg_dump -U postgres dreams_market > backup.sql
```

### Monitoring
- Application logs: `/var/log/dreams-market/`
- Database logs: PostgreSQL logs
- Metrics: Prometheus-compatible endpoints

## Support & Documentation

For issues and feature requests, please visit:
https://github.com/zezo8989/dreams-market-ai/issues

## License

Proprietary - Dreams Market Platform

## Authors

Principal Software Architect Team
Staff Backend Engineers
Senior Frontend Engineers
DevOps Engineers
AI Engineers
Database Architects
QA Leads
Security Auditors
