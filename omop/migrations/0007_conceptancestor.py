from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ("omop", "0006_visitoccurrence"),
    ]

    operations = [
        migrations.CreateModel(
            name="ConceptAncestor",
            fields=[
                ("id", models.AutoField(primary_key=True)),
                ("ancestor_concept_id", models.BigIntegerField()),
                ("descendant_concept_id", models.BigIntegerField()),
                ("min_levels_of_separation", models.IntegerField()),
                ("max_levels_of_separation", models.IntegerField()),
            ],
            options={"db_table": "concept_ancestor"},
        ),
    ]
