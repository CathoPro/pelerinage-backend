from django.shortcuts import render, redirect
from .forms import PelerinForm

def accueil(request):
    return render(request, "accueil.html")

def inscription(request):
    form = PelerinForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        pelerin = form.save()
        return redirect("recu", pelerin.id)
    return render(request, "inscription.html", {"form": form})

def paiement(request):
    return render(request, "paiement.html")

def recu(request, id):
    return render(request, "recu.html")

def felicitation(request):
    return render(request, "felicitation.html")

def dashboard(request):
    return render(request, "dashboard.html")

def boutique(request):
    return render(request, "boutique.html")
