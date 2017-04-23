from django.shortcuts import render

import trumptweets.services


def index(request):
    tag_list = trumptweets.services.get_tags()
    return render(request, 'index.html', {'tags': tag_list})


def tag(request, tag_id):
    tag_info = trumptweets.services.get_single_tag(tag_id)
    status_rows = trumptweets.services.get_tag_statuses(tag_id)
    return render(request, 'tag.html', {'tag': tag_info, 'status_rows': status_rows})
