from django.shortcuts import render
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
