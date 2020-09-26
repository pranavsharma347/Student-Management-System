from django.contrib import admin
from StudentManagementApp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['Rollno','user','FirstName','LastName','Course','Mobileno','Email','Address']

admin.site.register(Student,StudentAdmin)
