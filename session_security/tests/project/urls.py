import time

from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ImproperlyConfigured
from django.views import generic

try:
    from django.conf.urls import patterns
except ImportError:
    patterns = None

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


class SleepView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        time.sleep(int(request.GET.get('seconds', 0)))
        return super(SleepView, self).get(request, *args, **kwargs)


try:
    admin_site_urls = include(admin.site.urls)
except ImproperlyConfigured:
    admin_site_urls = admin.site.urls

urlpatterns = [
    url(r'^$', generic.TemplateView.as_view(template_name='home.html')),
    url(r'^sleep/$', login_required(
        SleepView.as_view(template_name='home.html')), name='sleep'),
    url(r'^admin/', admin_site_urls),
    url(r'session_security/', include('session_security.urls')),
    url(r'^ignore/$', login_required(
        generic.TemplateView.as_view(template_name='home.html')), name='ignore'),
]

if patterns:
    urlpatterns = patterns('', *urlpatterns)
