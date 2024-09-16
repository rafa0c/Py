#!/usr/bin/env python3

import sys
import random
import time
import os

def displayIntro():
	print('Game Starts now...')
	os.system("pause")
	print('You are on a planet full of dragons. In front of you,')
	os.system("pause")
	print('you see two caves. In one cave, the dragon is friendly')
	os.system("pause")
	print('and will share his treasure with you. The other dragon')
	os.system("pause")
	print('is greedy and hungry, and will eat you on sight.')
	os.system("pause")
	print('')

def chooseCave():
	
	cave = ''
	while cave != '1' and cave != '2':
         print('Which cave will you go into? (1 or 2)')
         cave = input()
         
         return cave

def checkCave(chosenCave):
	print('')
	print('You approach the cave...')
	time.sleep(2)
	print('It is dark and spooky...')
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	time.sleep(2)
	
	friendlyCave = random.randint(1, 2)
	
	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
		print('You Win!')
		print('')
	else:
		print('Gobbles you down in one bite!')
		print('You Loose!')
		print('')
		
		
playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
	caveNumber = chooseCave()
	checkCave(caveNumber)
	print('Do you want to play again? (yes or no)')
	playAgain = input()

    
	print('')

