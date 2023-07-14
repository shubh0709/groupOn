# Generated by Django 4.2.2 on 2023-07-14 03:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BaseModelClass",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "basemodelclass_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="groupOn.basemodelclass",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
                (
                    "creator_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=("groupOn.basemodelclass",),
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "basemodelclass_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="groupOn.basemodelclass",
                    ),
                ),
                ("name", models.CharField(max_length=25)),
            ],
            bases=("groupOn.basemodelclass",),
        ),
        migrations.CreateModel(
            name="Messages",
            fields=[
                (
                    "basemodelclass_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="groupOn.basemodelclass",
                    ),
                ),
                ("message", models.TextField()),
                (
                    "group_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="groupOn.group",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=("groupOn.basemodelclass",),
        ),
        migrations.CreateModel(
            name="GroupMembers",
            fields=[
                (
                    "basemodelclass_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="groupOn.basemodelclass",
                    ),
                ),
                (
                    "group_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="groupOn.group",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=("groupOn.basemodelclass",),
        ),
        migrations.AddField(
            model_name="group",
            name="message_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="groupOn.messages",
            ),
        ),
        migrations.AddField(
            model_name="group",
            name="subject_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="groupOn.subject",
            ),
        ),
    ]
