# file_reverser.py
def reverse_file(input_file, output_file):
    """Read a file and write its content in reverse order to another file."""
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
        
        with open(output_file, 'w') as file:
            for line in reversed(lines):
                file.write(line)
        print(f"File reversed successfully! Check {output_file} for the result.")
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'output.txt'
    reverse_file(input_file, output_file)
