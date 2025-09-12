import os
import psycopg2
from django.conf import settings
from omop.models import (
    Person, Location, ConditionOccurrence, Measurement, Observation,
    DrugExposure, ProcedureOccurrence, Episode, EpisodeEvent
)
from django.core.management.base import BaseCommand
# Connect to target database
TARGET_DATABASE_URL = os.environ.get('TARGET_DATABASE_URL')
conn = psycopg2.connect(TARGET_DATABASE_URL)
cursor = conn.cursor()

def get_patient_info():
    # Example: gather info from Person and related models
    for person in Person.objects.all():
        info = {
            'person_id': person.person_id,
            'gender_concept_id': person.gender_concept_id,
            'year_of_birth': person.year_of_birth,
            'race_concept_id': person.race_concept_id,
            'ethnicity_concept_id': person.ethnicity_concept_id,
            # Add more fields as needed from related models
        }
        yield info

def insert_patient_info(info):
    columns = ', '.join(info.keys())
    values = ', '.join(['%s'] * len(info))
    sql = f"INSERT INTO trials_patientinfo ({columns}) VALUES ({values})"
    cursor.execute(sql, list(info.values()))
    conn.commit()

class Command(BaseCommand):
    help = "Load patient data from OMOP tables"

    def add_arguments(self, parser):
        parser.add_argument("--n", type=int, default=5)

    def handle(self, *args, **opts):
        for info in get_patient_info():
            insert_patient_info(info)
        self.stdout.write(self.style.SUCCESS("Done loading patient data."))