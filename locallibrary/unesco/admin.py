from django.contrib import admin
from unesco.models import Category, Region, States, Iso, Site


admin.site.register(Category)
admin.site.register(Region)
admin.site.register(States)
admin.site.register(Iso)
admin.site.register(Site)