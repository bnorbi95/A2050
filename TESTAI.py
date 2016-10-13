from socketIO_client import SocketIO, LoggingNamespace
import sys

myId=1
kmap={"UP":38,"DOWN":40,"LEFT":37,"RIGHT":39}

def algorithm(data):
    """Write your code here"""
    dir=kmap["UP"]
    
    socketIO.emit("aiwrite",dir) #Don't remove this line


def error(msg):
    print(msg)
    sys.exit()

socketIO = SocketIO('desktop', 5000, LoggingNamespace)

socketIO.on('airead', algorithm)
socketIO.on('error', error)

socketIO.emit("aictl",myId)
socketIO.wait()
