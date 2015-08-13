# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(list_1):
	list_2 = list_1[:]
	list_2.sort()
	sorted_list = sort(list_2)
	if list_1 == sorted_list:
		return True
	else:
		return False
	
def sort(list_1):
	for item in range (len(list_1)):
		if (type(list_1[item]) == list):
			is_sorted(list_1[item])
	return list_1

def main():
	pass
	
if __name__ == '__main__':
    main()