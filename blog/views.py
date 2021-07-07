from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post, Comment


def home(request):
    return render(request, 'home.html')


def my_post(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, 'myPost.html', {"post_list":posts})
    return redirect('/account/login')


    

def new_post(request):
    if request.method == 'POST':
        if request.FILES.get('image'):
            # 객체 생성
            Post.objects.create(
                title = request.POST['title'],
                body = request.POST['body'],
                image = request.FILES['image']
            )
            # 객체를 생성하는 가운데 레포들을 각각 직접 가져와서
            # post라는 이름으로 저장
        else:
            Post.objects.create(
                title = request.POST['title'],
                body = request.POST['body'],
            )
        post_list = Post.objects.all()
        return render(request, 'myPost.html', {'post_list':post_list})
    return redirect('/')

def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'postDetail.html', {'post':post})


def post_update(request, pk):
    post =Post.objects.get(id=pk)

    if request.method == 'POST':
        title = request.POST['title'],
        body = request.POST['body'],
        image = request.FILES['image']
        post.title = title
        post.body = body
        post.image = image
        post.save()
        return redirect('/post/'+ str(post.id))
    else:
        return render(request, 'editPost.html', {'post':post})


def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/my-post/')


def comment_write(request, pk):
    if request.method =="POST":
        comment = Comment()
        comment.comment_writer = request.user
        comment.post = get_object_or_404(Post, id=pk)
        comment.comment_contents = request.POST.get('content')
        comment.save()
        return redirect('/post/' + str(pk))

def comment_delete(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return redirect('/my-post/')


def comment_update(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.comment_contents = request.POST.get('content2')
    comment.save()
    return redirect('/my-post/')