myTuple = (5, 2, 7, 9, 1, 4)
print("The element of the tuple are " + str(myTuple))
ele = 9
print("The search element is " + str(ele))
isPresent = False
for val in myTuple :
	if ele == val :
		isPresent = True
		break
if isPresent :
    print("The element is present in the tuple")
else :
    print("The element is not present in the tuple")
