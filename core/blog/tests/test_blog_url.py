from django.test import TestCase , SimpleTestCase     #Testcase for work in database
from django.urls import reverse , resolve
from ..views import Indexview , PostDetailView , PostlistView
# Create your tests here.

class TestUrl(SimpleTestCase):
    
    def test_blog_url_index_resolve(self):
        url = reverse('blog:fbv-index')
        self.assertEqual(resolve(url).func.view_class , Indexview)
        
    def test_blog_post_detail_url_resolve(self):
        url = reverse('blog:post-detail',kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class , PostDetailView)
        
    def test_blog_post_list_url_resolve(self):
        url = reverse('blog:post-list')
        self.assertEqual(resolve(url).func.view_class , PostlistView)