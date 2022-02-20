from django.contrib import admin
from rango.models import Category, Page

class PageAdmain(admin.ModelAdmin):
    list_display = ('title','category','url')

admin.site.register(Page,PageAdmain) 

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

