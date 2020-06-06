from django.shortcuts import render
from .models import Tour

def index(request):
    tours = Tour.objects.all()
    return render(
        request,
        'tours/index.html',
        {
            'tours': tours,
            'tour_arrivals': tours.distinct().values_list('arrival_zone__name', flat=True),
            'tour_takeoff': tours.distinct().values_list('takeoff_zone__name', flat=True),
            'user': request.user,
        }
    )