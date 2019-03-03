from django.shortcuts import render
from responseapp.forms import MyForm
from django.template import loader
from django.http import HttpResponse
from operator import itemgetter
from responseapp.predictions import *











     

def responseform(request):
 #if form is submitted
     if request.method == 'POST':
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            type1=request.POST.get('type1')
            name1 = myForm.cleaned_data['year1']
            email1 = myForm.cleaned_data['quantity1']
            feedback1 = myForm.cleaned_data['metric1']
            type2=request.POST.get('type2')
            type3='None'
            print(type2)
            context = {
            'type1':type1,
            'name1': name1,
            'email1': email1,
            'feedback1': feedback1,
            'type2':type2
            }
            
            
            measure=[[type1,type2,type3],
                      [name1,email1,feedback1]]
            print(measure)
            if(type1=='Clothes'):
                 c=cloth()
                 initial_data=Cloth_Preprocessing(measure)
                 print (initial_data)
                 final_data=c.predictions(initial_data)
                 """
                 final_data[4]=final_data[4][0]
                 final_data[5]=final_data[5][0]
                 final_data[6]=final_data[6][0]
                 final_data[7]=final_data[7][0]
                 """
                 c.visualize()
                
                 context = {
                 'type1':type1,
                 'name1': name1,
                 'email1': email1,
                 'feedback1': feedback1,
                 'type2':type2,
                 'hira':final_data[0],
                 'val2':final_data[1],
                 'val3':final_data[2],
                 'val4':final_data[3],
                 'val5':final_data[4],
                 'val6':final_data[5],
                 'val7':final_data[6],
                 'val8':final_data[7]
                 
                 }
                
                 template = loader.get_template('prediction-Cloth.html')
            
                 return HttpResponse(template.render(context, request))
            if(type1=='Paper'):
                p=paper()
                final_data=p.predictions(measure)
                print(final_data)
                context={
                 'type1':type1,
                 'name1': name1,
                 'email1': email1,
                 'feedback1': feedback1,
                 'type2':type2,
                 'hira':final_data[0],
                 'val2':final_data[1],
                 'val3':final_data[2],
                 'val4':final_data[3]

                    }
                template = loader.get_template('prediction-Paper.html')
            
                return HttpResponse(template.render(context, request))
            if(type1=='Electronics'):
                final_data=E_waste_Preprocessing(measure)
                
                visualize(final_data)
                context={
                 'type1':type1,
                 'name1': name1,
                 'email1': email1,
                 'feedback1': feedback1,
                 'type2':type2,
                 'hira':final_data[0],
                 'val2':final_data[1],
                 'val3':final_data[2],
                 'val4':final_data[3],
                 'val5':final_data[4]

                    }
                template = loader.get_template('prediction-Electronics.html')
                return HttpResponse(template.render(context, request))
           

     else:
         form = MyForm()

         return render(request, 'responseform.html', {'form':form});
