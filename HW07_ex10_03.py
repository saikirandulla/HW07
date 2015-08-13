# I want to be able to call cumulative_sum from main w/ various lists and 
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def cumulative_sum(list_num):
	list_csum = []
	for item in range(len(list_num)):
		if item > 0:
			x = (list_num[item] + list_csum[item-1])
			list_csum.append(x)
		else:
			list_csum.append(list_num[item])
	return list_csum

def main():
	pass
	
if __name__ == '__main__':
    main()