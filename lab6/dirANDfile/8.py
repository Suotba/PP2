import os

def delete_file(file_to_delete):
    if os.path.exists(file_to_delete):
        os.remove(os.path.join(os.path.dirname(file_to_delete), os.path.basename(file_to_delete)))
        print("Deleted successfully")
    else:
        print("Path is wrong or non-exist")
file_to_delete = 'exampl.txt'

delete_file(file_to_delete)
