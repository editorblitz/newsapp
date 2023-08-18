from django.urls import path
from .views import dashboard, SaveOrderView

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('save_order/', SaveOrderView.as_view(), name='save_order'),
]
