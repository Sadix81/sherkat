from django.shortcuts import render , redirect , get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request , 'post/index.html' , {'posts' : posts})


def userpost(request):
    posts = Post.objects.filter(user = request.user)
    return render(request , 'post/user_posts.html' , {'posts':posts})


@login_required
def create(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Set the logged-in user as the post's user
            form.save()
            return redirect('post-index')
    else:
        form = PostForm()
    return render(request, 'post/create.html', {'form': form})
    

def update(request , pk):
    post = get_object_or_404(Post , pk=pk)
    if request.method == 'POST' :
        form = PostForm(request.POST , request.FILES , instance=post)
        if form.is_valid() :
            form.save()
            return redirect('posts-user' , pk = post.pk)
    else :
        form = PostForm(instance=post)
    return render(request, 'post/user_posts.html', {'form': form})




