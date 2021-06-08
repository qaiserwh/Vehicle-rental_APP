from django.contrib import admin
from.models import*
# Register your models here.
class TaxiAdmin(admin.ModelAdmin):
    list_display=['The_beneficial_driver','status','client_name','phonenumber','time','location','To']
    search_fields=['The_beneficial_driver']
class BusAdmin(admin.ModelAdmin):
    list_display=['The_beneficial_driver','status','client_name','phonenumber','time','location','To']
    search_fields=['The_beneficial_driver']
class DriverAdmin(admin.ModelAdmin):
    list_display=['name','email','phonenumber','Type_of_car','carnumber']
class TruckseAdmin(admin.ModelAdmin):
    list_display=['The_beneficial_driver','status','client_name','phonenumber','time','Type_of_load','location','To']
class VipBusAdmin(admin.ModelAdmin):
    list_display=['The_beneficial_driver','status','clientname','phonenumber','price','time','location','To']
    search_fields=['The_beneficial_driver']



admin.site.site_header ='الادارة'
admin.site.site_title ='صفحة الادارة'
admin.site.register(Drivers,DriverAdmin)
admin.site.register(Taxie ,TaxiAdmin)
admin.site.register(Buse,BusAdmin)
admin.site.register(VipBuse,VipBusAdmin)
admin.site.register(Truckse,TruckseAdmin)
