from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Article)
admin.site.register(Keywords)
admin.site.register(KeywordList)
admin.site.register(Person)
admin.site.register(Organization)
admin.site.register(PersonList)
admin.site.register(OrganizationList)



