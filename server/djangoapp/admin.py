from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel

# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 6


# CarModelAdmin class
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name', 'description']
    search_fields = ['name']


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name',  'dealer_id', 'car_type', 'year']
    search_fields = ['name']


# CarMakeAdmin class with CarModelInline


