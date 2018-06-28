import os
import time
result = os.popen("ipconfig")
print(result.read())
q=time.strftime('%M', time.localtime(time.time()))
print (str(int(q)+1))
print(time.strftime('%Y-%m-%d_%H-%M', time.localtime(time.time())))