from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ("omop", "0005_remove_person_location_person_birth_datetime_and_more"), # Adjust the name if your migration 5 is different
    ]

    operations = [
        migrations.CreateModel(
            name="VisitOccurrence",
            fields=[
                ("visit_occurrence_id", models.BigIntegerField(primary_key=True)),
                ("person_id", models.BigIntegerField(null=True, blank=True)),
                ("visit_concept_id", models.BigIntegerField(null=True, blank=True)),
                ("visit_start_date", models.DateField(null=True, blank=True)),
                ("visit_start_datetime", models.DateTimeField(null=True, blank=True)),
                ("visit_end_date", models.DateField(null=True, blank=True)),
                ("visit_end_datetime", models.DateTimeField(null=True, blank=True)),
                ("visit_type_concept_id", models.BigIntegerField(null=True, blank=True)),
                ("provider_id", models.BigIntegerField(null=True, blank=True)),
                ("care_site_id", models.BigIntegerField(null=True, blank=True)),
                ("visit_source_value", models.CharField(max_length=255, null=True, blank=True)),
                ("visit_source_concept_id", models.BigIntegerField(null=True, blank=True)),
                ("admitting_source_concept_id", models.BigIntegerField(null=True, blank=True)),
                ("admitting_source_value", models.CharField(max_length=255, null=True, blank=True)),
                ("discharge_to_concept_id", models.BigIntegerField(null=True, blank=True)),
                ("discharge_to_source_value", models.CharField(max_length=255, null=True, blank=True)),
                ("preceding_visit_occurrence_id", models.BigIntegerField(null=True, blank=True)),
            ],
            options={"db_table": "visit_occurrence"},
        ),
    ]
