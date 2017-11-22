from django.contrib import admin
from polls.models import UserProfile
from polls.models import Posts

admin.site.register(UserProfile)
admin.site.register(Posts)
