# Generated by Django 3.0.10 on 2020-10-28 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reporting", "0018_auto_20201027_1914"),
        ("commandcenter", "0003_auto_20201027_1914"),
    ]

    operations = [
        migrations.AddField(
            model_name="reportconfiguration",
            name="enable_borders",
            field=models.BooleanField(default=False, help_text="Enable borders around images in Word documents"),
        ),
        migrations.AlterField(
            model_name="reportconfiguration",
            name="default_docx_template",
            field=models.ForeignKey(
                blank=True,
                help_text="Select a default Word template",
                limit_choices_to={"doc_type__doc_type__iexact": "docx"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reportconfiguration_docx_set",
                to="reporting.ReportTemplate",
            ),
        ),
        migrations.AlterField(
            model_name="reportconfiguration",
            name="default_pptx_template",
            field=models.ForeignKey(
                blank=True,
                help_text="Select a default PowerPoint template",
                limit_choices_to={"doc_type__doc_type__iexact": "pptx"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reportconfiguration_pptx_set",
                to="reporting.ReportTemplate",
            ),
        ),
    ]
