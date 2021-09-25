import gspread
from google.oauth2.service_account import Credentials
import json

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

creds = json.load(open('creds.json'))
CREDS = Credentials.from_service_account_info(creds)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("coagulant_dose")
"""
pHRAW = SHEET.worksheet("pHRAW2")

data = pHRAW.get_all_values()
print(data)
"""
def get_exp_data():
    print("Please enter lab experimental data")
    print("data should be three numbers separated by commas")
    print("Example:0,7.5,105\n")
    data_str = input("Enter your data here:")

    exp_data = data_str.split(",")
    validate_data(exp_data)

def validate_data(values):

    try:
        if len(values) != 3:
            raise ValueError(
                f"Exactly 3 values are required, you provided {len(values)}")

    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        
get_exp_data()