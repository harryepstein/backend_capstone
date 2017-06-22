from django.conf.urls import url
from thesleeptrackerapp.views import index, morning_diary, evening_diary, register, login_user, user_logout

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^morning_diary$', morning_diary, name='morning_diary'),
    url(r'^evening_diary$', evening_diary, name='evening_diary'),
    url(r'^register$', register, name='register'),
    url(r'^login$', login_user, name='login'),
    url(r'^logout$', user_logout, name='logout'),
]
