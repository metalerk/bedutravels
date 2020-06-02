from django.contrib import admin
from .models import (
    Tour,
    User,
    Zone,
)


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'last_name', 
        'nickname', 
        'email', 
        'gender', 
        'birthday',
    )


class TourAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'operator', 
        'slug', 
        'tour_type', 
        'description', 
        'country', 
        'takeoff_zone', 
        'arrival_zone',
    )


class ZoneAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'latitude', 'longitude',)

admin.site.register(User, UserAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(Zone, ZoneAdmin)