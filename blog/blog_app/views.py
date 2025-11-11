from django.shortcuts import render
from .models import Articles

def home(req):
    return render(req, 'index.html')
    
def articles(req):
    data = Articles.objects.all()
    return render(req, 'articles.html', {"articles": data})

def view_article(req, id):
    visible_len = 100
    
    return render(req, 'view_article.html', {"article": Articles.objects.get(id=id), "visible_len": visible_len})

def about(req):
    return render(req, 'about.html')