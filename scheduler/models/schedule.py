class Schedule(object):

	def __init__(self, name, activities, start_dt, end_dt):
		self.name = name
		self.activities = activities # unscheduled list of activities
		self.start_dt = start_dt
		self.end_dt = end_dt
