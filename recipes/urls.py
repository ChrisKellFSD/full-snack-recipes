from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('recipe_detail/<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('add_recipe/', login_required(views.AddRecipe.as_view()), name='add_recipe'),
    path(
        'your_recipes/<slug:slug>/', views.UsersRecipeList.as_view(), name='your_recipes'
        )
]
