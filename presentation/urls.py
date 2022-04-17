from django.urls import path

from presentation.views import PresentationCreateAndListAPIView, PresentationDetailAPIView

urlpatterns = [
    path('', PresentationCreateAndListAPIView.as_view()),
    path('<int:pk>/', PresentationDetailAPIView.as_view()),
]
