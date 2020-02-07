import os
import os.path
import re


def parse():                                                            # Function to search through dirs/subdirs for files
    workingD = "<working directory>"
    Specific_files = []
    os.chdir(workingD)
    for root, dirs, files in os.walk(workingD, topdown = True):         # Recursively searching parent dirs to pull out files
        for name in files:
            filepath = os.path.join(root, name)                         # Creates a file path for the file by conjoining the root with the name
            Specific_files.append({"name": name, "filepath": filepath})     # Appends the name of file and path to a list
    return Specific_files                                               # Returns the list


def file_parse():                                               # Function to parse through the files contents using Regex
    file_dict = parse()                     # Call back to the list
    data_dict = []
    overflow = []
    for i in file_dict:
        with open(i['filepath'], 'r') as search_file:
            print(i['filepath'])                            # Prints out the file path being parsed. Totally unnecesary but it helps you see where the process is at and it looks cool as it runs.
            contents = search_file.read()
            data = re.findall(r"(.*?)", contents, re.I)                 # Regex to search through the file, case ignored
            data_dict.append(data)                          # Appends the data found to a list in order to be split apart and check for originality.
    with open('[FILE LOCATION]', 'w') as document:
        for item in str(suspicious_dict).split(","):
            while item not in overflow:                         # Checks the data through a list in order to rid of duplicates
                overflow.append(item)
                document.write("%s\n" % item)          # Python3

file_parse()

