from django.contrib import admin
from myapp.models import Customer,Gallery,Tour,Booking

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass
    # search_fields=["Fname","Email","Phone"]
    # list_filter=["Age","Genders","Added_on"]
admin.site.register(Customer)
admin.site.register(Gallery)
admin.site.register(Tour)
admin.site.register(Booking)


