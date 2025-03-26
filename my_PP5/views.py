import os
from django.http import HttpResponse
from django.conf import settings

def sitemap_view(request):
    sitemap_path = os.path.join(settings.BASE_DIR, 'templates', 'sitemap.xml')


    try:
        with open(sitemap_path, 'r') as f:
            xml_content = f.read()
        return HttpResponse(xml_content, content_type='application/xml')
    except FileNotFoundError:
        return HttpResponse("Sitemap not found.", status=404)

