import os
def traverse_file(path):
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            yield file

        elif os.path.isdir(file_path):
            traverse_file(file_path)
path='downloads'
for i in traverse_file(path=path):
    pass