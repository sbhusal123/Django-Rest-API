from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views

"""
Default Router: generates the urls automatically
""" # noqa

router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredient', views.IngredientViewSet)
router.register('recipe', views.RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
