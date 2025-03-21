from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class HomepageView(TemplateView):

    #muestreme en la pantalla lo que tiene el diccionario de contexto
    template_name = 'core/index.html'


    navbar ={

        'inicio': 'Inicio',
        'finanzas': 'Sobre finanzas',
        'aprende': 'Aprende',
        'calculadora': 'Tu calculadora',
        'nosotros': 'Nosotros',
    }

    

    #Metodo que se encarga de devolver la vista
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.navbar)
    

class FinanzasPageView(TemplateView):
    """ Clase para mostrar la página finanzas """
    template_name = 'core/finanzas.html'

    dict_context = {
        "titulo": 'Titulo del Articulo'
    }

    def get(self, request, *args, **kwars):
        return render(request, self.template_name, self.dict_context)


class NosotrosPageView(TemplateView):
    template_name = 'core/nosotros.html'

    dict_context = {
        "dev_juan" : 'Juan David Garcia',
        "dev_yulieth" : ' Yulieth Moreno Caballero',
        "dev_larla" : 'Laura Galeano',
        "dev_paula" : 'Paula Martinez',
    }

    def get(self, request, *args, **kwars):
        return render(request, self.template_name, self.dict_context)
    

class CalculadoraPageView(TemplateView):
    template_name = 'core/calculadora.html'

    # dict_context = {
    
    # }

    def get(self, request, *args, **kwars):
        return render(request, self.template_name)
    

class AprendePageView(TemplateView):
    template_name = 'core/aprende.html'

    # dict_context = {
    
    # }

    def get(self, request, *args, **kwars):
        return render(request, self.template_name)