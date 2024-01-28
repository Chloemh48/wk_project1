
"""
Chloe Fabro
"""

import sys
import os
import fileinput

def write_file_backwards(file1, file2):

    content = []

    for line in fileinput.input(files=(file1,)):
        content.append(line.rstrip())

    with open(file2, "w") as myfile2:
        for line in reversed(content):
            line = line.strip()
            reversed_line = line[::-1]
            myfile2.write(reversed_line + "\n")
    

def main():
    if len(sys.argv) != 3:
        print('Usage: python argument1 argument2 argument3')
        sys.exit(1)  



    file1 = sys.argv[1]
    file2 = sys.argv[2]

    if not os.path.exists(file1): 
        print(f'File {file1} does not exist.')
        sys.exit(1)

    if not os.path.exists(file2) : 
        print(f'File {file2} does not exist.')
        sys.exit(1)

    write_file_backwards(file1, file2)

if __name__ == "__main__":
    main()


