# predictions/urls.py
from django.urls import path
from .views import home, YearPredictionsView

urlpatterns = [
    path('', home, name='home'),
    path('predictions/<int:year>/', YearPredictionsView.as_view(), name='year_predictions'),
]
