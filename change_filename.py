import os
path = 'Surprised'
files = os.listdir(path)
i = 51

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
    i = i+1