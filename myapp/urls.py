from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.financial_planner,name='financial_planner'),
]