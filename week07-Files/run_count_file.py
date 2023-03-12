# run_count_file.py
# # creates a file that counts how many times a program was run
# Author: Declan Fox

FILENAME = "count_file.txt"

def read_number():
    try:
        with open(FILENAME) as f:
            number = int(f.read())
            return number
    except IOError:
        # this file will be created when we write back.
        # no file assumes first time running
        # ie 0 previous runs
        return 0
    
def write_number(number):
    with open(FILENAME, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

# Main
num = read_number()
print (f'We have run this program {num} times')
num += 1
write_number(num)
