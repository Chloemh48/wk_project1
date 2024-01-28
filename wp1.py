
"""
Chloe Fabro
"""

def read_file():

    file = "riginaltext.txt"
    try:
        with open(file, "r") as myfile:
            content = myfile.readlines()
            for line in content:
                line = line.strip()
                print(line)
    except FileNotFoundError:
        print(f"{file} not exsit")
    
def write_file_backwards():
    pass

if __name__ == "__main__":
    read_file()

