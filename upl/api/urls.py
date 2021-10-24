from django.urls import path
from api import views

urlpatterns = [
    # path('watper/<int:id>', views.watperm, name="watper"),
    path('watperm/<int:id>', views.watsonperm, name="watperm"),
]