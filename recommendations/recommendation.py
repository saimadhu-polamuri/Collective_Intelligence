from recommendations_data import critics
from math import sqrt

class Recommendation():
	""" Recommendation for movie data """
	
	def __init__(self,dataset_name):
	
	 	""" constructed Function for Recommendation class """
	
		self.dataset_name = dataset_name

	def similarity_distance(self,person_1,person_2):

		""" Function for finding distance between two persons """

		self.person_1 = person_1
		self.person_2 = person_2

			# Get list of shared items
		si = {}
		for item in self.dataset_name[self.person_1]:
			#print item
			if item in self.dataset_name[self.person_2]:
				si[item] = 1
		if len(si) == 0 : return 0
		sum_of_squares = sum([pow(self.dataset_name[self.person_1][item] - self.dataset_name[self.person_2][item],2) for item in self.dataset_name[self.person_1] if item in self.dataset_name[self.person_2]])
		return 1/(1+sum_of_squares)

	def sim_pearson(self,person_1,person_2):
		
		""" Returns the Pearson correlation coefficient for person1 and person2 """
		
		self.person_1 = person_1
		self.person_2 = person_2

		# Get the list of mutually rated items

		si = {}
		for item in self.dataset_name[self.person_1]:
			if item in self.dataset_name[self.person_2]: si[item] = 1

		# Find the number of elements
		n = len(si)

		# If they are no ratings n common ,return 0
		if n == 0 : return 0

		# Add up all the preferences
		sum1 = sum([self.dataset_name[self.person_1][it] for it in si])
		sum2 = sum([self.dataset_name[self.person_2][it] for it in si])
		print "sum1: ",sum1
		print "sum2: ", sum2
		# Sum up the squares
		sum1sq = sum([pow(self.dataset_name[self.person_1][it],2) for it in si])
		sum2sq = sum([pow(self.dataset_name[self.person_2][it],2) for it in si])

		print "sum1sq: ",sum1sq
		print "sum2sq: ",sum2sq
		# Sum up the products
		psum = sum([self.dataset_name[self.person_1][it] * self.dataset_name[self.person_2][it] for it in si])
		print "psum: ",psum
		# Calculate pearson Score
		num = psum - (sum1*sum2/n)
		den = sqrt((sum1sq-pow(sum1,2)/n)*(sum2sq - pow(sum2,2)/n))
		if den==0: return 0
		r = num/den
		return r 	


def main():

	""" Function for creating Recommendation instance """
	recommendataion  = Recommendation(critics)
	#print recommendataion.dataset_name['Lisa Rose']
	sim_distance = recommendataion.similarity_distance('Lisa Rose','Gene Seymour')
	#print sim_distance
	simperson = recommendataion.sim_pearson('Lisa Rose','Gene Seymour')
	print simperson

if __name__ == "__main__":
	main()