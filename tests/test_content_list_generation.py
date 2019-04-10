import pytest

from test_preconditions.content_list_generation.generate import compilation_by_type, content_by_type, preorder
from test_preconditions.certificate import certificate


@pytest.mark.parametrize("content_type", ["single", "bundle"])
def test_content_by_type(content_type):
    content = content_by_type(['SVOD'], 2, content_type, 18)
    assert len(content) == 2


@pytest.mark.parametrize("adult", [True, False])
def test_adult_content(adult):
    content = content_by_type(['SVOD'], 2, adult=adult)
    assert len(content) == 2


@pytest.mark.parametrize("compilation_type", ["with_seasons", "without_seasons"])
def test_compilation_by_type(compilation_type):
    compilation = compilation_by_type(compilation_type, ['SVOD'], 2, 18)
    assert len(compilation) == 2


def test_generate_subscribe_certificate():
    cert = certificate.create()
    assert cert


def test_generate_subscribe_certificate_with_card():
    cert = certificate.create(card='t')
    assert cert


def test_generate_content_certificate():
    cert = certificate.create(type='content')
    assert cert

def test_preoder_list():
    preoders_list = preorder()
    assert len(preoders_list) > 0
