from tello_done_helper import Tello



# import threading 
# import socket

# host = ''
# port = 9000
# locaddr = (host,port) 


# # Create a UDP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# tello_address = ('192.168.10.1', 8889)

# sock.bind(locaddr)

# def recv():
#     while True: 
#         try:
#             data, server = sock.recvfrom(1518)
#             print(data.decode(encoding="utf-8"))
#         except Exception:
#             print ('\nExit . . .\n')
#             break


# print ('\r\n\r\nTello Python3 Demo.\r\n')

# print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

# print ('end -- quit demo.\r\n')


# #recvThread create
# recvThread = threading.Thread(target=recv)
# recvThread.start()

# while True: 

#     try:
#         msg = input("")

#         if not msg:
#             break  

#         if 'end' in msg:
#             print ('...')
#             sock.close()  
#             break

#         # Send data
#         sent = sock.sendto(msg.encode(encoding="utf-8") , tello_address)
#     except KeyboardInterrupt:
#         print ('\n . . .\n')
#         sock.close()  
#         break



