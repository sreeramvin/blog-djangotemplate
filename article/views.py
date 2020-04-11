from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms



# Create your views here.
def artilce_list(request):
    articles=Article.objects.all()
    return render(request, 'article/article.html',{'articles':articles})

def article_detail(request, slug_n):
    article= Article.objects.get(slug=slug_n)
    return render(request, 'article/article_detail.html',{'article':article})

@login_required(login_url="/accounts/login")
def article_create(request):
    if request.method =='POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('article:list')      
    else:
        form = forms.CreateArticle()
    return render(request, 'article/article_create.html',{'form':form})
