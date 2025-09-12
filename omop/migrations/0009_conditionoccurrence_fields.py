from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ("omop", "0008_concept"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conditionoccurrence",
            name="condition_occurrence_id",
            field=models.BigIntegerField(primary_key=True),
        ),
        migrations.AddField(
            model_name="conditionoccurrence",
            name="person_id",
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="conditionoccurrence",
            name="condition_concept_id",
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="conditionoccurrence",
            name="condition_start_datetime",
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="conditionoccurrence",
            name="condition_end_datetime",
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="conditionoccurrence",
            name="stop_reason",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="conditionoccurrence",
            name="provider_id",
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="conditionoccurrence",
            name="visit_occurrence_id",
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="conditionoccurrence",
            name="visit_detail_id",
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="conditionoccurrence",
            name="condition_source_value",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="conditionoccurrence",
            name="condition_source_concept_id",
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="conditionoccurrence",
            name="condition_status_source_value",
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="conditionoccurrence",
            name="condition_status_concept_id",
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
