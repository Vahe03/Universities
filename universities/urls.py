from django.urls import path
from . import views

urlpatterns = [
    path('', views.universities, name='universities'),
    path('', views.UniversityListView.as_view(), name='universities'),
    path('<int:id>', views.university, name='university'),
    path('<int:pk>', views.UniversityDetailView.as_view(), name='university'),

]
