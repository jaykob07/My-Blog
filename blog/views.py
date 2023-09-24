from django.shortcuts import render, get_object_or_404
from .models import Post

def render_post(request):              # esta funcion retorna el html posts
    posts = Post.objects.all()
    return render(request, 'posts.html', {'articulos': posts})


def post_details(request, post_id):
    vista = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_details.html', {'vistas': vista})


