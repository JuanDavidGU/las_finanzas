
from django.urls import path
from .views import HomepageView, FinanzasPageView, NosotrosPageView 

urlpatterns = [
    path('', HomepageView.as_view(), name= 'inicio'), 
    path('finanzas/', FinanzasPageView.as_view(), name = 'finanzas'),
    path('nosotros/', NosotrosPageView.as_view(), name = 'nosotros'),
]
