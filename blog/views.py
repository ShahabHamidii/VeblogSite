from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from blog.models import Post, Comment, Message, Like
from .forms import MessageForm
from django.views.generic import ListView, FormView, UpdateView, DeleteView, DetailView
from accounts.models import Profile
from django.urls import reverse_lazy


def post_detail(request, pk):

    post = get_object_or_404(Post.objects.filter(status=True), id=pk)
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to comment.")
            return redirect("accounts:login")

        parent_id_raw = request.POST.get("parent_id", "").strip()
        body = (request.POST.get("body") or "").strip()

        if not body:
            messages.error(request, "Comment cannot be empty.")
            return redirect("blog:post_detail", pk=pk)

        parent_id = None
        if parent_id_raw.isdigit():
            parent_id = int(parent_id_raw)

        Comment.objects.create(
            content=body,
            post=post,
            author=request.user,
            parent_id=parent_id,
        )

        return redirect("blog:post_detail", pk=pk)

    # Add like information
    if request.user.is_authenticated:
        post.is_liked = Like.objects.filter(user=request.user, post=post).exists()
    else:
        post.is_liked = False

    return render(request, "blog/post_details.html", {"post": post, "parent_id": ""})

def post_list(request):
    posts = Post.objects.published()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Add like information for each post
    for post in page_obj:
        if request.user.is_authenticated:
            post.is_liked = Like.objects.filter(user=request.user, post=post).exists()
        else:
            post.is_liked = False

    return render(request, "blog/blog_entries.html", {"posts": page_obj})


def search(request):
    q = (request.GET.get('q') or "").strip()
    all_posts = Post.objects.published()
    if q:
        all_posts = all_posts.filter(title__icontains=q)
    else:
        all_posts = all_posts.none()
    paginator = Paginator(all_posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Add like information for each post
    for post in page_obj:
        if request.user.is_authenticated:
            post.is_liked = Like.objects.filter(user=request.user, post=post).exists()
        else:
            post.is_liked = False

    return render(request, "blog/blog_entries.html", {"posts": page_obj})

class ProfileList(ListView):
    queryset = Profile.objects.all()
    template_name = "blog/user.html"


class ContactUsView(FormView):
    template_name = "blog/contactus.html"
    form_class = MessageForm
    success_url = "/"

    def form_valid(self, form):
        form_data = form.cleaned_data
        Message.objects.create(**form_data)
        return super().form_valid(form)

class MessageList(ListView):
    queryset = Message.objects.all()

class MessageUpdateView(UpdateView):
    model = Message
    fields = ["title", "content"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("blog:messages_list")

class MessageDeleteView(DeleteView):
    model = Message
    template_name_suffix = "_delete_form"
    success_url = reverse_lazy("blog:messages_list")

def like(request, pk):
    if not request.user.is_authenticated:
        return JsonResponse({"response": "error", "message": "Please login first"})
    
    post = get_object_or_404(Post, pk=pk)
    
    try:
        like_obj = Like.objects.get(user=request.user, post=post)
        like_obj.delete()
        return JsonResponse({
            "response": "unliked", 
            "count": post.likes.count()
        })
    except Like.DoesNotExist:
        Like.objects.create(user=request.user, post=post)
        return JsonResponse({
            "response": "liked", 
            "count": post.likes.count()
        })


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        if self.request.user.is_authenticated:
            context["is_liked"] = Like.objects.filter(user=self.request.user, post=post).exists()
        else:
            context["is_liked"] = False
        return context

