# Create your views here.
from django.shortcuts import render_to_response
from timetabling.models import Event, Location, Timeslot
from django.shortcuts import get_object_or_404


def get_homepage(request):
    timetable = build_row_dictionary()
    locations = Location.objects.all()
    locations.order_by('venue')
    return render_to_response('home.htm', {
        'timetable': timetable, 'locations': locations,
    })


def build_column_dictionary(specific_start_time):
    events_for_start_time = Event.objects.filter(timeslot=specific_start_time)
    events_for_start_time.order_by('location')
    events_by_location = {}
    for event in events_for_start_time:
        events_by_location[event.location] = event
    return events_by_location


def build_row_dictionary():
    timeslots = Timeslot.objects.all()
    timeslots.order_by('start_time')
    events_by_timeslot = {}
    for timeslot in timeslots:
        events_by_timeslot[timeslot] = build_column_dictionary(timeslot)
    return events_by_timeslot
