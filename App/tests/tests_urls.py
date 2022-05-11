from django.test import SimpleTestCase
from App.views import index
from django.urls import resolve,reverse
class TestUrls(SimpleTestCase):
    def test_index_url_resolved(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func,index)

    # def test_index_url_resolved(self):