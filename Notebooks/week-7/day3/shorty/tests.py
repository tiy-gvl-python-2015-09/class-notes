from django.test import TestCase
from shorty.models import UrlRecord

# Create your tests here.


class ModelTests(TestCase):

    def test_short_url_is_created_automatically(self):
        url_record = UrlRecord.objects.create(long_url="http://joel.io")
        self.assertNotEqual(url_record.short_url, "")
        self.assertEqual(len(url_record.short_url), 5)