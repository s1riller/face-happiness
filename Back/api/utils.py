from .models import UserTestResult, Medicine


def get_medicines_for_user(user_id):
    
    user_test_results = UserTestResult.objects.filter(user=user_id)

    
    medicine_ids = user_test_results.values_list('answers__Какие имеются несовершенства', flat=True)

    
    medicines = Medicine.objects.filter(id__in=medicine_ids)

    return user_test_results

