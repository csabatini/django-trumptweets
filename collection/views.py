from django.shortcuts import render
import services


def index(request):
    tag_list = services.get_tags()
    return render(request, 'index.html', tag_list)
