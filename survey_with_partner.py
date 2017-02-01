from time import sleep

tally = 0
tally2 = 0

print " "
print "Welcome to the survey!"
print " "

typer = raw_input("Who is typing right now? ")
print " "
sleep(1)

print "Hi " + typer + "!"
print " "
sleep(1)

friend = raw_input("So, who is sitting next to you, " + typer + "? ")
print " "
sleep(1)

print "Hi " + friend + ", welcome to the party!"
print " "
sleep(1)

print "Alright, " + typer + " and " + friend + ", " + "the following questions will determine a super duper important choice you'd make in an alternate reality. If you want to know what this super duper important choice is, let's continue!"
print " "
sleep(5)


typer_color = raw_input(typer + ", if you had to choose between the colors red-orange or orange-red, which would you choose? ").lower()

if typer_color == "red-orange":
	tally += 1
	print "Hmmm... very interesting. Let's continue."
	print " "
	sleep(1)
elif typer_color == "orange-red":
	tally += 0
	print "Hmmm... very interesting. Let's continue."
	print " "
	sleep(1)
else:
	print "Sorry, that's not a valid answer. Stop messing up the survey!"
print " "
sleep(1)


friend_color = raw_input("Cool! Now, it's " + friend + "'s turn. Red-orange or orange-red, " + friend + "? ").lower()

if friend_color == "red-orange":
	tally2 += 1
	print "Aha! I had a feeling that's what you'd say."
	print " "
	sleep(1)
elif friend_color == "orange-red":
	tally2 += 0
	print "Aha! I had a feeling that's what you'd say."
	print " "
	sleep(1)
else:
	print "That's not one of the choices I gave you. Stop messing up the survey!"
print " "
sleep(1)	



typer_animal = raw_input("What about tigers or bears? What do you think, " + typer + "? ").lower()

if typer_animal == "tigers":
	tally += 1
	print "Oh, really?! Facinating!"
	print " "
	sleep(1)
elif typer_animal == "bears":
	tally += 0
	print "Oh, really?! Facinating!"
	print " "
	sleep(1)
else:
	print "That's not one of the choices. Seriously! Play by the rules."
print " "
sleep(1)


friend_animal = raw_input(friend + ", what do you think -- bears or tigers? ").lower()

if friend_animal == "tigers":
	tally2 += 1
	print "Oh my! So, ferocious!"
	print " "
	sleep(1)
elif friend_animal == "bears":
	tally2 += 0
	print "Oh my! So, ferocious!"
	print " "
	sleep(1)
else:
	print "C'mon! That's not a choice! Follow the rules."
print " "
sleep(1)



typer_weather = raw_input("So, " + typer + " do you prefer winter or summer? ").lower()

if typer_weather == "winter":
	tally += 1
	print "Great job! The results will be calculated after " + friend + "'s turn."
	print " "
	sleep(1)
elif typer_weather == "summer":
	tally += 0
	print "Great job! The results will be calculated after " + friend + "'s turn."
	print " "
	sleep(1)
else:
	print "Don't mess with the game or it won't be pretty."
print " "
sleep(1)


friend_weather = raw_input("And you, " + friend + "? What's your favorite? Winter or summer? ").lower()

if friend_weather == "winter":
	tally2 += 1
	print "Nicely done! Gonna do some calculations here... boop beep boop..."
	print " "
	sleep(1)
elif friend_weather == "summer":
	tally2 += 0
	print "Nicely done! Gonna do some calculations here... boop beep boop..."
	print " "
	sleep(1)
else:
	print "Seriously, don't mess with the game."
print " "
sleep(1)



if tally <= 1:
	print typer + "! In an alternate reality, you would prefer a donut over a cupcake! I bet you're suprised!"
else:
	print typer + "! In an alternate reality, you would prefer a cupcake over a donut! I bet you're suprised!"
print " "
sleep(3)


if tally2 <= 1:
	print friend + "! In an alternate reality, you would choose a delicious donut over a cupcake! I bet you're NOT suprised!"
else:
	print friend + "! In an alternate reality, you would choose a delicious cupcake over a donut! I bet you're NOT suprised!" 	
print " "
sleep(2)

print "That concludes the survey! Thanks for playiing!"
print " "
print " "		
