import pytest
from .factories import PostFactory

@pytest.mark.django_db
def test_post_str():
    post = PostFactory(title="Título de Teste")
    assert str(post) == "Título de Teste"

@pytest.mark.django_db
def test_post_ordering():
    post1 = PostFactory(title="Antigo")
    post2 = PostFactory(title="Novo")
    posts = list(type(post1).objects.all())
    assert posts[0].title == "Novo"  # por causa do ordering = ['-created_on']
