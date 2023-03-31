from django.urls import path
from .views import polling_unit, total_res_lga

urlpatterns = [
    path('unit/<int:id>', polling_unit),
    path('total_res_lga/', total_res_lga)
]