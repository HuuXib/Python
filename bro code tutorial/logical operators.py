

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("the tamperature is good today ")
    print("go outside")
elif not temp <0 or temp > 30:
    print("the temperature is bad today ")
    print("stay inside")