from django.shortcuts import render
from responseapp.forms import MyForm
from django.template import loader
from django.http import HttpResponse
from operator import itemgetter
from responseapp.predictions import *




def preProcess(arr):
    a=[]
    b=arr[0]
    arr=arr[1:]
    final=[]
    for i in range(0,len(arr)):
       if(arr[i] is not None):
            if(arr[i][1] is not None and arr[i][0] is not None):
                a.append(arr[i])
            else:
                continue
    a=sorted(a, key=itemgetter(0))
    for i in range(0,len(a)):
        if(a[i][2]=='Kilograms'):
            a[i][1]=a[i][1]/1000
            a[i][2]='Tonnes'
        if(i>0):
            a[i][1]+=a[i-1][1]
    
    for i in range(0,len(a)-1):
        if((a[i][0]+1)!=a[i+1][0]):
            final.append(a[i])
            for j in range(1,(a[i+1][0]-a[i][0])):
                final.append([a[i][0]+j,a[i][1],a[i][2]])
        else:
            final.append(a[i])
    final.append(a[len(a)-1])
    final.append(b)
    return final





     

def responseform(request):
 #if form is submitted
     if request.method == 'POST':
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            type1=request.POST.get('type1')
            name1 = myForm.cleaned_data['year1']
            email1 = myForm.cleaned_data['quantity1']
            feedback1 = myForm.cleaned_data['metric1']
            name2 = myForm.cleaned_data['year2']
            email2 = myForm.cleaned_data['quantity2']
            feedback2 = myForm.cleaned_data['metric2']
            name3 = myForm.cleaned_data['year3']
            email3 = myForm.cleaned_data['quantity3']
            feedback3 = myForm.cleaned_data['metric3']
            name4 = myForm.cleaned_data['year4']
            email4 = myForm.cleaned_data['quantity4']
            feedback4 = myForm.cleaned_data['metric4']
            name5 = myForm.cleaned_data['year5']
            email5 = myForm.cleaned_data['quantity5']
            feedback5 = myForm.cleaned_data['metric5']
            type2='None'
            type3='None'
            context = {
            'type1':type1,
            'name1': name1,
            'email1': email1,
            'feedback1': feedback1,
            'name2': name2,
            'email2': email2,
            'feedback2': feedback2,
            'name3': name3,
            'email3': email3,
            'feedback3': feedback3,
            'name4': name4,
            'email4': email4,
            'feedback4': feedback4,
            'name5': name5,
            'email5': email5,
            'feedback5': feedback5
            }
            measure=[[type1,type2,type3],
                      [name1,email1,feedback1],
                      [name2,email2,feedback2],
                      [name3,email3,feedback3],
                      [name4,email4,feedback4],
                      [name5,email5,feedback5]]
            
            initial_data=preProcess(measure)
            print (initial_data)
            length=len(initial_data)
            if(type1=='Clothes'):
                 c=cloth()
                 final_data=c.predictions(initial_data[:length-1])
                 c.visualize()
            """
            if(type1=='School_material'):
                 final_data=predictions(initial_data)
            if(type1=='Electronics'):
                 final_data=predictions(initial_data)
            if(type1=='Utensils'):
                 final_data=predictions(initial_data)
            if(type1=='Footwear'):
                 final_data=predictions(initial_data)
            if(type1=='Paper'):
                 final_data=predictions(initial_data)
            if(type1=='Dry_Ration'):
                 final_data=predictions(initial_data)
            if(type1=='Toys'):
                 final_data=predictions(initial_data)
            """     
            raavay=initial_data[length-1][0]
            print(raavay)
            if(raavay=='Clothes'):
                 context = {
                 'type1':type1,
                 'name1': name1,
                 'email1': email1,
                 'feedback1': feedback1,
                 'name2': name2,
                 'email2': email2,
                 'feedback2': feedback2,
                 'name3': name3,
                 'email3': email3,
                 'feedback3': feedback3,
                 'name4': name4,
                 'email4': email4,
                 'feedback4': feedback4,
                 'name5': name5,
                 'email5': email5,
                 'feedback5': feedback5,
                 'val': initial_data[length-1][1],
                 'val1':final_data[0],
                 'val2':final_data[1],
                 'val3':final_data[2],
                 'val4':final_data[3],
                 'val5':final_data[4],
                 'val6':final_data[5],
                 'val7':final_data[6],
                 'val8':'Negotiable'
                 
                 }
                 
                 template = loader.get_template('prediction-Cloth.html')
            #template = loader.get_template('thankyou.html')
            return HttpResponse(template.render(context, request))



     else:
         form = MyForm()

     return render(request, 'responseform.html', {'form':form});
