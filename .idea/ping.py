

import socket


def _checkAddr(addr):
    #answer =  socket.gethostbyaddr(addr)
    try:
        answer =  socket.gethostbyaddr(addr)
        return True
    except:
        return False



answer1 = _checkAddr("www.google.com")
answer2 = _checkAddr("www.google1.com")
answer3 = _checkAddr("www.globes.co.il")



print(answer1)
print(answer2)
print(answer3)
