# Reddit ETL Pipeline

## Project Overview

This project is an ETL (Extract, Transform, Load) pipeline designed to extract data from the Reddit API, transform it as needed, and load it into an Amazon S3 bucket. It utilizes Apache Airflow for orchestration and can be integrated with Snowflake for data warehousing. 

### Architecture Diagram

![reddit_etl](https://github.com/user-attachments/assets/bf9afe4c-f2d4-46bf-8c61-5316e597e9ef)

### Key Components

1. **Reddit API**: The source of data, providing posts and comments from various subreddits.
2. **Python Script**: Extracts data from the Reddit API and uploads it to S3.
3. **Amazon S3**: Serves as the raw data storage before loading into Snowflake.
4. **Apache Airflow**: Orchestrates the ETL pipeline, scheduling and managing the extraction tasks.
5. **Snowflake**: Data warehousing solution where the transformed data can be loaded for analytics.

## Prerequisites

Before running this project, ensure you have the following:

1. **AWS Account**:
   - An active AWS account to create and manage S3 buckets.

2. **Snowflake Account**:
   - An active Snowflake account if you plan to integrate Snowflake for data warehousing.

3. **Docker**:
   - Docker installed on your machine to run the Airflow web server and scheduler in containers.

4. **Apache Airflow**:
   - Apache Airflow installed in your environment. You can use Docker to set it up easily.

5. **Python Environment**:
   - Python 3.x installed along with pip for managing dependencies.

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Nikunjmistry22/Reddit-ELT-Pipeline.git
   cd Reddit-ELT-Pipeline
   ```
2. **Install Dependencies:**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set Up Environment Variables:**
   <ul><li>Create a .env file in the config/ folder with your AWS and Reddit API credentials.</li></ul>
4. **Deploy Airflow on AWS:**
   <ul>
     <li>Launch an EC2 instance with the required specifications (e.g., Amazon Linux 2, Ubuntu).</li>
     <li>SSH into your EC2 instance and install Docker.</li>
     
     ```bash
    sudo yum update -y   # For Amazon Linux 2
    sudo yum install docker -y
    sudo service docker start
    sudo usermod -a -G docker ec2-user
     ```
     <li>Set up Airflow using Docker Compose or pull the official Airflow Docker image.</li>
     <li>Start Airflow Service<br>
       
     ```bash
       docker-compose up
     ```
     </li>
   </ul>

<hr>
## DB MODEL ON SNOWFLAKE
![ST](https://github.com/user-attachments/assets/ffbd4f0d-7308-4263-9592-5f2aac63212f)

