import os, platform
try:
    import httpx
except:
    os.system('pip install httpx')
os.system('git pull')
print('\033[1;32m [•] Follow For Updates')
os.system('xdg-open https://www.facebook.com/hackerbaba4')
import httpx
bit = platform.architecture()[0]
if bit == '64bit':
    from Pro import Baba
    Baba()
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
