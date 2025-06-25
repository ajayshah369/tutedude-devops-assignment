

# Create a text file and write some content to it

file_path = "output.txt"

with open(file_path, "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("We are writing some text into this file.\n")
    file.write("Python makes file operations easy!\n")

print(f"Content written to {file_path}")