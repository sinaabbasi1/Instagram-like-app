from post.views import index, PostDetails, NewPost, tags

from django.urls import path

urlpatterns = [
   	path('', index, name='index'),
   	path('<uuid:post_id>', PostDetails, name='postdetails'),
	path('newpost/', NewPost, name='newpost'),
   	path('tag/<slug:tag_slug>', tags, name='tags'),
]
