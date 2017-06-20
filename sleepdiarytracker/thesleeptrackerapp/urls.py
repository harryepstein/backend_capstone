from django.conf.urls import url
from thesleeptrackerapp.views import index, morning_diary, evening_diary, bokeh

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^morning_diary$', morning_diary, name='morning_diary'),
    url(r'^evening_diary$', evening_diary, name='evening_diary'),
    url(r'^bokeh$', bokeh, name='bokeh'),
]
