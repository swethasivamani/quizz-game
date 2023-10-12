print("Welcome to quizz world")

player=input("Do you want to play ?")

if player.lower()  != "yes":
    quit()
print("ok lets play!")
score=0

question=input("How many day do we have in a week ?")
if question.lower() == "seven":
    print("Super, its correct")
    score +=1
else:
    print("So sad, its incorrect")

question=input("In which direction does the sun rise ?")
if question.lower()  == "east":
    print("Super, its correct")
    score +=1
else:
    print("So sad, its incorrect")

question=input("In which direction does the sun set ?")
if question.lower()  == "west":
    print("Super, its correct")
    score +=1
else:
    print("So sad, its incorrect")

question=input("Which is our national bird ?")
if question.lower()  == "peacock":
    print("Super, its correct")
    score +=1
else:
    print("So sad, its incorrect")

question=input("Which is the fastest animal on the land ?")
if question.lower()  == "cheetah":
    print("Super, its correct")
    score +=1
else:
    print("So sad, its incorrect")

question=input("Which is the largest ocean in the world ?")
if question.lower()  == "pacific ocean":
    print("Super, its correct")
    score +=1
else:
    print("So sad, its incorrect")

print("your score"+ str(score))



