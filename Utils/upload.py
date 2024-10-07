import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access variables
credentials_path = os.getenv("GOOGLE_SHEET_CREDENTIALS_PATH")
api_key = os.getenv("SECRET_API_KEY")

# Step 1: Set up credentials and access to Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
client = gspread.authorize(creds)

# Step 2: Open the Google Sheet
try:
    sheet = client.open("Dummy Sheets").get_worksheet(2)  # Open the third sheet for script upload
except gspread.SpreadsheetNotFound:
    print("Spreadsheet not found. Please check the name and permissions.")
    exit()
except Exception as e:
    print("An error occurred while opening the spreadsheet:", str(e))
    exit()  # Exit if we can't open the sheet

# Step 3: Read CSV file
csv_file_path = '../Data/raw_data.csv'
try:
    df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    print(f"CSV file not found at path: {csv_file_path}")
    exit()  # Exit if we can't read the CSV

# Step 4: Upload data to Google Sheets
try:
    # Get the number of existing rows in the sheet
    existing_rows = len(sheet.get_all_values())
    
    # Insert the DataFrame rows starting from the row after the last existing row
    sheet.insert_rows(df.values.tolist(), existing_rows + 1)  # Append data after existing rows
    print(f"Successfully uploaded {len(df)} rows to Google Sheets.")
except Exception as e:
    print("Error uploading data to Google Sheets:", str(e))
