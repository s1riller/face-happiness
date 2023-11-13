import json

from django.conf import settings
from django.core.management.base import BaseCommand
from api.models import Medicine, UserTestResult

class Command(BaseCommand):
    help = 'Recommend medicine for user'

    def handle(self, *args, **options):
        results_with_empty_medicine = UserTestResult.objects.all()

        for result in results_with_empty_medicine:
            answer_texts = result.answers

            recommended_medicines = []

            for question, answers in answer_texts.items():
                answers_text = ', '.join(filter(None, answers))

                related_medicines = Medicine.objects.filter(treats__text__in=answers)

                recommended_medicines.extend(related_medicines)

            unique_recommended_medicines = set(recommended_medicines)

            recommended_medicine_info = []
            for medicine in unique_recommended_medicines:
                medicine_info = {
                    "name": medicine.name,
                    "description": medicine.description,
                    "treats": medicine.treats.text,
                    "img": medicine.img,
                }
                recommended_medicine_info.append(medicine_info)

            recommended_medicine_json = json.dumps(recommended_medicine_info)
            result.medicine = recommended_medicine_json
            result.save()

            # self.stdout.write(f"User Test Result ID: {result.id}")
            # self.stdout.write(f"Recommended Medicine (JSON): {recommended_medicine_json}")
