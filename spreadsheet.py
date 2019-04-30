import gspread
from oauth2client.service_account import ServiceAccountCredentials

service = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_keys.json', service)
client = gspread.authorize(credentials)

spreadsheet = client.open('Civics (Responses)').sheet1

def get_survey_results():

    all_results = []
    food_answers = ['Nachos', 'Salad']
    yes_no_answers = ['Yes', 'No']
    value_counts = {'nachos_num': 0, 'salad_num': 0, 'bathroom_yes': 0, 'bathroom_no': 0, 'cc_yes': 0, 'cc_no': 0, 'golf_yes': 0, 'golf_no': 0, 'hallway_yes': 0, 'hallway_no': 0}

    for num in range(2, 7):
        if spreadsheet.col_values(num) not in all_results:
            all_results.append(spreadsheet.col_values(num))

    for answer in all_results[0]:
        if answer == food_answers[0]:
            value_counts['nachos_num'] += 1
        elif answer == food_answers[1]:
            value_counts['salad_num'] += 1
        else:
            pass

    for answer in all_results[1]:
        if answer == yes_no_answers[0]:
            value_counts['bathroom_yes'] += 1
        elif answer == yes_no_answers[1]:
            value_counts['bathroom_no'] += 1
        else:
            pass

    for answer in all_results[2]:
        if answer == yes_no_answers[0]:
            value_counts['cc_yes'] += 1
        elif answer == yes_no_answers[1]:
            value_counts['cc_no'] += 1
        else:
            pass

    for answer in all_results[3]:
        if answer == yes_no_answers[0]:
            value_counts['golf_yes'] += 1
        elif answer == yes_no_answers[1]:
            value_counts['golf_no'] += 1
        else:
            pass

    for answer in all_results[4]:
        if answer == yes_no_answers[0]:
            value_counts['hallway_yes'] += 1
        elif answer == yes_no_answers[1]: 
            value_counts['hallway_no'] += 1
        else:
            pass

    print(f'{spreadsheet.cell(1,2).value}')
    print(f'{food_answers[0]}: {value_counts["nachos_num"]}')
    print(f'{food_answers[1]}: {value_counts["salad_num"]}\n')
    print(f'{spreadsheet.cell(1,3).value}')
    print(f'{yes_no_answers[0]}: {value_counts["bathroom_yes"]}')
    print(f'{yes_no_answers[1]}: {value_counts["bathroom_no"]}\n')
    print(f'{spreadsheet.cell(1,4).value}')
    print(f'{yes_no_answers[0]}: {value_counts["cc_yes"]}')
    print(f'{yes_no_answers[1]}: {value_counts["cc_no"]}\n')
    print(f'{spreadsheet.cell(1,5).value}')
    print(f'{yes_no_answers[0]}: {value_counts["golf_yes"]}')
    print(f'{yes_no_answers[1]}: {value_counts["golf_no"]}\n')
    print(f'{spreadsheet.cell(1,6).value}')
    print(f'{yes_no_answers[0]}: {value_counts["hallway_yes"]}')
    print(f'{yes_no_answers[1]}: {value_counts["hallway_no"]}\n')

get_survey_results()