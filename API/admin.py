# Register your models here.
from django.contrib import admin

from API.models import Users, ActivityPeriod, Members

admin.site.register(Users)
admin.site.register(ActivityPeriod)
admin.site.register(Members)
