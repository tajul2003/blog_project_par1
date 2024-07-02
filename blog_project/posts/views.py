from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from . import models

# Create your views here.
def add_post(request):
    if request.method == 'POST':
        add_post_forms = forms.PostForm(request.POST)
        if add_post_forms.is_valid():
            add_post_forms.save()
            return redirect('homepage')  # Redirect to the homepage or another page
    else:
        add_post_forms = forms.PostForm()
    return render(request, 'add_post.html', {'form': add_post_forms})

def edit_post(request, id):
    post = get_object_or_404(models.Post, pk=id)
    if request.method == 'POST':
        add_post_forms = forms.PostForm(request.POST, instance=post)
        if add_post_forms.is_valid():
            add_post_forms.save()
            return redirect('homepage')  # Redirect to the homepage or another page
    else:
        add_post_forms = forms.PostForm(instance=post)
    return render(request, 'add_post.html', {'form': add_post_forms})


def delete_post(request,id):
    post=models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')  