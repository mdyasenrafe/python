import glob
import shutil
import os

postfix = [1, 2]
source_path = '../source/*'
destination_path = '../destination'
while True:
    # path finder
    source_obj = glob.glob(source_path)

    # path name array
    obj_path = source_obj[0]
    shutil.copy(obj_path, '.')

    obj_name = obj_path.split('\\')[-1].split(".")
    prefix = obj_name[0]
    postfix2 = obj_name[1]

    for i in range(len(postfix)):
        file_name = prefix + "_" + str(i) + "." + postfix2
        shutil.copy(obj_path, f'{destination_path}/{file_name}')

    os.remove(obj_path)
    os.remove(obj_path.split('\\')[-1])
    print("Done")
