"""
this app is about optimum coagulant dose calcualtion
"""
import json
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
"""
Getting access to googlesheet (inspired from lovesandwithces project)
"""
creds = json.load(open('creds.json'))
CREDS = Credentials.from_service_account_info(creds)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("coagulant_dose")


def intro_app():
    """
    explain what app is about
    """
    print('What is this app about?')
    print('-This app is about optimum coagulant dose calculation')
    print('-The optimum dose is calcualted based on lab result')
    print('-Total coagulant dose is calculated based on user input value')
    print('- Googlesheet has four worksheets: pHRAW, pHRAW2, pHRAW3, pHRAW4')
    print('   - pHRAW refers to experimental conidition 1 at pH = 7.0')
    print('   - pHRAW2 refers to experimental conidition 2 at pH = 7.5')
    print('   - pHRAW3 refers to experimental conidition 3 at pH = 8.0')
    print('   - pHRAW4 refers to experimental conidition 4 at pH = 8.5')


intro_app()


def get_exp_data_from_google(sheet):
    """
    get data from google sheet
    """
    pHRAW = SHEET.worksheet(sheet)
    data = pHRAW.get_all_values()
    return data


def validate(data):
    """
    data validate with criteria of nummeric and positive except table heading
    """
    coagulant_dose = []
    pHCoag = []
    res = []
    for row in data[1:]:
        coagulant_dose.append(float(row[0]))
        pHCoag.append(float(row[1]))
        res.append(float(row[2]))
    return coagulant_dose, pHCoag, res


def find_optimum(ph_values, res_values):
    """
    find optimum coagulant dose from the experimental data
    """
    for i, res in enumerate(res_values):
        if res <= 2 and ph_values[i] >= 6 and ph_values[i] <= 7:
            return i
    return None


def get_optimum_value(sheet_name):
    """
    get optimum coagulant dose for all conditions
    """
    data = get_exp_data_from_google(sheet_name)
    # 'validate google sheet the data'
    try:
        cog, ph, res = validate(data)
        optimum_row = find_optimum(ph, res)
        if optimum_row is not None:
            print(f" Optimum dose is {cog[optimum_row]} for {sheet_name}")
            return cog[optimum_row], ph[optimum_row]
        return None
    except ValueError:
        print("Google sheet data is not valid ! Please check the data entry")
        return None


def get_dose_data():
    """
    Get dose calcualtion input from the user.
    We run a while loop to collect a valid string of data from the user
    via the terminal. The loop will repeatedly request data, until it is valid.
    """
    frate = get_valid_input("Enter flow rate in m3/s:\n")
    print(f"The data provided is {frate}")
    st_time = get_valid_input("Enter storage time in month:\n")
    print(f"The data provided is {st_time}")
    return frate, st_time


def next_available_row(worksheet):
    """
    get next available row in the worksheet for the data input
    """
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)


def get_valid_input(message):
    """
    validate the user input data
    """
    while True:
        try:
            # 'Convert it into integer'
            input_val = input(message)
            input_val = int(input_val)
            if input_val > int(0):
                return input_val
            print("Enter value can't be zero or negative, try again")
        except ValueError:
            try:
                # Convert it into float
                input_val = float(input_val)
                if input_val > float(0):
                    return input_val
                print("Enter value can't be zero or negative, try again")
            except ValueError:
                print('Please enter numeric value greater than 0')


def calculate_value(sheet_name, frate, st_time):
    """
    calcualte based on the user input data
    """
    cog, pH = get_optimum_value(sheet_name)
    worksheet = SHEET.worksheet('dose')
    row = next_available_row(worksheet)

    worksheet.update('C' + row, cog)
    worksheet.update('B' + row, pH)
    worksheet.update('A' + row, frate)
    worksheet.update('D' + row, st_time)
    worksheet.update('E' + row, float(frate)*float(cog)*86.4)
    worksheet.update('F' + row, (float(frate)*float(cog)*864))
    worksheet.update('G' + row, (float(frate)*float(cog)*0.864))
    worksheet.update('H' + row, (float(frate)*float(cog)*216))
    worksheet.update('I' + row, (float(frate)*float(cog)*0.216))
    worksheet.update('J' + row, (float(frate)*float(cog)*float(st_time)*6.48))
    worksheet.update('K' + row, sheet_name)
    row = worksheet.row_values(row)
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
    """
    end of app and instruction for user if they want to restart again
    """
    print('End of the programme')
    print('Please click the run program to restart the app again')


end_app()
