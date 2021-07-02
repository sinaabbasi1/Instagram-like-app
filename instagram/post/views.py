from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from post.models import Stream, Post
from django.template import loader

# Create your views here.

@login_required
def index(request):
	user = request.user
	posts = Stream.objects.filter(user=user)
	group_ids = []

	for post in posts:
		group_ids.append(post.post_id)
	post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')	

	template = loader.get_template('index.html')	

	context = {
		'post_items': post_items,
	}
	return HttpResponse(template.render(context, request))
@login_required
def PostDetails(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	template = loader.get_template('post_detail.html')
	context = {
		'post': post,
	}
	return HttpResponse(template.render(context, request))
