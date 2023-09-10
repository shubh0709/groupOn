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
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class Group(BaseModelClass):
    subject_id = models.ForeignKey(
        to=Subject, on_delete=models.SET_NULL, null=True)
    creator_id = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class GroupMembers(BaseModelClass):
    user_id = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    group_id = models.ForeignKey(
        to=Group, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Members: {self.user_id.username} {self.group_id.name}"


class Messages(BaseModelClass):
    message = models.TextField()
    member = models.ForeignKey(
        to=GroupMembers, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"\nuser - {self.member.user_id.username}\ngroupName - {self.member.group_id.name} \nmessage - {self.message}"
