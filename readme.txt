
This script is designed to read the contents of one file and write them in reverse order to another file. 

Requirements:
Python3
Two files needed. The script reads from the first file and writes the contents in reverse order to the second file.

Usage:
To use the script, you need to provide two command line arguments: the source file (file1) and the destination file (file2). The command should be structured as follows:

Copy code
python wp1.py file1 file2
Replace wp1.py with the actual name of your Python script, file1 with the path to the source file, and file2 with the path to the destination file.

Example:
python wp1.py file1 file2
This command will take the contents of source.bin, reverse the order of the bytes, and then write them to destination.bin.

Important Notes:
Ensure both file1 and file2 exist before running the script. The script checks for the existence of both files and will exit with an error message if either is not found.
The script works in binary mode ('rb' for reading and 'wb' for writing), which makes it suitable for any file type, including text and binary files.

Error Handling:
If the correct number of arguments is not provided, the script will display a usage message and exit.
If either of the specified files does not exist, the script will display an error message indicating which file was not found and then exit.