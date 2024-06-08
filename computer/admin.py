from django.contrib import admin
from .models import ComputerBrands, ComputerSpecification, Computer

# Register your models here.
admin.site.register(ComputerBrands)
admin.site.register(ComputerSpecification)
admin.site.register(Computer)