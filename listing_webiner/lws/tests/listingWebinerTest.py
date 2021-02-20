from django.test import TestCase
from lws.views.listingWebinerView import listingWebiner
from django.urls import reverse

class ListingWebinerTest(TestCase):
    def testUrlResolvesToListingWebinerView(self):
        found = reverse('/lws/webiner/')
        self.assertEqual(found.func, webiner_list)