# Generated by Django 5.0.6 on 2024-10-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_article_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="pen_name",
            field=models.CharField(max_length=250, null=True),
        ),
    ]
