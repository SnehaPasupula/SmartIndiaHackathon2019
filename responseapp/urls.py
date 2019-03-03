from django.urls import path
from django.contrib import admin


from responseapp import views as responseapp_views

urlpatterns = [
 path('home/',responseapp_views.responseform),
 path('response/', responseapp_views.responseform),
 path('prediction-Cloth/',responseapp_views.responseform),
 path('prediction-Paper/',responseapp_views.responseform),
 path('prediction-Electronics/',responseapp_views.responseform),
 path('thankyou/', responseapp_views.responseform),

path('', admin.site.urls),
]
#<table>
#    {{form.as_table}}

# </table>
