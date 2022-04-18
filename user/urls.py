from django.urls import path

from user.views import UserDetailAPIVIew

urlpatterns = [
    path('<int:pk>/', UserDetailAPIVIew.as_view()),

]
