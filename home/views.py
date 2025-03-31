from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from allauth.account.views import SignupView, LoginView
from django.http import HttpResponseForbidden
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Comment, NewsletterSignup
from .forms import CommentForm, NewsletterSignupForm



from django.shortcuts import redirect

def redirect_authenticated_user(view_class):
    class WrappedView(view_class):
        def dispatch(self, request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect('home')
            return super().dispatch(request, *args, **kwargs)

    return WrappedView.as_view()


def index(request):
    comments = Comment.objects.all().order_by('-created_at')
    newsletter_form = NewsletterSignupForm()  # ← this was missing

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.save()
            return redirect('home')
    else:
        form = CommentForm()

    return render(request, 'home/index.html', {
        'comments': comments,
        'form': form,
        'newsletter_form': newsletter_form  # ← this was missing
    })

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    # Allow the comment author or an admin to delete
    if request.user == comment.user or request.user.is_staff:
        comment.delete()
        return redirect('home')  # Redirect to the homepage
    return HttpResponseForbidden("You are not allowed to delete this comment.")

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if comment.user != request.user and not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to edit this comment.")

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully.")
            return redirect('home')
    else:
        form = CommentForm(instance=comment)

    return render(request, 'home/edit_comment.html', {'form': form, 'comment': comment})


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /accounts/",
        "Disallow: /profiles/",
        "Disallow: /checkout/",
        "Disallow: /cart/",
        "Allow: /",
        f"Sitemap: https://{request.get_host()}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for signing up for our newsletter!")
            return redirect('home')
        else:
            messages.error(request, "Please enter a valid email address.")
    return redirect('home')
