# Generated by Django 5.1.2 on 2024-11-13 16:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0006_remove_article_content_article_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="main_content",
            field=models.TextField(default=""),
        ),
    ]
