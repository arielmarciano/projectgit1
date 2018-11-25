from django.contrib import admin
from main_app.models import User, Tweet

admin.site.register(User)
admin.site.register(Tweet)