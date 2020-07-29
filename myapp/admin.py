from django.contrib import admin
from myapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['No', 'Name', 'Age', 'Mobile_No']
admin.site.register(Student, StudentAdmin)
