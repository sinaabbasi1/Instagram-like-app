from post.views import index, PostDetails, NewPost

from django.urls import path

urlpatterns = [
   	path('', index, name='index'),
   	path('<uuid:post_id>', PostDetails, name='postdetails'),
	  path('newpost/', NewPost, name='newpost'),
]
