import os

def check_path_access(path):
    if os.path.exists(path):
        print("The path exists.")

        if os.access(path, os.R_OK):
            print("The path is readable.")
        else:
            print("The path is not readable.")

        if os.access(path, os.W_OK):
            print("The path is writable.")
        else:
            print("The path is not writable.")

        if os.access(path, os.X_OK):
            print("The path is executable.")
        else:
            print("The path is not executable.")
    else:
        print("The path does not exist.")

path = 'Way/example1/'

check_path_access(path)
