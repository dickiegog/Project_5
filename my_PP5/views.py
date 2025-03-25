from django.http import HttpResponse

def sitemap_view(request):
    """Serve the static sitemap.xml file."""
    filepath = os.path.join(settings.BASE_DIR, 'static', 'sitemap.xml')
    with open(filepath, 'rb') as f:
        return HttpResponse(f.read(), content_type='application/xml')

def home(request):
    return HttpResponse("Hello, world! This is the home page.")
