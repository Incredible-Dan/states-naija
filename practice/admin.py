from django.contrib import admin

# Register your models here.
from practice.models import State, Capital, Region, Tribe

admin.site.register(State)
admin.site.register(Capital)
admin.site.register(Region)
admin.site.register(Tribe)
