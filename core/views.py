from django.shortcuts import render
import matplotlib.pyplot as plt
import os
from django.conf import settings
from .models import SalarioMinimos

from django.views.generic import TemplateView, ListView
from .forms import Calculadora

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
    

class FinanzasPageView(TemplateView, ListView):
    """ Clase para mostrar la página finanzas """
    template_name = 'core/finanzas.html'
    model = SalarioMinimos

    def get(self, request, *args, **kwars):
        """ Graficcamos """
        datos = SalarioMinimos.objects.all()            # Traigo toda la tabla
        anios = [dato.anio for dato in datos]
        varianza = [dato.variacion for dato in datos]

        plt.figure(figsize=(10,5))
        plt.plot(anios, varianza, marker = 'o', label = 'Variación %')
        plt.xlabel('Años')
        plt.ylabel('Varianza')
        plt.title('Varianza por año del Salario Minimo')
        plt.legend()
        plt.grid()

        # Ruta de la carpeta static donde se guardará la imagen
        static_dir = os.path.join(settings.STATICFILES_DIRS[0], 'img')
        os.makedirs(static_dir, exist_ok=True)  # Asegúrate de que la carpeta exista

        # Guarda el gráfico en la carpeta static
        image_path = os.path.join(static_dir, 'grafico_salario_minimo.png')
        plt.savefig(image_path)
        plt.close()

        return render(request, self.template_name, {
                                                    "titulo": 'Titulo del Articulo',
                                                    'grafico': f'img/grafico_salario_minimo.png'
                                                    })


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
    formulario = Calculadora()

    def get(self, request, *args, **kwars):
        return render(request, self.template_name, {
            'formulario': self.formulario
        })
    
    def mi_vista_humanize(request):
        context = { 
            'netoapagar'
        }
    
    def post(self, request, *args, **kwargs):

        formulario = Calculadora(data=request.POST)  # Crear el formulario con los datos enviados
        
        if formulario.is_valid():
            # Obtén los datos validados
            salario = formulario.cleaned_data.get('salario', 0)
            dias = formulario.cleaned_data.get('dias', 0)

            # Convertir a entero
            salario = int(salario)
            dias = int(dias)

            # Variables y operaciones
            
            mes = 30
            salario_dias = salario / mes * dias
            
            if salario <= 2850000 :
                transporte = 200000
                total_devengado = salario_dias + transporte
            if salario >= 5700000:
                transporte = 0
                solidario = 0.01
                total_devengado = salario_dias
            else:
                transporte = 0
                total_devengado = salario_dias
                solidario = 0

            salud = salario_dias * 0.04
            pension = salario_dias * 0.04
            bono_solidario = solidario * total_devengado
            base_gravada = total_devengado - (salud + pension + bono_solidario)

            if base_gravada * 0.25 < 3278434:
                renta_excenta = base_gravada * 0.25
            else:
                renta_excenta = 3278434

            base_retefuente = base_gravada - renta_excenta
            base_retefuenteuvt = base_retefuente / 49799

            
           
            if 0 < base_retefuenteuvt <= 95:
                 retefuenteuvt = 0
            if 95 < base_retefuenteuvt <= 150:
                retefuenteuvt = (base_retefuenteuvt - 95) * 0.19
            elif 150 < base_retefuenteuvt <= 360:
                retefuenteuvt = (base_retefuenteuvt - 150) * 0.28 + 10
            else:
                retefuenteuvt = (base_retefuenteuvt - 360) * 0.33 + 69
                
            if salario >= 4730905 :
                retefuentepesos = round(retefuenteuvt * 49799 / 1000) * 1000
            else:
                retefuentepesos = 0
                
            
            netoapagar = base_gravada - retefuentepesos
           
           
        

            

            # print(netoapagar, salario, dias)

            # Renderiza la plantilla con el resultado
            return render(request, self.template_name, {
                'formulario': formulario,
                'resultado': netoapagar,
                'transporte': transporte,
                'solidario': bono_solidario,
                'retefuente':retefuentepesos,
                'salud': salud,
                'pension': pension,
                'baseGravada': base_gravada,
                
            })

        # Si el formulario no es válido, renderiza nuevamente con los errores
        return render(request, self.template_name, {'formulario': formulario})
        

class AprendePageView(TemplateView):
    template_name = 'core/aprende.html'

    # dict_context = {
    
    # }

    def get(self, request, *args, **kwars):
        return render(request, self.template_name)