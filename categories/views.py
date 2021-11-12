from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from functools import wraps
from .models import Category
from posts.models import Post
from .forms import CategoryForm


def is_author(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        if request.user.id == post.author.id:
            return view_func(request, *args, **kwargs)
        return redirect(post.get_absolute_url())
    return _wrapped_view


def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    posts = Post.objects.filter(category=category)
    return render(request, 'category_detail.html', {'posts': posts})


@login_required(login_url='/account/login/')
def category_adding(request):
    form = CategoryForm()
    if request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Category.objects.create(name=cd['name'])
            return redirect('category_adding')
    categories = Category.objects.all()
    return render(request, 'adding_category.html', {'form': form, 'categories': categories})


@is_author
@login_required(login_url='/account/login/')
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.POST:
        category.delete()
        return redirect('category_adding')
    return render(request, 'category_delete.html', {'category': category})
