from django.shortcuts import render , redirect
from . import forms
# Create your views here.
def add_author(request):
    if request.method == 'POST':
        author_forms=forms.AuthorForm(request.POST)
        if author_forms.is_valid():
            author_forms.save()
            return redirect('add_author')
    else:
        author_forms=forms.AuthorForm()
    return render(request,'add_author.html',{'form' : author_forms})