# run_counter.py
# counts how many times a program was run
# Author: Declan Fox

FILENAME = "count.txt"

def read_number():
    with open(FILENAME) as f:
        number = int(f.read())
        return number
    
def write_number(number):
    with open(FILENAME, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

# Main
num = read_number()
print (f'We have run this program {num} times')
num += 1
write_number(num)
