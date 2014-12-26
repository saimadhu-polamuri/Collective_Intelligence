from recommendations_data import critics
from math import sqrt
def similarity_distance(data,person_1,person_2):

	# Get list of shared items
	si = {}
	for item in data[person_1]:
		if item in data[person_2]:
			si[item] = 1
	if len(si) == 0 : return 0
	
	#Add up the squares of all the differences		
	sum_of_squares = sum([pow(data[person_1][item] - data[person_2][item],2) for item in data[person_1] if item in data[person_2]])
	return 1/(1+sum_of_squares)
print similarity_distance(critics,'Lisa Rose','Gene Seymour')