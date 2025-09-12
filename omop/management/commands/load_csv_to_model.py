import csv
from django.core.management.base import BaseCommand
from omop import models

class Command(BaseCommand):
    help = "Load data from a CSV file into a specified OMOP model."

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Name of the OMOP model (PascalCase)')
        parser.add_argument('csv_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        model_name = options['model_name']
        csv_path = options['csv_path']
        model = getattr(models, model_name, None)
        if model is None:
            self.stderr.write(self.style.ERROR(f"Model '{model_name}' not found in omop.models."))
            return
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            objs = []
            for row in reader:
                mapped_row = {k.lower(): (v if v != '' else None) for k, v in row.items()}
                objs.append(model(**mapped_row))
            model.objects.bulk_create(objs)
        self.stdout.write(self.style.SUCCESS(f"Loaded data from {csv_path} into {model_name}"))
