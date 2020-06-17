from socket import socket, AF_INET,SOCK_DGRAM
from threading import Thread 
from multipledispatch import dispatch 


class Tello:
    sock : socket = None
    tello_address = None

    def __init__(self,address: str='', port: int = 9000, tello_address: str = '192.168.10.1', tello_port: int=8889):

        # Save the tello address
        self.tello_address=(tello_address, tello_port)

        # Set the socket and bind it to a port
        self.sock=socket(AF_INET, SOCK_DGRAM)
        self.sock.bind((address, port))

        self.command()
        data, server = self.sock.recvfrom(1518)

        # if data != 'ok':


        # # recive messages that comes from the threading
        # Thread(target=self.recv).start()

    def send(self, msg):
        self.sock.sendto(msg.encode(encoding="utf-8") , self.tello_address)
    
    def recv(self):
        while True: 
            try:
                data, server = self.sock.recvfrom(1518)
                print(data.decode(encoding="utf-8"))
            except Exception:
                print ('\nExit . . .\n')
                break

    def command(self):
        self.send('command')

    def takeoff(self):
        self.send('takeoff')

    def land(self):
        self.send('land')

    def streamon(self):
        self.send('streamon')

    def streamoff(self):
        self.send('streamoff')

    def emergency(self):
        self.send('emergency')

    def up(self, x):
        self.send(f'up {x}')

    def down(self, x):
        self.send(f'down {x}')

    def left(self, x):
        self.send(f'left {x}')

    def right(self, x):
        self.send(f'right {x}')

    def forward(self, x):
        self.send(f'forward {x}')

    def back(self, x):
        self.send(f'back {x}')

    def cw(self, x):
        self.send(f'cw {x}')

    def ccw(self, x):
        self.send(f'ccw {x}')

    def flip(self, x):
        self.send(f'flip {x}')

    @dispatch(int,int,int,int)
    def go(self, x, y, z, speed):
        self.send(f'go {x} {y} {z} {speed}')

    def stop(self):
        self.send('stop')

    @dispatch(int,int,int,int,int,int,int)
    def curve(self, x1, y1, z1, x2, y2, z2, speed):
        self.send(f'curve {x1} {y1} {z1} {x2} {y2} {z2} {speed}')

    @dispatch(int,int,int,int, int)
    # pylint: disable=function-redefined
    def go(self, x, y, z, speed, mid):
        self.send(f'go {x} {y} {z} {speed} {mid}')

    @dispatch(int,int,int,int,int,int,int,int)
    # pylint: disable=function-redefined
    def curve(self, x1, y1, z1, x2, y2, z2, speed, mid):
        self.send(f'curve {x1} {y1} {z1} {x2} {y2} {z2} {speed} {mid}')

    def jump(self, x, y, z, speed, yaw, mid1, mid2):
        self.send(f'jump {x} {y} {z} {speed} {yaw} {mid1} {mid2}')

    def speed(self, x):
        self.send(f'speed {x}')

    def rc(self, a, b, c, d):
        self.send(f'rc {a} {b} {c} {d}')

    def wifi(self, ssid, passwod):
        self.send(f'wifi {ssid} {passwod}')

    def mon(self):
        self.send('mon')

    def moff(self):
        self.send('moff')

    def mdirection(self, x):
        self.send(f'mdirection {x}')

    def ap(self, ssid, passwod):
        self.send(f'ap {ssid} {passwod}')

    def get_speed(self):
        self.send('speed?')

    def get_battery(self):
        self.send('battery?')

    def get_time(self):
        self.send('time?')

    def get_wifi(self):
        self.send('wifi?')

    def get_sdk(self):
        self.send('sdk?')

    def get_sn(self):
        self.send('sn?')