import os, shutil
os.chdir('C:/Users/Max/Documents/University/CP1404/Prac10/FilesToSort')
location_of_files = 'C:/Users/Max/Documents/University/CP1404/Prac10/FilesToSort'


file_types = ["xlsx", "xls", "txt", "png", "jpg", "gif", "docx", "doc"]
for file_type in file_types:
    file_name = input("what category would you like to sort {} into? ".format(file_type))
    try:
        os.mkdir(location_of_files + '/' + file_name)
    except FileExistsError:
        pass

    for files in os.listdir():
        if files.endswith(file_type):
            shutil.move(files, location_of_files + '/' + file_name)