
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z", " "]
#space = '_'

#something = 'Zntargvp sebz bhgfvqr arne pbeare'
something = input("enter any msg to encrpt : ")

something_list = list(something)

table = " "


for i, letter in enumerate (something_list):

	if letter == " ":
		new_number = 26

	else:
		number = alpha.index(letter.upper())
		if number < 13:
			new_number = number + 13
		else:
			new_number = number - 13

	table += alpha[new_number]

print(table)
