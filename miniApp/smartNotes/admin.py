from django.contrib import admin
from .models import Subject, Mentor, SmartNotes
# Register your models here.

admin.site.register(SmartNotes)
admin.site.register(Subject)
admin.site.register(Mentor)
