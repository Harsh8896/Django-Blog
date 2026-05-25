from django.shortcuts import render
from blogs.models import Category, Blog


def home(request):
    # categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True, status="published").order_by("updated_at")
    posts = Blog.objects.filter(is_featured=False, status="published").order_by("updated_at")
    # print(posts)
    context = {
        # 'categories': categories,
        'featured_post': featured_post,
        'posts': posts

    }
    return render(request, "home.html", context)