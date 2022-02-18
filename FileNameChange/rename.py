import os

file_path = 'C:\\Users\\sshim\\Desktop\\video'
file_names = os.listdir(file_path)
print(file_names)

for name in file_names:
    src = os.path.join(file_path, name)
    # new_name = name + '.jpg'
    new_name = name.split(".")[0] + '.mp4'
    print(new_name)
    dst = os.path.join(file_path, new_name)
    os.rename(src, dst)
