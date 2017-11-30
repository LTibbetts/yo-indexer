"""Main module for index_analyzer"""
import csv
import os
from pkg_resources import resource_listdir

def examine_csv():
    """The main function"""
    # Gets a list of all of the files in the csv_files dir
    csv_dir = resource_listdir('index_analyzer.csv_files', '')

    # Loop through them
    for file_name in csv_dir:

        # If it is a .csv then do stuff
        if file_name[-4:] == '.csv':
            print('Examining - ' + file_name)

            # Get the system file path
            file_path = os.path.join(os.path.dirname(__file__), 'csv_files/' + file_name)

            # Open the file
            with open(file_path) as csvfile:
                # Make csv reader
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')

                # Output
                for row in reader:
                    print(row)
                    print('==================================')
                    print(len(row))
        else:
            print('Skipping - ' + file_name)
