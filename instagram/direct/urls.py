from django.urls import path
from direct.views import Inbox
urlpatterns = [
   	path('', Inbox, name='inbox'),

]