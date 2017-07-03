from django.test import TestCase,RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from calpetrol.views import home_page


class HomePageTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='test', email='test@example.com', password='top_secret')

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/login/')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = home_page(request)
        self.assertEqual(response.status_code, 200)

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'calpetrol/home1.html')
