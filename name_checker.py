from ValidationException import ValidationException
import re
import ValidationException


def validate_file(file_path):
    # read file
    with open(file_path, "r") as inputFile:
        # get first name of each line
        for line in inputFile:
            line = line.strip()
            #using regular expression to get first name
            firstName = re.split(",", line)[0]
            print(firstName)

            for i in firstName:
                if i.isdigit():
                    print(f'Invalid first name: {firstName}')

def test():
    try:
        validate_file("users.txt")
    except ValidationException as ve:
        print(ve)


test()
