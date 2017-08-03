# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"

class InternshipsPageView(TemplateView):
    template_name = "internships.html"

class VolunteeringPageView(TemplateView):
    template_name = "volunteering.html"

class AdvicePageView(TemplateView):
    template_name = "advice.html"

class ScholarshipsPageView(TemplateView):
    template_name = "scholarships.html"

class ProgramsPageView(TemplateView):
    template_name = "programs.html"
