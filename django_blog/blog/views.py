from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post
from .forms import PostForm
from .models import Comment
from .forms import CommentForm
from django.db.models import Q
from .models import Post, Comment, Tag
from .forms import PostForm, CommentForm



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'blog/register.html'

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # creates the user
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect("login")  # or wherever you want to redirect
    else:
        form = UserCreationForm()

    return render(request, "blog/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = 'blog/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'


@login_required
def profile(request):
    # defensive: ensure profile exists
    if not hasattr(request.user, 'profile'):
        Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile was updated successfully.')
            return redirect('blog:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'blog/profile.html', context)

# --- Post CRUD views ---

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # blog/templates/blog/post_list.html
    context_object_name = 'posts'
    paginate_by = 10  # optional: paginate 10 posts per page


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        # set author to logged-in user
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Post created successfully.')
        return response

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.object.pk})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        # ensure author remains unchanged
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Post updated successfully.')
        return response

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def handle_no_permission(self):
        messages.error(self.request, 'You do not have permission to edit this post.')
        return redirect('blog:post-detail', pk=self.get_object().pk)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def handle_no_permission(self):
        messages.error(self.request, 'You do not have permission to delete this post.')
        return redirect('blog:post-detail', pk=self.get_object().pk)

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'  # fallback page; we will also post from post_detail inline

    def dispatch(self, request, *args, **kwargs):
        # ensure post exists
        self.post = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.post
        response = super().form_valid(form)
        messages.success(self.request, 'Your comment was added.')
        return response

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.post.pk})

    # if user POSTS the comment inline from post_detail, the CreateView will still accept it because it expects POST to this URL


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your comment was updated.')
        return response

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def handle_no_permission(self):
        messages.error(self.request, 'You do not have permission to edit this comment.')
        return redirect('blog:post-detail', pk=self.get_object().post.pk)

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def handle_no_permission(self):
        messages.error(self.request, 'You do not have permission to delete this comment.')
        return redirect('blog:post-detail', pk=self.get_object().post.pk)

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.object.post.pk})
    




# --- Posts ---

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        # set author
        form.instance.author = self.request.user
        # save Post first (but don't commit tags yet)
        response = super().form_valid(form)

        # process tags from the form
        tag_string = form.cleaned_data.get('tags', '')
        tag_objs = []
        if tag_string:
            tag_names = [t.strip() for t in tag_string.split(',') if t.strip()]
            for name in tag_names:
                tag_obj, created = Tag.objects.get_or_create(name__iexact=name, defaults={'name': name})
                # Tag.objects.get_or_create doesn't accept name__iexact in get params, so use try/except for case-insensitive uniqueness:
                # We'll implement case-insensitive get_or_create below to be safe
            # Corrected processing below (case-insensitive)
        # Re-implemented safely:
        if tag_string:
            tag_names = [t.strip() for t in tag_string.split(',') if t.strip()]
            for name in tag_names:
                tag_obj = Tag.objects.filter(name__iexact=name).first()
                if not tag_obj:
                    tag_obj = Tag.objects.create(name=name)
                tag_objs.append(tag_obj)

        if tag_objs:
            self.object.tags.set(tag_objs)

        messages.success(self.request, 'Post created successfully.')
        return response

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.object.pk})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        # Ensure the author remains the logged-in user (or keep original)
        form.instance.author = self.request.user
        response = super().form_valid(form)

        # process tags: replace post.tags with provided tags
        tag_string = form.cleaned_data.get('tags', '')
        tag_objs = []
        if tag_string:
            tag_names = [t.strip() for t in tag_string.split(',') if t.strip()]
            for name in tag_names:
                tag_obj = Tag.objects.filter(name__iexact=name).first()
                if not tag_obj:
                    tag_obj = Tag.objects.create(name=name)
                tag_objs.append(tag_obj)

        # set tags (if none provided, clear them)
        self.object.tags.set(tag_objs)
        messages.success(self.request, 'Post updated successfully.')
        return response

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def handle_no_permission(self):
        messages.error(self.request, 'You do not have permission to edit this post.')
        return redirect('blog:post-detail', pk=self.get_object().pk)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def handle_no_permission(self):
        messages.error(self.request, 'You do not have permission to delete this post.')
        return redirect('blog:post-detail', pk=self.get_object().pk)


# --- Tags and Search ---

class TagPostListView(ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, name__iexact=self.kwargs.get('tag_name'))
        return self.tag.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context


class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()
        if not query:
            return Post.objects.none()
        # search title OR content OR tag name (case-insensitive)
        queryset = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
