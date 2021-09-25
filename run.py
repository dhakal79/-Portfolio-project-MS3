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
    while True:
        print("Please enter lab experimental data")
        print("data should be three numbers separated by commas")
        print("Example:0,7.5,105\n")
        data_str = input("Enter your data here:")

        exp_data = data_str.split(",")
        if validate_data(exp_data):
            print("data is valid")
            break

    return exp_data

def validate_data(values):

    try:
        [int(value) for value in values]
        if len(values) != 3:
            raise ValueError(
                f"Exactly 3 values are required, you provided {len(values)}")

    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False
    return True    
get_exp_data()