from django.contrib import admin

from . import models

# Register your models here.
# admin.register(models.User)
admin.site.register(models.Messages)
admin.site.register(models.Subject)
admin.site.register(models.Group)
admin.site.register(models.GroupMembers)
