import requests

base_url = 'https://trumptweets.slickmobile.us/'


def get_tags():
    r = requests.get(base_url + 'api/v1/tag')
    return {'tags': r.json()}


def get_tag_statuses(tag_id):
    r = requests.get(base_url + 'api/v1/status', params={'tag_id': tag_id})
    status_rows = partition_status_rows(r.json())
    return {'status_rows': status_rows}


def partition_status_rows(statuses):
    status_count = len(statuses)
    num_rows = status_count / 3

    status_rows = []
    for i in range(0, num_rows):
        status_rows.append(statuses[(i * 3):(i * 3 + 3)])

    if status_count % 3 > 0:
        status_rows.append(statuses[((num_rows - 1) * 3 + 3):])

    return status_rows
