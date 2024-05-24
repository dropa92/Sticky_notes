from django.test import TestCase
from django.urls import reverse
from .models import Note,Post, Author
from .views import post_update

# Create your tests here.
class Note_model_test(TestCase):
 def setUp(self):
     
    # Create a note object for testing
    Note.objects.create(title='Test Note', content='This is mi first note')
    
    def test_note_has_title(self):
        # Test that a note object has the expected title
        note = Note.objects.get(id=1)
        self.assertEqual(post.title, 'Test Note')
    
    def test_note_has_content(self):
        # Test that a note object has the expected content
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is mi first note')
    

class Post_model_test(TestCase):
    def setUp(self):
        # Create an Author object
        author = Author.objects.create(name='Test Author')
        # Create a Post object for testing
        Post.objects.create(title='Test Post', content='This is a test post.', author=author)
    def test_post_has_title(self):
        # Test that a Post object has the expected title
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Test Post')
    def test_post_has_content(self):
        # Test that a Post object has the expected content
        post = Post.objects.get(id=1)
        self.assertEqual(post.content, 'This is a test post.')


class Post_view_test(TestCase):
    def setUp(self):
        # Create an Author object
        author = Author.objects.create(name='Test Author')
        # Create a Post object for testing views
        Post.objects.create(title='Second test post', content='This is the second test post', author=author)
    
    def test_post_list_view(self):
        # Test the post-list view
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Second test post')
    
    def test_post_detail_view(self):
        # Test the post-detail view
        post = Post.objects.get(id=1)
        response = self.client.get(reverse('post_detail',
        args=[str(post.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Second test post')
        self.assertContains(response, 'This is the second test post')
    
    
    def test_post_update(self):
        # Test the updated post
        post = Post.objects.get(id=1)
        
        new_content = "New content to my post"
        response = self.client.post(reverse('post_update', args=[post.pk]), {
            'title': post.title,
            'content': new_content,
            'author': 'Test Author'
        })
        
        
        post = Post.objects.get(id=1)
       
        
        self.assertEqual(response.status_code, 302)
        
        
        self.assertEqual(post.content, new_content)
        
    
    def test_post_delete(self):
        # Test the post deleted from the database
        post = Post.objects.get(id=1)
        response = self.client.post(reverse('post_delete', args=[post.pk]))
        self.assertEqual(response.status_code, 302)