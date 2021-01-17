import math
import random

def main():
	while True:
		try:
			n = int(input('How many rounds to simulate? (type 0 to exit) '))
			if (n < 0):
				raise
		except:
			print('Not a valid number')
			continue

		if (n == 0):
			break

		x, y = simulate(n)
		displacement = math.sqrt(x ** 2 + y ** 2)
		print(f'The final displacement after {n} rounds is {displacement}, its square is {displacement ** 2}')

def simulate(n):
	x = y = 0

	for i in range(n):
		dx, dy = move()
		x += dx
		y += dy

	return x, y

def move():
	dx = random.uniform(-1, 1)
	dy = math.sqrt(1 - dx ** 2) * random.choice([-1, 1])

	return dx, dy

if __name__ == '__main__':
	main()
