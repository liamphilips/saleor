# Generated by Django 3.2.13 on 2022-04-29 09:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0044_fulfill_checkout_line_new_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="checkoutline",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]