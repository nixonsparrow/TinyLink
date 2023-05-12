from rest_framework.test import APITestCase
from django.urls import reverse
from manager.models import Link


class LinksBaseAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.links_url = reverse("links")
        self.valid_data = {"original": "http://google.com"}


class LinksGETTestCase(LinksBaseAPITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.get_response = self.client.get(self.links_url)

    def test_get_link_list_in_json(self):
        self.assertEqual(self.get_response.status_code, 200)
        self.assertEqual(self.get_response.data, [])

    def test_get_link_list_in_json_count_before_and_after_adding_new_link(self):
        self.assertEqual(len(self.get_response.data), 0)

        self.client.post(self.links_url, data=self.valid_data, format="json")
        response = self.client.get(self.links_url)

        self.assertEqual(len(response.data), 1)
        self.assertIn("('id', 1)", response.data.__str__())
        self.assertIn("'original', 'http://google.com')", response.data.__str__())


class LinksSpecificGETTestCase(LinksBaseAPITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.client.post(self.links_url, data=self.valid_data, format="json")

    def test_if_link_redirects(self):
        response = self.client.get(self.links_url + Link.objects.get(id=1).short)

        self.assertEqual(response.status_code, 301)

    def test_if_link_redirects_properly(self):
        link = Link.objects.get(id=1)
        response = self.client.get(self.links_url + link.short, follow=True)
        short_used = str(response.redirect_chain[0][0]).replace("/", "")
        redirected_to = str(response.redirect_chain[1][0])

        self.assertEqual(short_used, link.short)
        self.assertEqual(redirected_to, link.original)


class LinksPOSTTestCase(LinksBaseAPITestCase):
    def test_links_post_add_link_to_database(self):
        self.client.post(self.links_url, data=self.valid_data, format="json")

        self.assertEqual(len(self.client.get(self.links_url).data), 1)
        self.assertEqual(Link.objects.all().count(), 1)

    def test_if_not_able_to_post_without_original_data(self):
        response = self.client.post(self.links_url, data={"xxx": "yyy"}, format="json")

        self.assertEqual(response.status_code, 400)
