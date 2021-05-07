from django.contrib import admin
from .models import*
# Register your models here.
class TaxiAdmin(admin.ModelAdmin):
    list_display=['The_beneficial_driver','status','client_name','phonenumber','age_of_driver','location','To']
admin.site.site_header ='Site Administration'
admin.site.site_title ='Site Administration'
admin.site.register(Drivers)
admin.site.register(Taxie ,TaxiAdmin)
admin.site.register(Buse)
admin.site.register(Truckse)
