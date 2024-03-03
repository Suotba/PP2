import os

def analyze_path(wa):
    if os.path.exists(wa):
        file_name = os.path.basename(wa)
        directory_path = os.path.dirname(wa)

        print("The path exists.")
        print(f"Filename: {file_name}")
        print(f"Directory: {directory_path}")
    else:
        print("The path does not exist.")


wa = 'Way/example1/inside_example/finally1.txt'

analyze_path(wa)
