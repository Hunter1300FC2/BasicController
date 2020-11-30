import RPi.GPIO as GPIO
import threading
import socket

defaultPort = 3301
defaultIP = "192.168.0.103"
host = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((defaultIP, defaultPort))
s.listen(1)

clientsocket, address = s.accept()
print(f"Connection from {address} has been established.")

upPin = 8
downPin = 10
rightPin = 12
leftPin = 16
jumpPin = 18
shootPin = 22
specialPin = 24
dashPin = 26
escPin = 3
enterPin = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(upPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(downPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(rightPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leftPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(jumpPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(shootPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(specialPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dashPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(escPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(enterPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def listenForKeyUp():
	while True:
		if GPIO.input(upPin) == GPIO.HIGH:
			msg = 'up'
			clientsocket.send(bytes(msg, 'utf-8'))
			listenForKeyUp()

def listenForKeyDown():
	while True:
		if GPIO.input(downPin) == GPIO.HIGH:
			msg = 'down'
			clientsocket.send(bytes(msg, 'utf-8'))
			listenForKeyDown()

def listenForKeyRight():
	while True:
		if GPIO.input(rightPin) == GPIO.HIGH:
			msg = 'right'
			clientsocket.send(bytes(msg, 'utf-8'))
			listenForKeyRight()

def listenForKeyLeft():
	while True:
		if GPIO.input(leftPin) == GPIO.HIGH:
			msg = 'left'
			clientsocket.send(bytes(msg, 'utf-8'))
			listenForKeyLeft()

def listenForKeyJump():
	while True:
		if GPIO.input(jumpPin) == GPIO.HIGH:
			msg = 'jump'
			clientsocket.send(bytes(msg, 'utf-8'))
			listenForKeyJump()

def listenForKeyShoot():
	while True:
		if GPIO.input(shootPin) == GPIO.HIGH:
			msg = 'shoot'
			clientsocket.send(bytes(msg, 'utf-8'))
			listenForKeyShoot()

def listenForKeySpecial():
	while True:
		if GPIO.input(specialPin) == GPIO.HIGH:
			msg = 'special'
			clientsocket.send(bytes(msg, 'utf-8'))
			listenForKeySpecial()

def listenForKeyDash():
	while True:
		if GPIO.input(dashPin) == GPIO.HIGH:
			msg = 'dash'
			clientsocket.send(bytes(msg, 'utf-8'))
			listenForKeyDash()

def listenForKeyEsc():
	while True:
		if GPIO.input(escPin) == GPIO.HIGH:
			msg = 'esc'
			clientsocket.send(bytes(msg, 'utf-8'))
			listenForKeyEsc()

def listenForKeyEnter():
	while True:
		if GPIO.input(enterPin) == GPIO.HIGH:
			msg = 'enter'
			clientsocket.send(bytes(msg, 'utf-8'))
			listenForKeyEnter()

listenUp = threading.Thread(target=listenForKeyUp)
listenDown = threading.Thread(target=listenForKeyDown)
listenRight = threading.Thread(target=listenForKeyRight)
listenLeft = threading.Thread(target=listenForKeyLeft)
listenJump = threading.Thread(target=listenForKeyJump)
listenShoot = threading.Thread(target=listenForKeyShoot)
listenSpecial = threading.Thread(target=listenForKeySpecial)
listenDash = threading.Thread(target=listenForKeyDash)
listenEsc = threading.Thread(target=listenForKeyEsc)
listenEnter = threading.Thread(target=listenForKeyEnter)

listenUp.start()
listenDown.start()
listenRight.start()
listenLeft.start()
listenJump.start()
listenShoot.start()
listenSpecial.start()
listenDash.start()
listenEsc.start()
listenEnter.start()