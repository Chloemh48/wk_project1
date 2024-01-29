
"""
Chloe Fabro
1/28/2024
Workout_Project1
"""
import sys
import os

def write_file_backwards(file1, file2):
    """
    Reads the contents of file1 and writes them in reverse order to file2.
    """
    content = []

    # Read the file1 byte by byte
    with open(file1, "rb") as myfile:
        byte = myfile.read(1)
        while byte:
            content.append(byte)
            byte = myfile.read(1)

    # Write the content in reverse order to the file2
    with open(file2, "wb") as file:
        for byte in reversed(content):
            file.write(byte)
  

def main():
    # Ensure the correct number of command-line arguments is 3
    if len(sys.argv) != 3:
        print('Usage: python script_name.py file1 file2')
        sys.exit(1)  

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    # if the file1 does not exists, it will print out message and exit the program
    if not os.path.exists(file1): 
        print(f'File {file1} does not exist.')
        sys.exit(1)

    # Call the function to write file1 contents in reverse to file2
    write_file_backwards(file1, file2)

if __name__ == "__main__":
    main()



