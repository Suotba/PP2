import os

def analyze_path(given_path):
    if os.path.exists(given_path):
        file_name = os.path.basename(given_path)
        directory_path = os.path.dirname(given_path)

        print("The path exists.")
        print(f"Filename: {file_name}")
        print(f"Directory: {directory_path}")
    else:
        print("The path does not exist.")


path = 'Way/example1/inside_example/finally1.txt'

analyze_path(path)
