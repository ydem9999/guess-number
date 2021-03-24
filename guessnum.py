import random
start = input('pick a number as a start:')
end = input('pick a number as an end:')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1
	if count > 5:
		print('You loss, too many times!')
		break

	num = input('Guess a number:')
	num = int(num)
	if num == r:
		print('You are right!')
		print('You have guessed', count,'times.')
		break
	elif num > r:
		print('Too big')
	elif num < r:
		print('too small')
	print('You have guessed', count,'times.')
