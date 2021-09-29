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

# ' get data from google sheet"


def get_exp_data_from_google(sheet):
    pHRAW = SHEET.worksheet(sheet)
    data = pHRAW.get_all_values()
    return data
# 'validate the data in the google sheet'


def validate(data):
    # 'criteria:should be nummeric and positive except table heading'
    coagulant_dose = []
    pHCoag = []
    res = []
    for row in data[1:]:
        coagulant_dose.append(float(row[0]))
        pHCoag.append(float(row[1]))
        res.append(float(row[2]))
    return coagulant_dose, pHCoag, res
# 'find optimum coagulant dose from the experimental data'


def find_optimum(ph_values, res_values):
    for i, res in enumerate(res_values):
        if res <= 2 and ph_values[i] >= 6 and ph_values[i] <= 7:
            return i
    return None

# 'get the optimum dose for each conditions'


def plot_sheet(sheet_name):
    data = get_exp_data_from_google(sheet_name)
    # 'validate the data'
    try:
        cog, ph, res = validate(data)
        optimum_row = find_optimum(ph, res)
        if optimum_row is not None:
            print(f"Optimum dose {cog[optimum_row]} for {sheet_name}")
    except ValueError:
        print("Data is not valid ! Please check the data entry")


plot_sheet('pHRAW')
plot_sheet('pHRAW2')
plot_sheet('pHRAW3')
plot_sheet('pHRAW4')


# 'calculating the amount of coagulant dose for a give water flow'
def get_dose_data(sheet):
    dose = SHEET.worksheet(sheet)
    data_cal = dose.get_all_values()
    return data_cal


def dose_calcualtion_data():
    """
    Get dose calcualtion input from the user.
    We run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """

    while True:
        print("Please enter data from the given condition.")
        print("Data should be three numbers, separated by commas.")
        print("Example: 1,2,3\n")
        data_str = input("Enter your data here: \n")

        dose_data = list(data_str.split(","))

        if validate_data(dose_data):
            break

    return dose_data

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """

    try:
        [int(value) for value in values]
        if len(values) != 3:
            raise ValueError(
                f"Exactly 3 values are required, you provided {len(values)}")

    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False

    return True

