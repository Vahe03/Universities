from django.contrib import admin
from universities.models import University, Student


# Register your models here.
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rank', 'country']
    search_fields = ['name', ]
    list_filter = ['country']


admin.site.register(University, UniversityAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_universities']
    search_fields = ['name', ]

    def get_universities(self, obj):
        return '123'

admin.site.register(Student, StudentAdmin)
