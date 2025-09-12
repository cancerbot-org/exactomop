from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ("omop", "0007_conceptancestor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Concept",
            fields=[
                ("concept_id", models.BigIntegerField(primary_key=True)),
                ("concept_name", models.CharField(max_length=255)),
                ("domain_id", models.CharField(max_length=100)),
                ("vocabulary_id", models.CharField(max_length=100)),
                ("concept_class_id", models.CharField(max_length=100)),
                ("standard_concept", models.CharField(max_length=10, null=True, blank=True)),
                ("concept_code", models.CharField(max_length=100)),
                ("valid_start_date", models.DateField()),
                ("valid_end_date", models.DateField()),
                ("invalid_reason", models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={"db_table": "concept"},
        ),
    ]
