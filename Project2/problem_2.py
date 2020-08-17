import os

def find_files(suffix, path):
    if not os.path.isdir(path):
        return 'Not a dir'

    if type(suffix) is not str:
        return 'Suffix not a string'

    path_list = os.listdir(path)
    files = []
    for item in path_list:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            files += find_files(suffix, item_path)
        elif os.path.isfile(item_path) and item_path.endswith(suffix):
            files.append(item_path)

    return files

print(find_files('.c', './test_files/'))
