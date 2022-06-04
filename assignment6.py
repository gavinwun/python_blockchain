# 1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.
# 2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.
# 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.
# 4) Adjust the logic to load the file content to work with pickled/ json data.
import pickle
import json

values = []

def load_data(format, filename):
    global values
    if format == 'json':
        with open(filename, mode='r') as f:
            values = json.loads(f.read())
    elif format == 'pickle':
        with open(filename, mode='rb') as f:
            values = pickle.loads(f.read())

def save_data(format, filename):
    if format == 'json':
        with open(filename, mode='w') as f:
            f.write(json.dumps(values))
    elif format == 'pickle':
        with open(filename, mode='wb') as f:
            f.write(pickle.dumps(values))

fileformat = input('Enter file format to use (json or pickle): ')

if fileformat == 'json':
    filename = 'values.json'
if fileformat == 'pickle':
    filename = 'values.pickle'

while True:
    print('Currently using file format ' + fileformat)
    print('1: Enter a value to save into file')
    print('2: Show contents of file saved')
    print('3: Change file format')
    print('q: Quit')

    option = str(input("Enter option: "))

    if option == '1':
        input_val = str(input('Enter a value: '))
        values.append(input_val)
        save_data(fileformat, filename)
    elif option == '2':
        load_data(fileformat, filename)
        print(values)
    elif option == 'q':
        break