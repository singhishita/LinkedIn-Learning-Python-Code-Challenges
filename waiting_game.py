from random import randint
from time import perf_counter

def waiting_game():
	target_wait = randint(2,7) #target wait seconds
	print("\nYour waiting time is {} seconds".format(target_wait))

	input('-----Press Enter to Begin The Game-----')
	start_time = perf_counter()

	input('-----Press Enter again after {} seconds-----'.format(target_wait))
	end_time = perf_counter()
	delay = end_time - start_time #delay is the difference in time

#print comments as per the result
	print('\nElapsed Time = {0:.3f} seconds'.format(delay))
	if delay == target_wait:
		print("Wow! You did it!")
	elif delay < target_wait:
		print("{0:.3f} seconds too fast".format(target_wait - delay))
	else:
		print("{0:.3f} seconds too slow".format(delay - target_wait))
