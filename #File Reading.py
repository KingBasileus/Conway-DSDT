#File Reading
import json
import csv

json_file = '/workspaces/Conway-DSDT/Files_for_import/ex_file.json'
csv_file = '/workspaces/Conway-DSDT/Files_for_import/home_loan_complaints-2 (1).csv'

#Getting the input
user_input = input('Do you want to open the CSV or JSON file :)')
option = str(user_input).upper()

if option == "JSON" or option == "CSV":
    print("Thnak you, printing")
    #Open Json File
    if option == "JSON":
        with open(json_file, 'r') as file:
            data_json = json.load(file)

    #Printing it out
        for item in data_json:
            print("-----  " + item['_id'] + "  -----")
            print(item['name'])
            print(item['email'])
            print(item['age'])
            print(item['is_active'])
            print(item['roles'])
            print(item['created_at'])
            print()
        print("FINISHED JSON FILE PRINT")

    #Open CSV File
    elif option == "CSV":
        with open(csv_file, 'r') as file:
            data_csv = csv.DictReader(file)
            for row in data_csv:
                print("-----  " + row['user_id'] + "  -----")
                print(row['Date received'])
                print(row['Issue'])
                print(row['Consumer complaint narrative'])
                print(row['State'])
                print(row['ZIP code'])
                print(row['Date sent to company'])
                print(row['Company response to consumer'])
                print(row['Timely response?'])
                print(row['Consumer disputed?'])
                print(row['Complaint ID'])
                print()
            print("FINISHED CSV FILE PRINT")

else:
    print('Invalid input')

