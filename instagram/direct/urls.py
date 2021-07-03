from django.urls import path
from direct.views import Inbox, Directs
urlpatterns = [
   	path('', Inbox, name='inbox'),
   	path('directs/<username>', Directs, name='directs'),

]