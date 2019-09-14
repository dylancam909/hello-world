import random

number = random.randint(1,9)
count = 1

while count > 0:
    okay = input('guess number')

    if okay == 'exit':
        break

    okay = int(okay)
    if okay < number:
        print('too low')
    elif okay > number:
        print('too high')
    elif okay == number:
        print('got it with', count, 'tries')
        break
    count += 1
