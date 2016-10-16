from math import sqrt

class Location(object):

	def __init__(self, latitude, longitude):
		self.latitude = latitude
		self.longitude = longitude

	def calc_travel_time(self, other_location):
		return 2 * self.calc_distance(other_location)

	def calc_distance(self, other_location):
		return sqrt(
				pow((self.latitude - other_location.latitude), 2) +
				pow((self.longitude - other_location.longitude), 2))

	def __str__(self):
		return str(self.latitude) + ',\n' + str(self.longitude)
