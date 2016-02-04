from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView

from rest_framework import routers, serializers, viewsets

from polls.viewsets import ChoiceViewSet, PollViewSet
from polls.forms import ChoiceForm, PollForm

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'poll', PollViewSet)
router.register(r'choice', ChoiceViewSet)

admin.autodiscover()

react_urls = patterns('',
    url(r'^$', TemplateView.as_view(template_name='react/react.html'), {'poll_form': PollForm, 'choice_form': ChoiceForm}, name='react_index'),
)

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^react/', include(react_urls, namespace='react')),
)