# Read from a text file and display its contents

file_path = "output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
