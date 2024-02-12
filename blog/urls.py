from django.contrib.auth.views import LogoutView
from django.urls import path

from blog.views import HomePageView, AboutPageView, PostDetailView, UserPostView, PostConfirmDeleteView, \
    LoginPageView, RegisterPageView, NewPostView

app_name = 'blog'
urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('login', LoginPageView.as_view(), name='login'),
    path('register', RegisterPageView.as_view(), name='register'),
    path('new-post', NewPostView.as_view(), name='new-post'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('about', AboutPageView.as_view(), name='about-page'),
    path('post/', PostDetailView.as_view(), name='post-detail'),
    path('user-post', UserPostView.as_view(), name='user-post'),
    path('post/confirm-delete', PostConfirmDeleteView.as_view(), name='post-confirm-delete'),
]