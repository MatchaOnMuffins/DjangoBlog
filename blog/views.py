from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post, Comments
from .forms import PostForm, EditForm, AddComment


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'
    context_object_name = 'post'
    slug_field = 'url'
    slug_url_kwarg = 'post_url'


# create a new post
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # fields = ('title', 'title_tag', 'content','author')


class PostUpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'
    # fields = ('title', 'title_tag', 'content')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class CommentCreateView(CreateView):
    model = Comments
    form_class = AddComment
    context_object_name = 'comments'
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post = Post.objects.get(id=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    # fields = "__all__"
    # fields = ('title', 'title_tag', 'content','author')


class CommentUpdateView(UpdateView):
    model = Comments
    form_class = AddComment
    template_name = 'edit_comment.html'


class CommentDeleteView(DeleteView):
    model = Comments
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('home')
