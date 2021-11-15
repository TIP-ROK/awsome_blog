from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from functools import wraps
from posts.views import Post
from .forms import SearchingUserForm


def is_author(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        if request.user.id == post.author.id:
            return view_func(request, *args, **kwargs)
        return redirect(post.get_absolute_url())
    return _wrapped_view


@login_required(login_url='/account/login/')
def authors_post(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'author_posts.html', {'posts': posts})


def user_search(request):
    form = SearchingUserForm()
    if request.POST:
        form = SearchingUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            posts = Post.objects.filter(author__contains=cd['author'])
    return render(request, 'search_user.html', locals())
