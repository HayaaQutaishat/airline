from ast import Pass
from tkinter import HORIZONTAL
from django.contrib import admin

from flights.models import Airport, Flight, Passenger

# Register your models here.
class AirportAdmin(admin.ModelAdmin):
    list_display= ("city", "code")

class FlightAdmin(admin.ModelAdmin):
    list_display= ("id","origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal= ("flights", )
    

admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
