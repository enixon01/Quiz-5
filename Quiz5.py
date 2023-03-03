#Emily Nixon
#Problem 1
pres = int(input("What is your tire pressure?\n"))
def tire_pressure(pres):
    if pres < 28:
        print("Tire pressure is low.")
    else:
        print("None")
tire_pressure(pres)

#Problem 2
temp = int(input("What is the temperature?\n"))
def thermostat(temp):
    if temp <= 52:
        print("The heater is on.")
    elif 52<temp<71:
        print("Heater and AC are off.")
    elif temp >= 71:
        print("The AC is on.")
thermostat(temp)

#Problem 3
def fruit_function(fruit):
    if fruit == "banana":
        print("Banana it is!")
    if fruit == "cherry":
        print("I cherish you!")
    if fruit == "apple":
        print("I applesolutely like you!")
    if fruit =="orange":
        print("Orange you glad to see me?")
    if fruit == "melon":
        print("You are one in a Melon.")


fruit_function("banana")
fruit_function("cherry")
fruit_function("apple")
fruit_function("orange")
fruit_function("melon")
