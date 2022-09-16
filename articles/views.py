from django.shortcuts import render
from articles.models import Articles

# Create your views here.



def articlelist(request):
    arti = Articles.objects.all().order_by('date')
    return render(request, 'articles/articlelist.html', {'arts':arti})

