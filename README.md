# **Data-Ingestion**
## ***Project decription***
A python ETL project to extract data from google sheet and load it to Postgress database

## ***features***
- Extract: Read data from google sheet using Google service account
- Transform: Clean and formart the data
- Load: Load the data into Postgress Database

## 1. **Extract Data From Google Sheet**
- Go to [Google cloud Console](https://developers.google.com/workspace/sheets/api/quickstart/python)
- Create a new project
- Navigate to API and services- Library and enable:
     - Google Sheet API
     - Google Drive API 
- Create a service account under ** IAM & ADMIN - Service account **
- Using the service account Create a key(JSON) and save it to your workspace
- Share your google sheet with the ***client_email*** from the JSON file

  
