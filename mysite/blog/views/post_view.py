from django.http import HttpResponse
from django.views import View

class PostView(View):
    def get(self, request):
        return HttpResponse("Hello World")
