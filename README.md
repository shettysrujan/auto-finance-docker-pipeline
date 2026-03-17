# 🚗 Auto Finance Data Pipeline

## 📌 Overview

This project demonstrates a **real-world data engineering pipeline** for an auto finance company. It processes loan application data, evaluates risk, and stores transformed results using a fully containerized architecture.

The system uses:

- 🐳 Docker (containerization)
- ⚙️ Docker Compose (orchestration)
- 🌪️ Apache Airflow (workflow orchestration)
- ⚡ PySpark (data transformation)
- 🐘 PostgreSQL (data storage)
- ☁️ AWS EC2 (deployment)

---

## 🧠 Use Case

An auto finance company wants to:

- Analyze loan applications
- Evaluate customer credit risk
- Automate ETL workflows
- Build scalable, reproducible pipelines

---

## 🏗️ Architecture
            +-------------------+
            |   Airflow DAG     |
            | (Orchestration)   |
            +--------+----------+
                     |
                     v
            +-------------------+
            |   PySpark Job     |
            | (Transformation)  |
            +--------+----------+
                     |
                     v
            +-------------------+
            |   PostgreSQL      |
            | (Data Storage)    |
            +-------------------+

---

## 📁 Project Structure

```

auto-finance-pipeline/
│
├── docker-compose.yml
├── dags/
│   └── finance_dag.py
│
├── scripts/
│   └── transform.py
│
├── data/
│   └── loans.csv
│
└── README.md

