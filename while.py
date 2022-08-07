#s = secret no 
s = 5
i = 0
limit = 3

while i < limit:
    g = int(input("Guess the number: "))
    i += 1
    if g == s:
        print("You win!!!")
        break
    else:
        print("Guess again.")
else:
    print("Sorry, please try again.")