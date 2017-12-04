"""Main module for yo_indexer"""
import csv
import os

def examine_csv():
    """The main function"""
    # Count the Yo Index
    count = 0

    # Get the system file path
    file_name = "Yo.csv"
    file_path = os.path.join(os.path.dirname(__file__), 'csv_files/' + file_name)
    with open(file_path) as file:
        reader = csv.reader(file, delimiter=',', quotechar='|')
        for row in reader:
            for entry in row:
                has_data = len(entry)
                if has_data != 0:
                    count += 1
    yo_index = count
    print('Yo index:' + str(yo_index))

    # Compare to other group files
    files = ['GitHub.csv']
    for file_name in files:
        file_path = os.path.join(os.path.dirname(__file__), 'csv_files/' + file_name)

        count = 0
        with open(file_path) as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')

            # Features = number of cells
            for row in reader:
                for entry in row:
                    has_data = len(entry)
                    if has_data != 0:
                        count += 1

        print("Number of features for " + file_name + ': ' + str(count))
        print("Yo index for " + file_name + ': ' + str(count/yo_index))

    # Compare to our files (different format)
    files = ['Gmail.csv', 'Windows Mail.csv', 'Windows Outlook.csv']
    for file_name in files:
        file_path = os.path.join(os.path.dirname(__file__), 'csv_files/' + file_name)

        count = 0
        with open(file_path) as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')

            # Features = number of rows
            for row in reader:
                count += 1

        print("Number of features for " + file_name + ': ' + str(count))
        print("Yo index for " + file_name + ': ' + str(count/yo_index))
