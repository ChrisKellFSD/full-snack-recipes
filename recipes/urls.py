from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('all_recipes/', views.AllRecipeList.as_view(), name='all_recipes'),
    path('recipe_detail/<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('add_recipe/', login_required(views.AddRecipe.as_view()), name='add_recipe'),
    path('search_recipes/', views.search_recipes, name='search_recipes'),
    path('update_recipe/<slug:slug>/', login_required(views.UpdateRecipe.as_view()), name='update_recipe'),
    path('delete_recipe/<slug:slug>/', views.delete_recipe, name='delete_recipe'),
    path(
        'my_recipes/', views.UsersRecipeList.as_view(), name='my_recipes'
        )
]
