# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /volunteering/ route
    url(r'^internships/$', views.InternshipsPageView.as_view()),
    url(r'^scholarships/$', views.ScholarshipsPageView.as_view()),
    url(r'^volunteering/$', views.VolunteeringPageView.as_view()),
    url(r'^advice/$', views.AdvicePageView.as_view()),
    url(r'^programs/$', views.ProgramsPageView.as_view()),
]
