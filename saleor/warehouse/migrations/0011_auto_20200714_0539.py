# Generated by Django 3.0.6 on 2020-07-14 05:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("warehouse", "0010_auto_20200709_1102"),
    ]

    operations = [
        migrations.AlterField(
            model_name="warehouse",
            name="slug",
            field=models.SlugField(allow_unicode=True, max_length=255, unique=True),
        ),
    ]