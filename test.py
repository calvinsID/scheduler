from scheduler.models.activity import Activity
from scheduler.models.location import Location
from scheduler.models.schedule import Schedule
from scheduler.scheduler import Scheduler

import random

def generate_random_activity(uuid):
	location = Location(
		random.randint(1, 100),
		random.randint(1, 100))

	activity = Activity(
		uuid,
		'activity' + str(uuid),
		location,
		random.randint(10, 180)
	)

	return activity

def create_schedule(num_activities):
	activities = []
	for i in xrange(num_activities):
		activities.append(generate_random_activity(i))

	schedule = Schedule(
		'schedule',
		activities,
		1,
        2
	)

	return schedule

if __name__ == '__main__':
	print '#### UNSCHEDULED ####'

	schedule = create_schedule(10)

	for activity in schedule.activities:
		activity.output()

	scheduler = Scheduler()

	scheduled, distance = scheduler.schedule(schedule)

	print '#### SCHEDULED ####'
	print distance
	for activity in scheduled:
		activity.output()


