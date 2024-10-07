import os
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

# Load environments from .env file
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

# Step 3: Retrieve original values from the Google Sheet
try:
    original_values = sheet.get_all_values()  # Retrieve all values from the sheet
    column_values = [row[0] for row in original_values]  # Extract the first column values

    # Get unique values using a set
    unique_values = list(set(column_values))  # Convert set back to list

    # Convert to DataFrame
    df = pd.DataFrame(unique_values, columns=["Unique Values"])  # Add a column name for better clarity

    # Step 4: Upload DataFrame to Google Sheets
    sheet.clear()  # Clear existing data in the sheet
    sheet.insert_rows(df.values.tolist(), 1)  # Insert new data starting from the first row

    print(f"Successfully cleaned the data and updated {len(df)} unique rows to Google Sheets.")

except Exception as e:
    print("Error retrieving data from Google Sheets:", str(e))
