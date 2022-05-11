from django.test import TestCase, Client
from django.urls import reverse
from App.models import Customers
import json


class TestViews(TestCase):
    # def setuo(self):
    #     self.client = Client

    def test_index_view_GET(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'index.html')
