from django.test import TestCase
from django.test import Client

# Create your tests here.
from .models import Gem


class GemViewTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.gem1 = Gem.objects.create(
            name='Jawannite',
            image_filename='jawannite.jpg',
            image_caption='Jawann special mineral',
            category='Tests'
        )

        self.gem2 = Gem.objects.create(
            name='Pretty-rockite',
            image_filename='pretty-rockite.jpg',
            image_caption='Pretty test rock',
            category='Tests',
            crystal_habit='jumping'
        )

        self.gem3 = Gem.objects.create(
            name='George-(Y)',
            image_filename='George-(Y).jpg',
            image_caption='Testing Different Name format',
            category='Tests',
            strunz_classification='00:ZF:45'
        )

    def test_views_exist(self):
        # Issue a GET request.
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gems/gem_list.html')
        response2 = self.client.get('/Jawannite')
        self.assertEqual(response2.status_code, 200)
        self.assertTemplateUsed(response2, 'gems/gem_detail.html')
        response3 = self.client.get('/random')
        self.assertEqual(response3.status_code, 302)

    def test_gem_list_view(self):
        response = self.client.get('/')

        self.assertContains(response, self.gem1.name)
        self.assertContains(response, self.gem2.name)

    def test_gem_name_format(self):
        # Tests to ensure the name formatting is accurate
        self.assertEqual(str(self.gem1), 'Jawannite')
        self.assertEqual(str(self.gem2), 'Pretty-rockite')
        self.assertEqual(str(self.gem3), 'George')

    def test_gem_detail_view(self):
        response = self.client.get('/George-(Y)')
        response2 = self.client.get('/Pretty-rockite')
        response3 = self.client.get('/fakefake')

        # Verifies that empty options are not shown
        self.assertNotContains(response, 'Crystal Habit')

        # Verifies that it's title case and underscores have been removed
        self.assertContains(response, 'Strunz Classification')
        self.assertContains(response2, 'Crystal Habit')
        self.assertNotContains(response2, 'Strunz Classification')

        # Properly raise 404
        self.assertEqual(response3.status_code, 404)

        # Ignores _state
        self.assertNotContains(response, '_state')

