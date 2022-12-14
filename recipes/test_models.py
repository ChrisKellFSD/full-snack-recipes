from django.test import TestCase
from django.contrib.auth.models import User
from .models import Comment, Recipe


class TestModels(TestCase):

    def test_recipe_model_str(self):
        author = User.objects.create(username='example_username')
        recipe = Recipe.objects.create(
            title='Example Recipe',
            slug='example-recipe',
            author=author,
            excerpt='This is an example recipe.',
            ingredients='This is an example ingredient.',
            method='This is an example method.'
            )
        self.assertEqual(str(recipe), 'Example Recipe')
        

    def test_can_create_comment(self):

        author = User.objects.create(username='example_username')
        recipe = Recipe.objects.create(
            title='Example Recipe',
            slug='example-recipe',
            author=author,
            excerpt='This is an example recipe.',
            ingredients='This is an example ingredient.',
            method='This is an example method.'
            )
    
        comment = Comment.objects.create(
            post=recipe,
            name='Example Commenter',
            email='example@example.com',
            body='This is an example comment.',
            )

        self.assertIsNotNone(comment.id)