from django.contrib import admin
# from .models import related models
from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Set the number of inline forms to display

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    # Customize the display of CarModel in the admin
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id')

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
