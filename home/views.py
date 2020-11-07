from django.shortcuts import render
import requests
from django.views.generic import TemplateView
import json

class HomePageView(TemplateView):
    template = "home/home_page.html"

    def get(self,*args, **kwargs):
        api_call = requests.get("https://hamyarandroid.com/api?t=currency").json()
        return render(self.request, self.template, {"coins": json.dumps(api_call)})