from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
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
            return redirect('home')  # Redirect to the index after saving
    else:
        form = CommentForm()
    return render(request, 'home/index.html', {'comments': comments, 'form': form})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    # Only allow admin users to delete
    if request.user.is_staff:
        comment.delete()
        return redirect('home')  # Redirect to the homepage
    return HttpResponseForbidden("You are not allowed to delete this comment.")
