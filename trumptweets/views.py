from django.shortcuts import render

from trumptweets.services import ApiService

service = ApiService()


def index(request):
    return render(request, 'index.html', service.get_tags())


def tag(request, tag_id):
    return render(request, 'tag.html', service.get_tag_statuses(tag_id))
