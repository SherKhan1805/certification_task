from django.contrib import admin

from hierarchy.models import Contacts, Products, Factory, Retail, Entrepreneur

admin.site.register(Contacts)
admin.site.register(Products)
admin.site.register(Factory)
admin.site.register(Retail)
admin.site.register(Entrepreneur)
