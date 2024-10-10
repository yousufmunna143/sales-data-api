# predictions/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd

def home(request):
    return render(request, 'home.html')

class YearPredictionsView(APIView):
    def get(self, request, year):
        try:
            if year == 2025:
                data = pd.read_csv('predictions/data/prophet_predictions_2025.csv')
            elif year == 2026:
                data = pd.read_csv('predictions/data/prophet_predictions_2026.csv')
            else:
                return Response({"error": "Invalid year"}, status=status.HTTP_400_BAD_REQUEST)

            data = data.rename(columns={'yhat': 'predicted_sales'})
            return Response(data.to_dict(orient='records'))
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
