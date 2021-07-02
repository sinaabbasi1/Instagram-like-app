from post.views import index, PostDetails, NewPost, tags, like, favorite
from django.urls import path

urlpatterns = [
   	path('', index, name='index'),
   	path('<uuid:post_id>', PostDetails, name='postdetails'),
	path('newpost/', NewPost, name='newpost'),
	path('tag/<slug:tag_slug>', tags, name='tags'),
	path('<uuid:post_id>/like', like, name='postlike'),
	path('<uuid:post_id>/favorite', favorite, name='postfavorite'),
]
