from django.conf.urls import url
import thesleeptrackerapp.views

urlpatterns = [
    url(r'^$', thesleeptrackerapp.views.index, name='index'),
]
