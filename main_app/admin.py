from django.contrib import admin
from .models import Regions, Districts

class RegionsAdmin(admin.ModelAdmin):
	list_display = ('name_ge', 'created', 'updated') #Only applies to the Django Admin interface.
	readonly_fields = ('created', 'updated') #Only applies to the Django Admin interface.
	history_list_display = ["name_ge"] #Only applies to the Django Admin interface.

admin.site.register(Regions, RegionsAdmin)

class DistrictsAdmin(admin.ModelAdmin):
	list_display = ('region', 'name_ge', 'created', 'updated')
	readonly_fields = ('created', 'updated')
	history_list_display = ["name_ge"]

admin.site.register(Districts, DistrictsAdmin)