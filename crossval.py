import os
import random
import sys
import shutil

path = sys.argv[1]

enroll_part = 0.3 #sys.argv[2]
classes_part = 0.5

os.chdir(path)

if os.path.exists(os.path.join(path, 'database')):
    shutil.rmtree(os.path.join(path, 'database'))

os.mkdir(os.path.join(path, 'database'))

os.mkdir(os.path.join(path, 'database','enroll'))
os.mkdir(os.path.join(path, 'database','classes'))
os.mkdir(os.path.join(path, 'database','4recognition'))

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    if 'database' not in r:
        if len(f) != 0:
            os.mkdir(os.path.join(path, 'database','classes', os.path.basename(r)))
        files = []
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(r, file))
        c = len(files)
        random.shuffle(files)
        enroll_len = int(enroll_part*c)
        classes_len = int(classes_part*c)
        for index in range(enroll_len):
            shutil.copy(files[index], os.path.join(path, 'database','enroll'))
        for index in range(enroll_len,enroll_len+classes_len):
            shutil.copy(files[index], os.path.join(path, 'database','classes', os.path.basename(r)))
        for index in range(enroll_len+classes_len, c):
            shutil.copy(files[index], os.path.join(path, 'database','4recognition'))