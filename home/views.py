from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

def index(request):
    comments = Comment.objects.all().order_by('-created_at')  # Show comments in reverse chronological order
    if request.method == 'POST':  # Handle form submissions
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user  # Assign the logged-in user
            new_comment.save()
            return redirect('index')  # Redirect to the index after saving
    else:
        form = CommentForm()
    return render(request, 'home/index.html', {'comments': comments, 'form': form})
