# Generated by Django 4.2.1 on 2023-12-16 08:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0004_auto_20210325_0234"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
