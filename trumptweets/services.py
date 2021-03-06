import requests

base_url = 'https://trumptweets.slickmobile.us/api/v1/'


class ApiService(object):
    def get_tags(self):
        tag_list = self.get_url_json(base_url + 'tag')
        return {'tags': tag_list}

    def get_tag_statuses(self, tag_id):
        tag = self.get_url_json(base_url + 'tag', params={'id': tag_id})
        statuses = self.get_url_json(base_url + 'status', params={'tag_id': tag_id})
        return {
            'tag': tag,
            'status_rows': self.partition_status_rows(statuses)
        }

    def get_url_json(self, url, params={}):
        resp = requests.get(url, params=params)
        return resp.json()

    #
    # partition_status_rows is a helper function for dividing a list into a grid (2d list) of x rows by 3 columns
    # If the original number of objects isn't divisible by 3, the remainder (1 or 2) will be in the last row
    #
    def partition_status_rows(self, statuses):
        status_count = len(statuses)
        num_rows = status_count / 3

        status_rows = []
        for i in range(0, num_rows):
            status_rows.append(statuses[(i * 3):(i * 3 + 3)])

        if status_count % 3 > 0:
            status_rows.append(statuses[((num_rows - 1) * 3 + 3):])

        return status_rows
