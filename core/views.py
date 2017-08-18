from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.views import generic
from .models import Post, User
from .forms import PostForm, CustomUserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin

def is_author(user):
		return user.groups.filter(name='author').exists()

class IndexView(generic.ListView):
	model = Post
	template_name = 'core/index.html'
	context_object_name = 'posts'

	def get_queryset(self):
		return Post.objects.all()


class CreateView(UserPassesTestMixin, generic.FormView):
	template_name = 'core/new.html'
	form_class = PostForm	
	login_url = '/'	
	success_url = '/'

	def test_func(self):
		return is_author(self.request.user)

	def form_valid(self, form):
		form.instance.posted_by = self.request.user
		form.instance.slug = slugify(form.instance.title)
		form.save()
		return super(CreateView, self).form_valid(form)



class SignUpView(generic.FormView):
	template_name = 'core/signup.html'
	form_class = CustomUserCreationForm
	success_url = '/'

	def form_valid(self, form):
		form.save()
		return super(SignUpView, self).form_valid(form)

	def dispatch(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('index')
		else:
			return super(SignUpView, self).dispatch(request, *args, **kwargs)

