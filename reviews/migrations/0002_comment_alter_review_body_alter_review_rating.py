# Generated by Django 4.1.3 on 2024-03-08 12:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField()),
                ("review_id", models.IntegerField()),
                ("body", models.TextField(blank=True, null=True)),
                ("date_posted", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name="review",
            name="body",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(5),
                ]
            ),
        ),
    ]
