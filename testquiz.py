"""
Behavior: These variables will be questions and answers. 
Inputs: Questions and answers
Outputs: None
"""
easy_text = """
elephants have tails (yes/no)  __1__
crows have 3 eyes (true/false) __2__ 
result of this (21/7)+2        __3__
capital of turkey?	       __4__
"""

easy_answers = ["yes","false","5","ankara"]

medium_text = """
result of this 21/(3+2*2)     __1__
result of this (21/7)+2*2     __2__
one meter equals to __3__ cantimeter
one liter equals to __4__ mililiter
""" 

medium_answers = ["3","7","100","1000"]

hard_text = """ 
how many cats do i have? __1__ 
how many dogs do i have? __2__ 
where will i live soon   __3__
name of my black cat?    __4__
"""

hard_answers = ["4","0","urla","karam"]

blank = ["__1__","__2__","__3__","__4__"]
line = "-" * 38


"""
Behavior: User asked to select level difficulty. With the choice question and answer set will assigned. 
Inputs: User choice. 
Outputs: Question and answer set. 
"""
def choose_level():
	level = ""
	print "choose level: easy / medium / hard"
	levels = ["easy", "medium", "hard"]
	while level not in levels:
		level = raw_input("Choose a level: ")
		if level == "easy":
			return easy_text, easy_answers
		elif level == "medium":
			return medium_text, medium_answers
		elif level == "hard":
			return hard_text, hard_answers
		else:
			print "Choose an option from list!!!"

"""
Behavior: Defination will get players trials 
Inputs: Player trial
Outputs: Score
"""
def trial(score):
	trial = raw_input("    ===> Answer for " + score + "  :  ")
	return trial

"""
Behavior: This defination check the user trial with real answer via asinged answers and questions. End of the round asks for new game. 
Inputs: Question, answer set, user trial, again choice.  
Outputs: Counter, correct answers or wrong massage, answers, play again or end.  
"""
def game():
	score = 0
	counter = 0
	question, answer = choose_level()
	while score < len(blank):
		counter = counter + 1
		print question
		user_trial = trial(blank[score])
		if user_trial == answer[score]:
			print "Correct!"
			question = question.replace(blank[score], user_trial)
			score = score + 1
		else:
			print "You are wrong, try again."
	print line + "\nALL ANSWERS ARE TRUE!\n" + question + "\nYOU HAVE DONE",counter,"TRIAL!\n" + line  #thanks for the tip. now all my prints are in a single line
	ask_again = raw_input ("Enter 'y' start again or anything else to quit: ")
	if ask_again == "y":
		game()
	
game()