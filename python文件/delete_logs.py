import os

rootdir = 'D:\\GCloud\\log\\dtdCheckOfCity'
list = os.listdir(rootdir)
for i in range(0, len(list)):
    try:
        path = os.path.join(rootdir, list[i])
        path = path.replace('\\', '/')
        if os.path.exists(path):
            os.remove(path)
    except Exception as e:
        print(e)
        pass
