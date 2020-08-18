from django.shortcuts import render, HttpResponseRedirect, reverse
from cowsay_app.models import input_text
from cowsay_app.forms import InputTextForm
import subprocess

def index_view(request):
    if request.method == "POST":
        form = InputTextForm(request.POST)
        form.save()
        form_text = request.POST.get('text')
        process = subprocess.run(['cowsay', form_text], capture_output=True, shell=True)
        process = process.stdout.decode()
        form = InputTextForm
        return render(request, "index.html", {"form": form, "process": process})
    form = InputTextForm()
    return render(request, "index.html", {"form": form})