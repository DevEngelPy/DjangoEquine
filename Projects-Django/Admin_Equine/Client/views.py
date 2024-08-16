from django.shortcuts import render
from Client.forms import ClientForm
# Create your views here.
def list_client(request):
    formulario = ClientForm()
    context = {'form':formulario}
    return render(request,'client/client.html', context)