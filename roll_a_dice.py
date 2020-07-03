from random import randint
from collections import Counter

def roll_dice(*dice, n_trials = 1_00_000):
	counts = Counter()
	for roll in range(n_trials):
		counts[sum((randint(1,sides) for sides in dice))] += 1
		
	print('\nOUTCOME\tPROBABILITY')
	for outcome in range(len(dice), sum(dice)+1):
		print('{}\t{:0.2f}%'.format(outcome, counts[outcome]*100/n_trials))
		
roll_dice(4,6,6) 
