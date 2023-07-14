import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class BaseModelClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
        
class Subject(BaseModelClass):
    name = models.CharField(max_length=25)


class Group(BaseModelClass):
    subject_id = models.ForeignKey(
        to=Subject, on_delete=models.SET_NULL, null=True)
    creator_id = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=120)


class GroupMembers(BaseModelClass):
    user_id = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    group_id = models.ForeignKey(
        to=Group, on_delete=models.SET_NULL, null=True)


class Messages(BaseModelClass):
    message = models.TextField()
    user_id = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    group_id = models.ForeignKey(
        to=Group, on_delete=models.SET_NULL, null=True)
