print" "
print" "
print " /$$   /$$ /$$                       /$$     /$$             /$$       /$$  /$$$$$$"         
print "| $$$ | $$|__/                      | $$    | $$            | $$      |__/ /$$__  $$"        
print "| $$$$| $$ /$$ /$$$$$$$   /$$$$$$  /$$$$$$  | $$$$$$$       | $$       /$$| $$  \__//$$$$$$" 
print "| $$ $$ $$| $$| $$__  $$ /$$__  $$|_  $$_/  | $$__  $$      | $$      | $$| $$$$   /$$__  $$"
print "| $$  $$$$| $$| $$  \ $$| $$$$$$$$  | $$    | $$  \ $$      | $$      | $$| $$_/  | $$$$$$$$"
print "| $$\  $$$| $$| $$  | $$| $$_____/  | $$ /$$| $$  | $$      | $$      | $$| $$    | $$_____/"
print "| $$ \  $$| $$| $$  | $$|  $$$$$$$  |  $$$$/| $$  | $$      | $$$$$$$$| $$| $$    |  $$$$$$$"
print "|__/  \__/|__/|__/  |__/ \_______/   \___/  |__/  |__/      |________/|__/|__/     \_______/"
print" "                                                                                            
print" "
print" "
print "			             *     ,MMM8&&&.            *"
print "			                  MMMM88&&&&&    ."
print "			                 MMMM88&&&&&&&"
print "			     *           MMM88&&&&&&&&"
print "			                 MMM88&&&&&&&&"
print "			                 'MMM88&&&&&&'"
print "			                   'MMM8&&&'      *"
print "			          |\___/|"
print "			          )     (             .              "
print "			         =\     /="
print "			           )===(       *"
print "			          /     \\"
print "			          |     |"
print "			         /       \\"
print "			         \       /"
print "			  _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_"
print "			  |  |  |  |( (  |  |  |  |  |  |  |  |  |  |"
print "			  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |"
print "			  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |"
print "			  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |"
print " "


from time import sleep

def menu_choice():

    print '\n    0 - Main Menu'
    print '    1 - Play game.'
    print '    2 - Show high scores.'
    print '    3 - Exits the program.\n'

    choice = int(raw_input('Meow! Please choose from the menu options: '))

    return choice

def main():

	while True:
		choice = menu_choice()

		if choice == 0:
			continue  #continue goes to the next loop iteration

		elif choice == 1:
			print ' '
			print 'Hello! Welcome to the game Nineth Life.\n'
			print 'We are pleased to tell you that a long time ago, in a reality far far away, you were A CAT.\n'
			print 'A great furry admiral who commanded legions. You prowled the night with your best friend, Colonel Meow, and together you plotted the demise of humans. "Take cover," those furless creatures shouted. "Here comes the mighty..."\n'
			sleep(1)

			player1 = raw_input ('Wait, remind us, what was your fur-name? ')
			print ' '
			sleep(1)

			print '"Take cover," those furless creatures shouted. "Here comes the mighty %s!"' % (player1)
			print ' '
			sleep(3)

			print 'The night welcomes you, %s. You are about to begin your evening patrol. What would you like to do first? ' % (player1)
			print ' '
			print 'a) Find a snack\n' 'b) Explore the neighbor\'s yard\n' 'c) Take a nap\n' 'd) Exit game\n'
			answer_one = raw_input ('What strikes your fancy? a, b, or c? ').lower()
			print ' '
			sleep(1)

			if answer_one == 'a':
				print 'You chose a) Find a snack!\n'
				sleep(1)
				print 'Mmm... a delightful scent floats through the air. Smells like Defenseless Prey! Which way does your nose point?\n'
				print 'a) Left towards the graveyard\n' 'b) Right towards the forest\n' 'c) Forward towards the town gas station\n' 'd) Exit game\n'
				answer_one_a = raw_input ('What\'ll it be? a, b, c, or d? ').lower()
				print ' '

				if answer_one_a == 'a':
					print 'You chose a) Left towards the graveyard!\n'
					sleep(1)
					print'Mmm... so many delicious smells among the tombstones, but that\'s not all. Your cunning ears detect tiny heartbeats scurrying about. Quick! Catch some mice!\n'
					print 'To play this game, you can type \'grab\' or \'ignore\' in order to grab mice or ignore distractions like balls of lint.\n'
					
					answer_one_a_action_a1 = raw_input ('**scratch scratch** Is that a mouse? **scurry scurry** IT\'S A MOUSE! GRAB IT! ').lower()
					if answer_one_a_action_a1 == 'grab':
						print '\nGreat job! You caught the mouse!\n'
						sleep(1)
					else:
						print '\nWhelp, there\'s always next time.\n'
						sleep(1)
					
					answer_one_a_action_a2 = raw_input ('Oh! What\'s that over there? It\'s just a ball of lint. Ignore it. ').lower()
					if answer_one_a_action_a2 == 'ignore':
						print '\nNice. Good thing we didn\'t get distracted.\n'
						sleep(1)
					else:
						print '\nLint GLORIOUS LINT! How could I possibly ignore such fun?!\n'
						sleep(1)

					answer_one_a_action_a3 = raw_input ('**squeak squeak** MOUSE!!! ').lower()
					if answer_one_a_action_a3 == 'grab':
						print '\nCongratulations, %s! You\'ve successfully caught mice today. You\'re a superior kitty! Time to go home and take a well deserved nap.\n' % (player1) 	
						sleep(1)
					else:
						print '\nMeh. You tried your best, %s. Tomorrow you\'ll catch more mice. Today, it\'s time to go home and take a nap.\n' % (player1) 	

				elif answer_one_a == 'b':
					print 'You chose b) Right towards the forest!\n'
					sleep(1)
					print'The crunch of leaves beneath your paws fills you with confidence. You are a true hunter. Unless of course, there\'s a coyote around. Which there is. Quick! Run away from the coyote!\n'
					print 'To play this game, you can type \'run\' or \'jump\' in order to run away or jump onto fallen logs.\n'
					
					answer_one_a_action_b1 = raw_input ('**hooowwwl** Oh no! A coyote is right behind you! Run away!! ').lower()
					if answer_one_a_action_b1 == 'run':
						print '\nGreat job! You\'re way ahead of the coyote!\n'
						sleep(1)		
					else:
						print '\nWhelp, you didn\'t run. The coyote nipped at you but you managed to side step. Escape while you can!\n'
						sleep(1)

					answer_one_a_action_b2 = raw_input ('**pant pant pant*** This is a workout! Stay one step ahead of the coyote by jumping on logs. ').lower()
					if answer_one_a_action_b2 == 'jump':
						print '\nNice! Good thing we didn\'t get caught in the coyote\'s jaws.\n'
						sleep(1)
					else:
						print '\nAHHH! You didn\'t jump! The coyote nipped your tail!\n'
						sleep(1)

					answer_one_a_action_b3 = raw_input ('Do you hear the coyote anymore? Hmmm... just to be safe, jump onto the branches of this tree and look around. ').lower()
					if answer_one_a_action_b3 == 'jump':
						print '\nCongratulations, %s! You\'ve successfully escaped the coyote today. You\'re a superior kitty! Time to go home and take a well deserved nap.\n' % (player1) 	
						sleep(1)	
					else:
						print '\nMeh. You tried your best, %s. You\'re missing part of your tail, but consider it a badge of honor. Tomorrow you\'ll show that coyote your true prowess. Today, it\'s time to go home, lick your wounds and take a nap.\n' % (player1) 	

				elif answer_one_a == 'c':
					print 'You chose c) Forward towards the gas station!\n'
					sleep(1)
					print'Glistening greasy hot dogs sit unattended inside the gast station trash cans. Quick! Get to the delicious hot dogs by jumping on the roofs of refueling cars!\n'
					print 'To play this game, you can type \'run\' or \'jump\' in order to run towards the hot dogs or jump onto the refueling cars.\n'
					
					answer_one_a_action_c1 = raw_input ('**beep beep** There\'s a car pulling up behind you! Run away! ').lower()
					if answer_one_a_action_c1 == 'run':
						print '\nGreat job! You\'re way ahead of the car and much closer to the hot dogs!\n'
						sleep(1)		
					else:
						print '\nWhelp, you didn\'t run. The car almost ran you over but you managed to side step. Escape while you can!\n'
						sleep(1)

					answer_one_a_action_c2 = raw_input ('Hmmm... the quickest way to the tasty hot dogs is to jump on these cars. Jump! ').lower()
					if answer_one_a_action_c2 == 'jump':
						print '\nNice! You\'re so spry and graceful.\n'
						sleep(1)
					else:
						print '\nAHHH! You didn\'t jump! If you\'re not careful you\'re gonna be roadkill!\n'
						sleep(1)

					answer_one_a_action_c3 = raw_input ('**sniff sniff** Those hot dogs are so close! Jump into the trash can. ').lower()
					if answer_one_a_action_c3 == 'jump':
						print '\nCongratulations, %s! You\'ve successfully fit all the hot dogs into your furry belly. You\'re a superior kitty! Time to go home and take a well deserved nap.\n' % (player1) 	
						sleep(1)	
					else:
						print '\nMeh. You tried your best, %s. You didn\'t get the tasty hot dogs, but maybe you will tomorrow. Today, it\'s time to go home and take a nap.\n' % (player1) 	
				
				elif answer_one_a == 'd':
					break
				
				else:
					print 'Whoops! That\'s not an option. Please choose A, B, or C.'
				# 	#restart the game at answer_one_a raw_input. Wrap the game in a function? Or create a menu function. 

			elif answer_one == "b":
				print 'You chose b) Explore the neighbor\'s yard!\n'
				sleep(1)
				print 'Ah yes. The neighbor\'s yard. A forbidden place. Many have entered, few have escaped. **CRASH** What was that? Your feline senses tell you it is...\n'
				print 'a) A family of rats\n' 'b) The neighbor\'s dogs\n' 'c) An automatic sprinkler system\n' 'd) Exit game\n'
				answer_one_b = raw_input ('What\'ll it be? a, b, c, or d? ').lower()
				print ' '

				if answer_one_b == 'a':
					print 'You chose a) A family of rats!\n'
					sleep(1)
					print'Your mouth waters and your sharp nails glisten in the moonlight. Time to grab some dinner. Quick! Catch those rats!\n'
					print 'To play this game, you can type \'grab\' or \'ignore\' in order to grab rats or ignore distractions like floating specks of dust.\n'
					
					answer_one_b_action_a1 = raw_input ('**scratch scratch** Is that a rat? **scurry scurry** IT\'S A RAT! GRAB IT! ').lower()
					if answer_one_b_action_a1 == 'grab':
						print '\nGreat job! You caught the rat!\n'
						sleep(1)
					else:
						print '\nWhelp, there\'s always next time.\n'
						sleep(1)
					
					answer_one_b_action_a2 = raw_input ('Oh! What\'s that over there? It\'s just a floating speck of dust. Ignore it. ').lower()
					if answer_one_b_action_a2 == 'ignore':
						print '\nNice. Good thing we didn\'t get distracted.\n'
						sleep(1)
					else:
						print '\nFloating dust GLORIOUS DUST! How could I possibly ignore such fun?!\n'
						sleep(1)

					answer_one_b_action_a3 = raw_input ('**squeak squeak** RAT!!! ').lower()
					if answer_one_b_action_a3 == 'grab':
						print '\nCongratulations, %s! You\'ve successfully caught rats today. You\'re a superior kitty! Time to go home and take a well deserved nap.\n' % (player1) 	
						sleep(1)
					else:
						print '\nMeh. You tried your best, %s. Tomorrow you\'ll catch more rats. Today, it\'s time to go home and take a nap.\n' % (player1) 	

				elif answer_one_b == 'b':
					print 'You chose b) The neighbor\'s dogs!\n'
					sleep(1)
					print'Your old foes think they have you cornered. Silly slobbery fools! They\'re no match for your graceful agility. Quick! Evade the dogs by staying one pounce ahead!\n'
					print 'To play this game, you can type \'run\' or \'jump\' in order to run on a path or jump onto lawn furniture.\n'
					
					answer_one_b_action_b1 = raw_input ('**woof woof** There\'s a dog right behind you! Run away! ').lower()
					if answer_one_b_action_b1 == 'run':
						print '\nGreat job! You\'re way ahead of the dog. Keep going!\n'
						sleep(1)		
					else:
						print '\nWhelp, you didn\'t run. The dog almost ate you but you managed to side step. Escape while you can!\n'
						sleep(1)

					answer_one_b_action_b2 = raw_input ('Hmmm... the quickest way back home is to jump on this picnic table. Jump! ').lower()
					if answer_one_b_action_b2 == 'jump':
						print '\nNice! You\'re so spry and graceful.\n'
						sleep(1)
					else:
						print '\nAHHH! You didn\'t jump! If you\'re not careful you\'re gonna be dog food!\n'
						sleep(1)

					answer_one_b_action_b3 = raw_input ('**sniff sniff** Those dogs are so close! Jump over the fence and back into your own yard. ').lower()
					if answer_one_b_action_b3 == 'jump':
						print '\nCongratulations, %s! You\'ve successfully evaded those doggies. You\'re a superior kitty! Time to go home and take a well deserved nap.\n' % (player1) 	
						sleep(1)	
					else:
						print '\nMeh. You tried your best, %s. One of the dogs nipped your tail. Tomorrow, you\'ll return with vengeance. Today, it\'s time to go home, lick your wounds and take a nap.\n' % (player1) 	
				
				elif answer_one_b == 'c':
					print 'You chose c) An automatic sprinkler system!\n'
					sleep(1)
					print'You refuse to let falling water foil your night. It\'s beneath you. Literarlly. Jump on the tops of backyard furniture to avoid the sprinklers!\n'
					print 'To play this game, you can type \'run\' or \'jump\' in order to run on a path or jump onto lawn furniture.\n'
					
					answer_one_b_action_c1 = raw_input ('**swish swish** There\'s a sprinkler right behind you! Run away! ').lower()
					if answer_one_b_action_c1 == 'run':
						print '\nGreat job! You\'re way ahead of the sprinkler. Keep going!\n'
						sleep(1)		
					else:
						print '\nWhelp, you didn\'t run. The sprinkler almost got you but you managed to side step. Escape while you can!\n'
						sleep(1)

					answer_one_b_action_c2 = raw_input ('Hmmm... the quickest way back home is to jump on this picnic table. Jump! ').lower()
					if answer_one_b_action_c2 == 'jump':
						print '\nNice! You\'re so spry and graceful.\n'
						sleep(1)
					else:
						print '\nAHHH! You didn\'t jump! If you\'re not careful you\'re gonna be drenched!\n'
						sleep(1)

					answer_one_b_action_c3 = raw_input ('**sprinkle sprinkle** Those sprinklers are so close! Jump over the fence and back into your own yard. ').lower()
					if answer_one_b_action_c3 == 'jump':
						print '\nCongratulations, %s! You\'ve successfully evaded those demon sprinklers. You\'re a superior kitty! Time to go home and take a well deserved nap.\n' % (player1) 	
						sleep(1)	
					else:
						print '\nMeh. You tried your best, %s. One of the sprinklers got you all wet. Tomorrow, you\'ll return with vengeance. Today, it\'s time to go home, dry your fur and take a nap.\n' % (player1) 	
				
				elif answer_one_b == 'd':
					break

				#else:
					#print 'Whoops! That\'s not an option. Please choose A, B, or C.'

			elif answer_one == "c":
				print 'You chose c) Take a nap!\n'
				sleep(1)
				print 'Home sweet home. Look there, it\'s your favorite comfy pile of towels -- fresh from the dryer. As you stroll leisurely towards the clean folded laundry, something catches the corner of your bright eye. Heavens no! It\'s a...\n'
				print 'a) Red laser beam darting about the floor\n' 'b) Vacuum cleaner roaring to life\n' 'c) Freshly mopped floor, still covered in a layer of water\n' 'd) Exit game\n'
				answer_one_c = raw_input ('What\'ll it be? a, b, c, or d? ').lower()
				print ' '

				if answer_one_c == 'a':
					print 'You chose a) Red laser beam darting about the floor!\n'
					sleep(1)
					print'AHHH! Pesky red laser! How did you get back in the house? It matters not. Prepare to die!\n' 'Quick! Catch the red laser dot.\n'
					print 'To play this game, you can type \'grab\' or \'ignore\' in order to grab the red light or ignore distractions like the desire to lick yourself to sleep.\n'
					
					answer_one_c_action_a1 = raw_input ('**glimmer glimmer** Is that the red laser light? **flash flash** IT\'S THE MOVING RED DOT! GRAB IT! ').lower()
					if answer_one_c_action_a1 == 'grab':
						print '\nGreat job! You caught the red dot!\n'
						sleep(1)
					else:
						print '\nWhelp, there\'s always next time.\n'
						sleep(1)
					
					answer_one_c_action_a2 = raw_input ('Oh! What\'s that funny feeling? It\'s just your feline instinct telling you to lick yourself all over. Ignore it. ').lower()
					if answer_one_c_action_a2 == 'ignore':
						print '\nNice. Good thing we didn\'t get distracted.\n'
						sleep(1)
					else:
						print '\nMmmm... Not gonna ignore your innate desire. **Lick lick lick** Zzzzzz...\n'
						sleep(1)

					answer_one_c_action_a3 = raw_input ('**Flicker flicker** The red dot LIVES!!! ').lower()
					if answer_one_c_action_a3 == 'grab':
						print '\nCongratulations, %s! You\'ve successfully caught the red dot today. You\'re a superior kitty! Time to take a well deserved nap.\n' % (player1) 	
						sleep(1)
					else:
						print '\nMeh. You tried your best, %s. Tomorrow you\'ll catch the pesky red laser dot. Today, it\'s time to take a nap.\n' % (player1) 	

				elif answer_one_c == 'b':
					print 'You chose b) Vacuum cleaner roaring to life!\n'
					sleep(1)
					print'AHHH! The vacuum has woken from its dusty slumber. Don\'t let it EAT YOU!\n' 'Quick! Run away!\n'
					print 'To play this game, you can type \'run\' or \'jump\' in order to run on a path or jump onto household furniture.\n'
					
					answer_one_c_action_b1 = raw_input ('**ROAR ROAR** The vacuum cleaner is right behind you! Run away! ').lower()
					if answer_one_c_action_b1 == 'run':
						print '\nGreat job! You\'re way ahead of the vacuum. Keep going!\n'
						sleep(1)		
					else:
						print '\nWhelp, you didn\'t run. The vacuum almost got you but you managed to side step. Escape while you can!\n'
						sleep(1)

					answer_one_c_action_b2 = raw_input ('Hmmm... the quickest way to safety is to jump on the kitchen counter. Jump! ').lower()
					if answer_one_c_action_b2 == 'jump':
						print '\nNice! You\'re so spry and graceful.\n'
						sleep(1)
					else:
						print '\nAHHH! You didn\'t jump! If you\'re not careful you\'re gonna be eaten by the vacuum cleaner!\n'
						sleep(1)

					answer_one_c_action_b3 = raw_input ('**VROOOM VROOOM** The vacuum cleaner is so close! Jump onto the couch! ').lower()
					if answer_one_c_action_b3 == 'jump':
						print '\nCongratulations, %s! You\'ve successfully evaded that demon vacuum cleaner. You\'re a superior kitty! Time to take a well deserved nap.\n' % (player1) 	
						sleep(1)	
					else:
						print '\nMeh. You tried your best, %s. The vacuum sucked up part of your tail but you pulled away just in time. Tomorrow, you\'ll return with vengeance. Today, it\'s time to take a nap.\n' % (player1) 	
				
				elif answer_one_c == 'c':
					print 'You chose c) Freshly mopped floor, still covered in a layer of water!\n'
					sleep(1)
					print'Silly humans washing floors. Don\'t they know you put your butt on EVERYTHING? Whatever. Avoid the wet floor and jump on the fancy furniture.\n'
					print 'To play this game, you can type \'run\' or \'jump\' in order to run on a path or jump onto household furniture.\n'
					
					answer_one_c_action_c1 = raw_input ('**splash splash** There\'s a giant puddle right behind you! Run away! ').lower()
					if answer_one_c_action_c1 == 'run':
						print '\nGreat job! You\'re far way from the puddle. Time to find a place to nap!\n'
						sleep(1)		
					else:
						print '\nWhelp, you didn\'t run away. The puddle almost got you wet but you managed to side step. Escape while you can!\n'
						sleep(1)

					answer_one_c_action_c2 = raw_input ('Hmmm... the quickest way to safety is to jump on the kitchen counter. Jump! ').lower()
					if answer_one_c_action_c2 == 'jump':
						print '\nNice! You\'re so spry and graceful.\n'
						sleep(1)
					else:
						print '\nAHHH! You didn\'t jump! If you\'re not careful you\'re gonna get your paws wet!\n'
						sleep(1)

					answer_one_c_action_c3 = raw_input ('**splash splash** The floor is super wet here! Jump onto the couch! ').lower()
					if answer_one_c_action_c3 == 'jump':
						print '\nCongratulations, %s! You\'ve successfully evaded that wet floor. You\'re a superior kitty! Time to take a well deserved nap.\n' % (player1) 	
						sleep(1)	
					else:
						print '\nMeh. You tried your best, %s. The wet floor got your paws wet. Tomorrow, you\'ll return with vengeance. Today, it\'s time to dry your fur and take a nap.\n' % (player1) 	

				elif answer_one_c == 'd':
					break

			elif answer_one == 'd':
				break	

			#else:
			#print 'Nope! That\'s not an option. Please choose A, B, C, or D.'
			# 	#restart the game at answer_one raw_input

		#elif choice == 2:
			#show high scores using input/output readlines

		elif choice == 3: 		
			break

if __name__ == '__main__':
    main()