from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):

    send_mail("Hola desde luisyaqu",
    "Hola!!. Este es un mensaje automático.",
    "luisyaqu_16@hotmail.com",
    ["lyanaa@unsa.edu.pe"],
    fail_silently=False)

    return render(request, "send/index.html")

