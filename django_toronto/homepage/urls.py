from django.conf.urls import url, patterns

from .views import HomepageView


urlpatterns = patterns('',
    url(r'^$', HomepageView.as_view(), name='home'),
)
