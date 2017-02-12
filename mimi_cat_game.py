from time import sleep

print ' '
print 'Hello! Welcome to the game Nineth Life.' '\n'  
print 'We are pleased to tell you that a long time ago, in a reality far far away, you were A CAT.' '\n'
print 'A great furry admiral who commanded legions. You prowled the night with your best friend, Colonel Meow, and together you plotted the demise of humans. "Take cover," those furless creatures shouted. "Here comes the mighty..."' '\n'
sleep(1)

player1 = raw_input ('Wait, remind us, what was your fur-name? ')
print ' '
sleep(1)

print '"Take cover," those furless creatures shouted. "Here comes the mighty %s!"' % (player1)
print ' '
sleep(3)

print 'The night welcomes you, %s. You are about to begin your evening patrol. What would you like to do first? ' % (player1)
print ' '
print 'a) Find a snack' '\n' 'b) Explore the neighbor\'s yard' '\n' 'c) Take a nap' '\n'
answer_one = raw_input ('What strikes your fancy? a, b, or c? ').lower()
print ' '
sleep(1)

if answer_one == 'a':
	print 'You chose a) Find a snack!' '\n'
	sleep(1)
	print 'Mmm... a delightful scent floats through the air. Smells like Defenseless Prey! Which way does your nose point? ' '\n'
	print 'a) Left towards the graveyard' '\n' 'b) Right towards the forest' '\n' 'c) Forward towards the town gas station' '\n'
	answer_one_a = raw_input ('What\'ll it be? a, b, or c? ').lower()
	print ' '

	if answer_one_a == 'a':
		print 'You chose a) Left towards the graveyard!' '\n'
		sleep(1)
		print'Mmm... so many delicious smells among the tombstones, but that\'s not all. Your cunning ears detect tiny heartbeats scurrying about. Quick! Catch some mice!' '\n'
		print 'To play this game, you can type \'grab\' or \'ignore\' in order to grab mice or ignore distractions like balls of lint.' '\n'
		answer_one_a_action1 = raw_input ('**scratch scratch** Is that a mouse? **scurry scurry** IT\'S A MOUSE! GRAB IT!').lower()
			if answer_one_a_action1 == 'grab':
				print 'Great job! You caught the mouse!'
			else:
				print 'Whelp, there\'s always next time.'
		answer_one_a_action2		 	
	#take it this direction
	# elif answer_one_a == 'b':
	# #take it this direction
	# elif answer_one_a == 'c':
	# #take it this direction
	# else:
	# 	print 'Whoops! That\'s not an option. Please choose A, B, or C.'
	# 	#restart the game at answer_one_a raw_input
# elif answer_one == "b":
# 	#take it this other direction
# elif answer_one == "c":
# 	#take it this other direction
# else:
# 	print 'Nope! That\'s not an option. Please choose A, B, or C.'
# 	#restart the game at answer_one raw_input