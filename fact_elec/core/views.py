from django.shortcuts import render

def index(request):
    template_name="Index.html"
    return render(request,template_name)
