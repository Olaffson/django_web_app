from django.test import TestCase

from listings.models import Band, Listing


class PagesTests(TestCase):

    def test_hello_lists_bands(self):
        Band.objects.create(name='Daft Punk')
        response = self.client.get('/hello/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'DAFT PUNK')

    def test_listings_lists_listings(self):
        Listing.objects.create(title='T-shirt de tournée')
        response = self.client.get('/listings/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'T-shirt de tournée')

    def test_listings_empty(self):
        response = self.client.get('/listings/')
        self.assertContains(response, 'Aucune annonce pour le moment.')

    def test_about(self):
        response = self.client.get('/about-us/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'À propos')
