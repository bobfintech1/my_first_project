from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from post.forms import CreatePostForm, UpdatePostForm, DeletePostFrom
from post.models import PostModel


class PostView(ListView):
    model = PostModel
    template_name = "post.html"


def create_post_view(request):

    context = {}

    form = CreatePostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = CreatePostForm()

    context['form'] = form

    return render(request, 'page/create.html', context)


def update_post_view(request, id):
    context = {}

    article = get_object_or_404(PostModel, id=id)

    if request.POST:
        form = UpdatePostForm(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            form.save()
            # obj.save()
            context['success_message'] = "Updated"

    form = UpdatePostForm(
        initial={
            'title': article.title,
            'body': article.body,
            'primer': article.primer,
        }
    )

    context['form'] = form
    return render(request, 'page/update.html', context)


def delete_post_view(request, id):

    context = {}

    article = get_object_or_404(PostModel, id=id)

    if request.POST:
        form = DeletePostFrom(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.save()
            context['success_message'] = "Updated"
            article = obj

    form = DeletePostFrom(
        initial={
            'title': article.title,
            'body': article.body,
            'primer': article.primer,
        }
    )

    context['form'] = form
    return render(request, 'page/delete.html', context)
