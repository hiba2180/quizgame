print("HELLO USER")
print("welcome to my quiz world!")

playing = input("do you want to play? ")
print(playing)
if playing.lower()!="yes":
    quit()
else: print("yohoo!!, lets play ;))")
score = 0
answer = input("who is the father of economics? ")
if answer.lower() == "adam smith":
    print("correct")
    score+=1
else:
    print("incorrect")

answer = input("The process of curing inflation by reducing the money supply is called? ")
if answer.lower() == "disinflation":
    print("correct")
    score+=1
else:
    print("incorrect")

answer = input("Price theory is also known as? ")
if answer.lower() == "microeconomics":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("who is the founder of macroeconomics? ")
if answer.lower() == "john maynard keynes":
    print("correct")
    score += 1
else:
    print("incorrect")

print("you got " + str(score) + " questions correct!" )
print("you got " + (str((score/4) * 100)) + "%" )



