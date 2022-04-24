from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from home.forms import CreateHomeForm, UpdateHomeForm, DeleteHomeFrom
from home.models import HomeModel


class HomeView(ListView):
    model = HomeModel
    template_name = "base.html"


def create_home_view(request):

    context = {}

    form = CreateHomeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = CreateHomeForm()

    context['form'] = form

    return render(request, 'create.html', context)


def update_home_view(request, id):
    context = {}

    article = get_object_or_404(HomeModel, id=id)

    if request.POST:
        form = UpdateHomeForm(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            form.save()
            # obj.save()
            context['success_message'] = "Updated"

    form = UpdateHomeForm(
        initial={
            'title': article.title,
            'body': article.body,
            'primer': article.primer,
        }
    )

    context['form'] = form
    return render(request, 'update.html', context)


def delete_home_view(request, id):

    context = {}

    article = get_object_or_404(HomeModel, id=id)

    if request.POST:
        form = DeleteHomeFrom(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.save()
            context['success_message'] = "Updated"
            article = obj

    form = DeleteHomeFrom(
        initial={
            'title': article.title,
            'body': article.body,
            'primer': article.primer,
        }
    )

    context['form'] = form
    return render(request, 'delete.html', context)
