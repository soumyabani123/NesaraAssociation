from django.contrib import admin
from .models import member
from .models import meeting

# Register your models here.

admin.site.register(member)
admin.site.register(meeting)
