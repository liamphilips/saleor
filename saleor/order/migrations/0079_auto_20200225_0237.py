# Generated by Django 2.2.10 on 2020-02-25 08:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0078_auto_20200221_0257"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="fulfillment",
            options={"ordering": ("pk",)},
        ),
    ]