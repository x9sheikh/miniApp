from django.contrib import admin
from .models import Subject, Mentor, MySmartNote
# Register your models here.

admin.site.register(MySmartNote)
admin.site.register(Subject)
admin.site.register(Mentor)
