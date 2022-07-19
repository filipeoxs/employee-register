from django.contrib import admin
from .models import Employee, Position

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    fields = ['fullname','emp_code','mobile','position']
admin.site.register(Employee, EmployeeAdmin)

class PositionAdmin(admin.ModelAdmin):
    fields = ['title']
admin.site.register(Position, PositionAdmin)