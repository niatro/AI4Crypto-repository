from django.shortcuts import render
from . import forms
# from forms import FormName

# Create your views here.

def index(request):
    return render(request,'IA4Crypto_app/index.html')

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form =forms.FormName(request.POST)
        if form.is_valid():
            # HACER ALGUNA COSA
            print("VALIDACION ACCES")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXTO: "+form.cleaned_data['text'])



    return render(request,'IA4Crypto_app/form_page.html',{'form':form})
