from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.authtoken import views as rest_views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'posts/(?P<id>\d+)/comments',
                views.CommentViewSet, basename='comment')


urlpatterns = [
    path('api-token-auth/', rest_views.obtain_auth_token),
    path('', include(router.urls))
]
