#Import necessary libraries for Google API authentication and requests
import pandas as pd

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Define the scope for Google Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = 'secret_key/keys.json'
SPREADSHEET_ID = '1CHSfRQTla3Kkang7E_PptCKc6WYMIlzwDoe_hgMMajE'
RANGE_NAME = "supermarket_transactions!A1:L50784"

# Main function to read data from Google Sheets
def main():
    try:
        # Authenticate using service account credentials
        creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        # Build the Google Sheets API service
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()

        # Call the Sheets API to get the data from the specified range
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return
        # Print the retrieved data
        print(f"Rows fetched: {len(values)}")

        # Convert the data to pandas DataFrame for further processing
        headers = values[0]  # First row as headers
        data = values[1:]    # Remaining rows as data
        df = pd.DataFrame(data, columns=headers)
        print(df.head())  # Print the first few rows of the DataFrame

    except HttpError as error:
        print(f"An error occurred: {error}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")    

if __name__ == '__main__':
    main()  
    