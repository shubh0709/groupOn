from django.contrib import admin

from . import models

# Register your models here.
# admin.register(models.User)
admin.register(models.Messages)
admin.register(models.Subject)
admin.register(models.Group)
admin.register(models.GroupMembers)
admin.register(models.Subject)
admin.register(models.BaseModelClass)
