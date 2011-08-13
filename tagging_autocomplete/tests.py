from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import simplejson

class TaggingAutocompleteViewTest(TestCase):
    urls = 'tagging_autocomplete.urls'

    def test_no_term(self):
        """
        test view list_tags without submitting a term
        """
        response = self.client.get(reverse('tagging_autocomplete-list'))
        data = simplejson.loads(response.content)
        self.assertEqual(data, [])
