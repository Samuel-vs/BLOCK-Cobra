x = int(input("What's your weight? "))
conv = input("Convert to: Kg(K) or Lbs(L)? ")

if conv == "K" or conv == "k":
    c = x/2.20462
    print(f"Your weight is {c}Kg!!!")
elif conv == "L" or conv == "l":
    m = x * 2.20462
    print(f"Your weight is {m}Lbs!!!")
else:
    print("An unexpected error occured!!!")