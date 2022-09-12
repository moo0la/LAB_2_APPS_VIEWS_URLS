from django.http import HttpResponse 

def index(request):
   helomsg ="Hello World, This is my new HOME !" 
    return HttpResponse(helomsg)