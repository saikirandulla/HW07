# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3,5,6]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

##############################################################################


def nested_sum(list_num):
	sum = 0
	for item in range (len(list_num)):
		if (type(list_num[item]) == list):
			sum = sum + nested_sum(list_num[item])
		else:
			sum = sum + list_num[item]
	return sum

def main():
	pass
	
if __name__ == '__main__':
    main()