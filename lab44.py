import time
from lab40 import lab40
from lab41 import lab41
from lab42 import lab42
tm=[]
for i in range(3):
    exe='lab4'+str(i)+'()'
    tmin=time.time()
    for j in range(100):
        exec(exe)
    tm+=[f'{exe[:-2]}: {time.time()-tmin:.4f}s for 100 loops']
for i in tm:
    print(i)