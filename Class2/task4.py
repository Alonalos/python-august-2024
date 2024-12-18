tip = int(input("Enter tip amount: "))

if tip == 15:
    print("Standard")
elif tip == 18:
    print("Good")
elif tip == 20:
    print("Great")
elif tip > 20:
    print("My hero")
else:
    print("Provide right tip")