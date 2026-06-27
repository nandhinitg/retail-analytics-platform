# Retail Analytics Platform

## Overview
An end-to-end Azure Data Engineering project that ingests retail sales data, processes it through Bronze, Silver, and Gold layers using PySpark and Delta Lake, and generates business insights.

## Tech Stack
- Azure Data Factory
- Azure Databricks
- PySpark
- Delta Lake
- Azure Data Lake Storage Gen2
- SQL
- Power BI

## Architecture
CSV Files
    ↓
ADLS (Raw)
    ↓
Databricks (Bronze)
    ↓
Databricks (Silver)
    ↓
Databricks (Gold)
    ↓
Power BI

## Key Features
- Incremental Data Loads
- Data Quality Checks
- CDC using Delta Lake MERGE
- Star Schema Modeling
- Business KPI Generation
