# Generated by Django 3.0.10 on 2020-11-19 23:43

from django.db import migrations, models
import ghostwriter.reporting.models
import ghostwriter.reporting.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0020_auto_20201105_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidence',
            name='document',
            field=models.FileField(blank=True, upload_to=ghostwriter.reporting.models.Evidence.set_upload_destination, validators=[ghostwriter.reporting.validators.validate_evidence_extension]),
        ),
    ]
