from django.contrib import admin
from .models import Regions

class RegionsAdmin(admin.ModelAdmin):
	list_display = ('name_ge', 'created', 'updated')

admin.site.register(Regions, RegionsAdmin)