char = input ("Enter two space-seperated characters: ")
ch1, ch2 = char.split()
max_char =  max (ch1, ch2)

print ("-------------------------")
print (f"The character with greater value is: {max_char}")
print ("-------------------------")
print ("This part is optional to include \n Showing ASCII Values")

print (f"{ch1} : {ord(ch1)}")
print (f"{ch2} : {ord(ch2)}")
