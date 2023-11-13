from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from api.resource import MedicineResource  # Импортируйте MedicineResource из правильного места

from .models import User, Imperfection, SkinType, Question, Answer, Medicine, UserTestResult

admin.site.register(User)
admin.site.register(Imperfection)
admin.site.register(SkinType)
admin.site.register(Question)
admin.site.register(Answer)

admin.site.register(UserTestResult)

@admin.register(Medicine)
class MedicineAdmin(ImportExportModelAdmin):  # Используйте ImportExportModelAdmin
    resource_class = MedicineResource  # Укажите ресурс MedicineResource
