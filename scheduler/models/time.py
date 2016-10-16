class Time(object):

	def __init__(self, dt):
		self.dt = dt # datetime object

	def weekday(self):
		return self.dt.weekday()

	def time(self):
		return self.dt.hour, self.dt.minute

