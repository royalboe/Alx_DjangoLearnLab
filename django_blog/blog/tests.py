# blog/tests/test_views.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post

class PostPermissionsTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='pass12345')
        self.user2 = User.objects.create_user(username='user2', password='pass56789')
        self.post = Post.objects.create(title='T', content='C', author=self.user1)

    def test_edit_by_author(self):
        self.client.login(username='user1', password='pass12345')
        resp = self.client.get(reverse('blog:post-update', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 200)

    def test_edit_by_other(self):
        self.client.login(username='user2', password='pass56789')
        resp = self.client.get(reverse('blog:post-update', kwargs={'pk': self.post.pk}))
        # will redirect to detail due to handle_no_permission
        self.assertEqual(resp.status_code, 302)
