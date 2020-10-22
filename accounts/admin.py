from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)
admin.site.register(CustomerContactPerson)
admin.site.register(Lead)
admin.site.register(Deal)