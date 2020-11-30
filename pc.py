from pynput.keyboard import Key, Controller
import socket
import threading

defaultPort = 3301
defaultIP = "192.168.0.103"
host = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((defaultIP, defaultPort))

keyboard = Controller()

def simulateUp():
	keyboard.press(Key.up)
	keyboard.release(Key.up)

def simulateDown():
	keyboard.press(Key.down)
	keyboard.release(Key.down)

def simulateRight():
	keyboard.press(Key.right)
	keyboard.release(Key.right)

def simulateLeft():
	keyboard.press(Key.left)
	keyboard.release(Key.left)

def simulateSpace():
	keyboard.press(Key.space)
	keyboard.release(Key.space)

def simulateEnter():
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)

def simulateEsc():
	keyboard.press(Key.escape)
	keyboard.release(Key.escape)

def simulateShoot():
	keyboard.press('x')
	keyboard.release('x')

def simulateSpecial():
	keyboard.press('v')
	keyboard.release('v')

def simulateDash():
	keyboard.press(key.leftshift)
	keyboard.release(key.leftshift)

threadUp = threading.Thread(target=simulateUp)
threadDown = threading.Thread(target=simulateDown)
threadRight = threading.Thread(target=simulateRight)
threadLeft = threading.Thread(target=simulateLeft)
threadJump = threading.Thread(target=simulateSpace)
threadShoot = threading.Thread(target=simulateShoot)
threadSpecial = threading.Thread(target=simulateSpecial)
threadDash = threading.Thread(target=simulateDash)
threadEsc = threading.Thread(target=simulateEsc)
threadEnter = threading.Thread(target=simulateEnter)

def listenForMsg():
	while True:
		try:
			msg = s.recv(1024)
			msg = msg.decode('utf-8')
			if msg == "up":
				threadUp.start()
			if msg == "down":
				threadDown.start()
			if msg == "right":
				threadRight.start()
			if msg == "left":
				threadLeft.start()
			if msg == "jump":
				threadJump.start()
			if msg == "shoot":
				threadShoot.start()
			if msg == "special":
				threadSpecial.start()
			if msg == "dash":
				threadDash.start()
			if msg == "esc":
				threadEsc.start()
			if msg == "enter":
				threadEnter.start()
		except Exception as e:
			print(e)
			pass

listenForMsg()
