from django.test import TestCase
from . models import Rating,Post,Profile
from django.contrib.auth.models import User

# Create your tests here.

class RatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='sekani')
        self.post = Post.objects.create(id=1, title='test post', image='https://ucarecdn.com/c0e1bb0a-9bab-47f1-b171-170d1e1b2b44/', 
                                        user=self.user, url='http://url.com')
        self.rating = Rating.objects.create(id=1, design=6, usability=7, content=9, user=self.user, post=self.post)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)

class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(id=1, username='sekani', password='yolo123!!!!')
        self.user.save()


    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()
        
class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='sekani')
        self.post = Post.objects.create(id=1, title='test post', image='https://ucarecdn.com/c0e1bb0a-9bab-47f1-b171-170d1e1b2b44/',
                                        user=self.user, url='http://url.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

   
    def test_search_post(self):
        self.post.save()
        post = Post.search_project('test')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.search_project('test')
        self.assertTrue(len(post) < 1)  