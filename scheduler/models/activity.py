class Activity(object):

	def __init__(self,
				 uuid,
				 name,
				 location,
				 duration=None):
		self.uuid = uuid
		self.name = name
		self.location = location
		self.duration = duration # suggested duration / actual duration
		# self.start_time = start_time
		# self.end_time = end_time

	def calc_distance(self, other_activity):
		return self.location.calc_distance(
			other_activity.location)

	def output(self):
		print 'ACTIVITY:'
		# print self.uuid
		print self.name
		print self.location.latitude
		print self.location.longitude
		print self.duration
