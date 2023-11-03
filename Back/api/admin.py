# abstract_user/users/admin.py
from django.contrib import admin

from .models import User, Imperfection, SkinType, Question,Answer, Medicine, UserTestResult

admin.site.register(User)
admin.site.register(Imperfection)
admin.site.register(SkinType)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Medicine)
admin.site.register(UserTestResult)