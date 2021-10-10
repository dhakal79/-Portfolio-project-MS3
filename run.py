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


def intro_app():
    """
    """
    print('What is this app about?')
    print('i) This app is about optimum coagulant dose calculation')
    print('ii) The optimum dose is calcualted based on lab result')
    print('iii) Total cogulant dose is calculated based on user input value')
    print('iv)Googlesheet has four worksheets: pHRAW, pHRAW2, pHRAW3, pHRAW4')
    print('- pHRAW refers to experimental conidition 1 at pH = 7.0')
    print('- pHRAW2 refers to experimental conidition 2 at pH = 7.5')
    print('- pHRAW3 refers to experimental conidition 3 at pH = 8.0')
    print('- pHRAW4 refers to experimental conidition 4 at pH = 8.5')


intro_app()


def get_exp_data_from_google(sheet):
     """
    """
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


def get_optimum_value(sheet_name):
     """
    """
    data = get_exp_data_from_google(sheet_name)
    # 'validate the data'
    try:
        cog, ph, res = validate(data)
        optimum_row = find_optimum(ph, res)
        if optimum_row is not None:
            print(f" Optimum dose is {cog[optimum_row]} for {sheet_name}")
            return cog[optimum_row], ph[optimum_row]
    except ValueError:
        print("Data is not valid ! Please check the data entry")

# 'calculating the amount of coagulant dose for a give water flow'


def get_dose_data():
    """
    Get dose calcualtion input from the user.
    We run a while loop to collect a valid string of data from the user
    via the terminal. The loop will repeatedly request data, until it is valid.
    """
    flowrate = get_valid_input("Enter flow rate in m3/s:\n")
    print(f"The data provided is {flowrate}")
    storage_time = get_valid_input("Enter storage time in month:\n")
    print(f"The data provided is {storage_time}")
    return flowrate, storage_time


def next_available_row(worksheet):
    """
    """
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)


def get_valid_input(message):
     """
    """
    while True:
        try:
            # 'Convert it into integer'
            input_val = input(message)
            input_val = int(input_val)
            if input_val > int(0):
                break
            else:
                print("Enter value can't be zero or negative, try again")
        except ValueError:
            try:
                # Convert it into float
                input_val = float(input_val)
                if input_val > float(0):
                    break
                else:
                    print("Enter value can't be zero or negative, try again")
            except ValueError:
                print('Please enter numeric value greater than 0')
    return input_val


def calculate_value(sheet_name, flowrate, storage_time):
     """
    """
    cog, pH = get_optimum_value(sheet_name)
    worksheet = SHEET.worksheet('dose')
    row_number = next_available_row(worksheet)

    worksheet.update('C' + row_number, cog)
    worksheet.update('B' + row_number, pH)
    worksheet.update('A' + row_number, flowrate)
    worksheet.update('D' + row_number, storage_time)
    worksheet.update('E' + row_number, float(flowrate)*float(cog)*86.4)
    worksheet.update('F' + row_number, (float(flowrate)*float(cog)*864))
    worksheet.update('G' + row_number, (float(flowrate)*float(cog)*0.864))
    worksheet.update('H' + row_number, (float(flowrate)*float(cog)*216))
    worksheet.update('I' + row_number, (float(flowrate)*float(cog)*0.216))
    worksheet.update('J' + row_number, sheet_name)
    row = worksheet.row_values(row_number)
    pretty_array = []
    for item in worksheet.row_values(1):
        pretty_array.append([item])
    for i, item in enumerate(row):
        pretty_array[i].append(item)
    for row in pretty_array:
        label, value = row
        print(f'  - {label}: {value}')


flowrate, storage_time = get_dose_data()
calculate_value('pHRAW', flowrate, storage_time)
calculate_value('pHRAW2', flowrate, storage_time)
calculate_value('pHRAW3', flowrate, storage_time)
calculate_value('pHRAW4', flowrate, storage_time)


def end_app():
    print('Please click the run program to restart the app again')
   

end_app()