from django.shortcuts import render

# Create your views here.
def index(request):
    # images = Post.objects.all()
    # users = User.objects.all()
    # if request.method == 'POST':
    #     form = PostForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.user = request.user.profile
    #         post.save()
    #         return HttpResponseRedirect(request.path_info)
    # else:
    #     form = PostForm()
    #     comment_form = CommentForm()
    params = {
        # 'images': images,
        # 'form': form,
        # 'comment_form': comment_form,
        # 'users': users,

    }
    return render(request, 'index.html', params)
