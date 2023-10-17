from django.views import generic as views


# Create your views here.

class WebView(views.TemplateView):
    template_name = 'index.html'
