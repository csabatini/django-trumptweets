def test_root_url_renders_index_html(client):
    response = client.get('/')
    template_names = [t.name for t in response.templates]

    assert response.status_code == 200
    assert len(template_names) == 2
    assert 'base.html' in template_names
    assert 'index.html' in template_names


def test_tag_id_url_renders_tag_html(client):
    response = client.get('/tag/22/')
    template_names = [t.name for t in response.templates]

    assert response.status_code == 200
    assert len(template_names) == 2
    assert 'base.html' in template_names
    assert 'tag.html' in template_names


def test_invalid_url_returns_404(client):
    response = client.get('/bad_url')
    assert response.status_code == 404
