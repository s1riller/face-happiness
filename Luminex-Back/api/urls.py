from django.contrib import admin
from django.urls import path, include

from api.serializers import UserTestResultListView
from api.views import *
from import_export.admin import ImportMixin

from api.views import profile_view

urlpatterns = [
    path('profile',UserInfoView.as_view(), name="profile"),
    path('skintypes/', SkinTypeList.as_view(), name='skintype-list'),
    path('questions/', QuestionView.as_view()),
    path('user_test_results/', UserTestResultView.as_view(), name='user-test-results'),
    path('usertestresults/', UserTestResultListView.as_view(), name='usertestresult-list'),
    path('medicines/', MedicineListView.as_view(), name='medicine-list'),
    path('usertestresults2/', UserTestResultList.as_view(), name='usertestresult-list'),
    # path('usertestresults/<int:pk>/', UserTestResultDetail.as_view(), name='usertestresult-detail'),

]
