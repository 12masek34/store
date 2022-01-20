from django.contrib import admin

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(CustomUser)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
