from django.urls import path
from notifications.views import ShowNOtifications, DeleteNotification


urlpatterns = [
   	path('', ShowNOtifications, name='show-notifications'),

]
