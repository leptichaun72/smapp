largest = None
smallest = None
num = None

while True:
    inp = input("Enter a number: ")
    if inp == "done" : 
        break
    try:
        num=float(inp)
    except:
        print ("Invalid input")
        continue

    if largest is None:
        largest = num
        smallest = num

    if num>largest: 
        largest=num
    if num<smallest: 
        smallest=num

print ("Maximum is ", largest)
print ("Minimum is ", smallest)

