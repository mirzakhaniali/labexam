from django.urls import path
from .views import user_inputs, create_model_instance, success_page

urlpatterns = [
    path('user_inputs/', user_inputs, name='user_inputs'),
    path('create/', create_model_instance, name='create_model'),
    path('success/', success_page, name='success_page'),
]
