from blog.models import Post, Category


def recent_posts(request):
    recent_posts = Post.objects.all().order_by('-date')[:3]
    categories = Category.objects.all()
    return {'recent_posts': recent_posts, 'categories': categories}