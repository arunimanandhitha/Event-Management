from django.contrib import admin
from .models import Event, Booking, EventImage

class EventImageInline(admin.TabularInline):   # Inline sub-images in Event
    model = EventImage
    extra = 3   # show 3 empty slots by default

class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]

admin.site.register(Event, EventAdmin)
admin.site.register(Booking)