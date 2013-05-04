from django.db import models

class Location(models.Model):
	"""The locaion of the event"""
	venue = models.CharField(max_length=200, unique=True)

	def __unicode__(self):
		return self.venue


class Timeslot(models.Model):
	"""The time slot of the event at the location"""
	start_time = models.DateTimeField()
	duration = models.IntegerField()

	def __unicode__(self):
		return u'%s' % (self.start_time)


class Event(models.Model):
	'''
	A lecture, lesson, game etc. A thing which you attend
	'''
	title = models.CharField(max_length=200, unique=True)
	description = models.TextField()
	contact = models.CharField(max_length=200)
	timeslot = models.ForeignKey(Timeslot, related_name='event_timeslot')
	location = models.ForeignKey(Location, related_name='event_location')

	def __unicode__(self):
		return self.title
