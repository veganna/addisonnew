from django.shortcuts import render
from .models import *



def index(request):
    context = {}
    pictures = Picture.objects.all()
    categories = PictureCategory.objects.all()
    context['pictures'] = pictures
    context['categories'] = categories
    
    if request.method=="POST":
        content = request.POST
        name = content.get('name')
        email = content.get('email')
        instance = ContactForm(name = name, email = email)
        instance.save()
    
    home = HomepageStyle.objects.get(pk=1)
    context['homestyle'] = home  
    return render(request, 'index.html', context)
