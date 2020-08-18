from django.shortcuts import render, HttpResponseRedirect, reverse
from cowsay_app.models import text_input
from cowsay_app.forms import InputTextForm
import subprocess

def index_view(request):
    if request.method == "POST":
        
        form = InputTextForm(request.POST)
        form.save()
        form = InputTextForm
        process = subprocess.run(['cowsay', request.POST.get('text')], capture_output=True, shell=True).stdout.decode()

        return render(request, "index.html", {"form": form, "cowsay": process})
    
    form = InputTextForm()
    return render(request, "index.html", {"form": form})


def history_view(request):
    data = text_input.objects.all().order_by('-id')[:10]
    return render(request, 'history.html', {'cowsay': data})