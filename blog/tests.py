from django.test import TestCase
from django.urls import reverse
 #  from .models import Post  # предполагается, что есть модель Post

class BlogTests(TestCase):
    def test_blog_index_status_code(self):
        url = reverse('blog:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
#    def test_blog_post_detail_status_code(self):

 #       # Создаем тестовый пост
  #      post = Post.objects.create(
   #         title='Test Post',
    #        content='Test content',
     #       
  #      )
   #     url = reverse('blog:post_detail', args=[post.id])
    #    response = self.client.get(url)
     #   self.assertEqual(response.status_code, 200)
