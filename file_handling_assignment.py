# file_handling_assignment.py

def create_file():
    """Create a new file and write initial content."""
    try:
        with open('my_file.txt', 'w') as file:
            file.write("This is the first line.\n")
            file.write("Here is the second line with a number: 123.\n")
            file.write("Finally, the third line.\n")
        print("File created and initial content written.")
    except PermissionError:
        print("Error: Permission denied while creating the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def read_file():
    """Read and display the content of the file."""
    try:
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("\nFile contents:\n")
            print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied while reading the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def append_to_file():
    """Append additional content to the file."""
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Appending a new line to the file.\n")
            file.write("Another appended line with a number: 456.\n")
            file.write("Yet another appended line.\n")
        print("Additional lines appended to the file.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied while appending to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to execute file operations."""
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read and display content again after appending

if __name__ == "__main__":
    main()
