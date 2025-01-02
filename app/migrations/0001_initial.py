# Generated by Django 5.1.2 on 2025-01-02 21:35

import django.db.models.deletion
import prose.fields
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("pen_name", models.CharField(max_length=250, null=True)),
                ("bio", models.TextField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=200)),
                ("published_date", models.DateTimeField(auto_now_add=True)),
                ("image", models.ImageField(null=True, upload_to="images/")),
                ("snippet", models.CharField(max_length=250)),
                ("main_content", models.TextField(default="")),
                ("content", prose.fields.RichTextField(default="")),
                ("slug", models.SlugField(blank=True, max_length=255, unique=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="articles",
                        to="app.author",
                    ),
                ),
            ],
        ),
    ]
