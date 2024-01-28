
"""
Chloe Fabro
"""

def read_file():
    with open("originaltext.txt", "r") as myfile:
        content = myfile.readlines()
        for line in content:
            line = line.strip()
            print(line)
def write_file_backwards():