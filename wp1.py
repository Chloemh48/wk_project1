
"""
Chloe Fabro
"""

import sys
import os

def write_file_backwards(file1, file2):

    content = []

    with open(file1, "rb") as myfile:
        byte = myfile.read(1)
        while byte:
            content.append(byte)
            byte = myfile.read(1)

    with open(file2, "wb") as file:
        for byte in reversed(content):
            file.write(byte)
  

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


