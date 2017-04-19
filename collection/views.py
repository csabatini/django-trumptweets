from django.shortcuts import render
import services


def index(request):
    tag_list = services.get_tags()
    return render(request, 'index.html', tag_list)


def tag(request, tag_id):
    status_rows = services.get_tag_statuses(tag_id)
    return render(request, 'tag.html', status_rows)
