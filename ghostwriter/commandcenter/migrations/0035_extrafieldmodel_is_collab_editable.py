# Generated by Django 4.2 on 2025-06-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("commandcenter", "0034_merge_20250110_1938"),
    ]

    operations = [
        migrations.AddField(
            model_name="extrafieldmodel",
            name="is_collab_editable",
            field=models.BooleanField(default=False),
        ),
    ]
