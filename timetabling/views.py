# Create your views here.
from django.shortcuts import render_to_response
from timetabling.models import Event, Location, Timeslot
from django.shortcuts import get_object_or_404


def getHomepage(request):
	timeslots = Timeslot.objects.all()
	timeslots.order_by('location', 'start_time')
	events = Event.objects.all()
	events.order_by('timeslot.start_time')
	return render_to_response('home.htm', {
		'timeslots' : timeslots,
		'events' : events,
	})
