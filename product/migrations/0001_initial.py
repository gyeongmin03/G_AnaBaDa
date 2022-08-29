# Generated by Django 4.1 on 2022-08-29 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(default="", max_length=50)),
                ("category", models.CharField(default="", max_length=10)),
                ("content", models.TextField(default="")),
                ("write_time", models.DateField(auto_now=True)),
                ("location", models.CharField(default="", max_length=10)),
                (
                    "hashtag",
                    models.CharField(blank=True, default="", max_length=10, null=True),
                ),
                ("count", models.PositiveIntegerField(default=0)),
                (
                    "writer",
                    models.ForeignKey(
                        default="admin",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
