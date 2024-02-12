from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'blog/home.html'


class AboutPageView(TemplateView):
    template_name = 'blog/about.html'


class LoginPageView(TemplateView):
    template_name = 'blog/login.html'


class RegisterPageView(TemplateView):
    template_name = 'blog/register.html'


class PostConfirmDeleteView(TemplateView):
    template_name = 'blog/post_confirm_delete.html'


class NewPostView(TemplateView):
    template_name = 'blog/post_form.html'


class PostDetailView(TemplateView):
    template_name = 'blog/post_detail.html'


class UserPostView(TemplateView):
    template_name = 'blog/user_posts.html'


class Logout(TemplateView):
    template_name = 'blog/logout.html'
