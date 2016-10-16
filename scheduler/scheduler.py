class Scheduler(object):
	
	@classmethod
	def schedule(cls, schedule):
		# schedule the schedule

		scheduled_activities, min_distance = cls.simple_schedule(schedule)

		return scheduled_activities, min_distance

	# Returns a simple schedule of activites
	# The order in which to perform the activites,
	# according to the minimum travelling time between locations
	@classmethod
	def simple_schedule(cls, schedule):
		distances_graph = cls.generate_distance_graph(schedule)

		optimal_path = []
		min_distance = None

		for activity in schedule.activities:
			path, total_distance = cls.find_shortest_path_greedy(activity, schedule.activities, distances_graph)
			if min_distance is None or total_distance < min_distance:
				optimal_path = path
				min_distance = total_distance

		return optimal_path, min_distance

	# Finds the distances between every pair of activities
	# in the schedule.
	@classmethod
	def generate_distance_graph(cls, schedule):
		distances_graph = {}
		for i, activity_1 in enumerate(schedule.activities):
			for activity_2 in schedule.activities[i+1:]:
				distance = activity_1.calc_distance(activity_2)
				if activity_1.uuid < activity_2.uuid:
					key = (activity_1.uuid, activity_2.uuid)
				else:
					key = (activity_2.uuid, activity_1.uuid)
				distances_graph[key] = distance

		return distances_graph

	# # Traverses the graph given a starting node
	# # Finds the shortest path that passes through all nodes once
	# @classmethod
	# def find_shortest_path(start_node, nodes, weights):
	# 	# Djikstra's
	# 	# Hamiltonian Path
	# 	# Travellin Salesman

	@classmethod
	def find_shortest_path_greedy(cls, current_location, destinations, distances_graph):
		path = []
		total_distance = 0

		path.append(current_location)

		while destinations:
			destinations.remove(current_location) # Remove the start node
			if destinations:
				next_destination, distance = cls.get_next_destination(
					current_location,
					destinations,
					distances_graph)

				path.append(next_destination)
				total_distance = total_distance + distance

				current_location = next_destination

		return path, total_distance

	@classmethod
	def get_next_destination(cls, current, destinations, distances_graph):
		# Given the current location, find the next closest destination
		# Distances is the distance graph: map of (activity1, activity2) -> distance
		next_destination = None
		min_distance = None
		distances = []
		for destination in destinations:
			if current.uuid < destination.uuid:
				key = (current.uuid, destination.uuid)
			else:
				key = (destination.uuid, current.uuid)
			distance = distances_graph[key]
			if min_distance is None or distance < min_distance:
				next_destination = destination
				min_distance = distance

		return next_destination, min_distance
