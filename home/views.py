from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from django.views import View

# Create your views here.


class Home(View):
    def get(self, request):
        form = UserForm()
        return render(request, "home/home_page.html", {"form": form})

    def post(self, request):
        name = request.POST.get("name")
        age = request.POST.get("age")
        flag = request.POST.get("flag")
        return HttpResponse(
            f"<h1>Привет, {name}</h1>\n"
            f"<p>Тебе {age} лет?</p>"
            f"<p>Флаг имеет значене = {flag}</p>"
        )

class HomeWork(View):

    def get(self, request):
        return render(request, "homework/homework_page.html")

class HomeWork2(View):

    def get(self, request):
        return render(request, "homework2/index.html")
        
class HomeWork3(View):

    def get(self, request):
        return render(request, "homework3/homework3.html")