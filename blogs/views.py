from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Blog, Category

# Create your views here.

def post_by_category(request, category_id):
    posts = Blog.objects.filter(status="published", category=category_id)
    # try:
        # category = Category.objects.get(pk=category_id)                     
    # except:
    #     pass 
     #Or
    #Or
    # try:
    #     category = Category.objects.get(pk=category_id)                     
    # except:
    #     return redirect("home")
    #OR
    category = get_object_or_404(Category, pk=category_id)

    context = {
        "posts": posts,
        "category": category,
    }
    return render(request, "post_by_category.html", context)