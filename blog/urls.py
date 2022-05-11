from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('create_post/', views.create_user_post, name='create_post'),
    path('update_post/<post_id>', views.update_user_post, name='update_post'),
    path('delete_post/<post_id>', views.delete_post, name='delete_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
