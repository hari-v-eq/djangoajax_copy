from django.contrib import admin
from .models import Student

# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display= ['id','name','email','course']