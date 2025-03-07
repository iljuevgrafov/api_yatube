from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.authtoken import views as rest_views

router_v1 = DefaultRouter()
router_v1.register(r'posts', views.PostViewSet, basename='post')
router_v1.register(r'posts/(?P<id>\d+)/comments',
                   views.CommentViewSet, basename='comment')


urlpatterns = [
    path('v1/api-token-auth/', rest_views.obtain_auth_token),
    path('v1/', include(router_v1.urls))
]
