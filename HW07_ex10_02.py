# I want to be able to call capitalize_nested from main w/ various lists 
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(list_string):
	list_string2 = []
	for item in range (len(list_string)):
		if (type(list_string[item]) == list):
			list_string2.append(capitalize_nested(list_string[item]))
		elif (type(list_string[item]) == int or float):
			list_string2.append(list_string[item])
		else:
			list_string2.append(list_string[item].capitalize())
	return list_string2

def main():
	pass
	
if __name__ == '__main__':
    main()