from django.contrib import admin
from . models import Category,District
admin.site.register(Category)
admin.site.register(District)
# Register your models here.
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug':('name',)}

# class DistrictAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug':('name',)}
#     list_per_page = 20





