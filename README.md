# Retail_Lakehouse_platform
# AWS & Databricks Retail Lakehouse

## Business Problem

A retail company receives customer, product, order, payment, and inventory data from multiple operational systems. The objective is to build a scalable Lakehouse platform capable of batch and incremental analytics using AWS and Databricks.

## Architecture

MySQL / REST APIs / CSV

↓

Amazon S3 (Raw)

↓

Databricks Bronze Layer

↓

Silver Layer (Clean & Validated)

↓

Gold Layer (Business Analytics)

↓

Athena + Redshift Serverless

## Technology Stack

* AWS S3
* AWS Glue
* Athena
* Redshift Serverless
* Databricks
* PySpark
* Delta Lake
* Airflow
* Terraform
* CloudWatch

## Features

* Bronze / Silver / Gold architecture
* Incremental ETL
* Data Quality Validation
* Delta MERGE
* Partition Optimization
* Airflow Orchestration
* Infrastructure as Code
* CI/CD

## Project Status

Sprint 1 – Foundation
