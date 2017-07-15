
from statistics import mean




#2- Sum of all arguments 


list = []

def mysum(*num1):
	for i in num1:
		list.append(i)
	return(sum(list))		
		

#3 - race timing 


def ave_mile():
	
	Monday = float(input("Please enter mile time: "))
	Tuesday = float(input("Please enter mile time "))
	Wednesday = float(input("Please enter mile time: "))
	Thursday = float(input("Please enter mile time "))
	Friday = float(input("Please enter mile time: "))
	Saturday = float(input("Please enter mile time "))
	Sunday = float(input("Please enter mile time "))

	average = (Monday + Tuesday + Wednesday + Thursday + Friday + Saturday + Sunday)/7
	average = round(average, 2)
	


#4 - Hexadecimal output


#5 - Pig Latin

def piglatin():
	word = input("Please enter a word: ")
	if word[0] == "a":
		print(word + "way")
	elif word[0] == "e":
		print(word + "way")
	elif word[0] == "i":
		print(word + "way")
	elif word[0] == "o":
		print(word + "way")
	elif word[0] == "u":
		print(word + "way")
	else:
		print(word[1::] + word[0] + "way")



# Pig Latin sentence

def piglatinsent():
	sentence = input("Please enter a sentence: ")
	out = []
	for i in sentence.split():
		if i[0] in "aeiou":
			out.append(i + "way")
		else:
			out.append(i[1:] + i[0] + "ay")

	print(" ".join(out))


# Ubbi Dubbi 

def ubbidubbi():
	word = input("Please enter a word: ")
	output = []
	for i in word:
		if i in "aeiou":
			output.append("ub" + i)
		else:
			output.append(i)
	print("".join(output))


# First and last of a string

def firstlast():
	string1 = input("Please enter a string: ")
	string2 = string1[0]
	string3 = string2[0]+string1[-1]
	print(string3)






# Sorting a string

def strsort():
	strings = input("Please enter a sentence: ")
	new = strings.split(" ")
	new.sort()
	print(new)


#mysum2 

list1 = []

def mysum2(*args):
	if args == int:
		print(args)










	
	

		












	 





