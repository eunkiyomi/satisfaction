from django.contrib import admin

# Register your models here.
from .models import Praise
from .models import Profile

admin.site.register(Praise)
admin.site.register(Profile)
