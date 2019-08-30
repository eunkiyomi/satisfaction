from django.contrib import admin

# Register your models here.
from .models import Praise
from .models import Profile
from .models import Photo

admin.site.register(Praise)
admin.site.register(Profile)
admin.site.register(Photo)
