from django.contrib import admin
from .models import Image, Todo
# from import_export.admin import ImportExportModelAdmin


# class todoAdmin(ImportExportModelAdmin):
#     list_display = ['name']
#     list_filter = ['name']
#     exclude = ['slug']
#

# admin.site.register(todo, todoAdmin)
admin.site.register(Image)
admin.site.register(Todo)


