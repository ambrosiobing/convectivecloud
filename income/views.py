import os
import pickle
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from income.models import Adult
from income.serializers import AdultSerializer
from income.forms import AdultForm
import sklearn
import pandas as pd

def tuple2dict(tuple_object):
    return [{x:y} for x, y in tuple_object]

age_choices = tuple2dict(Adult.AGE_CHOICES)
edu_choices = tuple2dict(Adult.EDU_CHOICES)
num_choices = tuple2dict(Adult.NUM_CHOICES)
sta_choices = tuple2dict(Adult.STA_CHOICES)
occ_choices = tuple2dict(Adult.OCC_CHOICES)
rel_choices = tuple2dict(Adult.REL_CHOICES)
rac_choices = tuple2dict(Adult.RAC_CHOICES)
sex_choices = tuple2dict(Adult.SEX_CHOICES)
hrs_choices = tuple2dict(Adult.HRS_CHOICES)

all_data = {
    'age':age_choices,
    'edu':edu_choices,
    'num':num_choices,
    'sta':sta_choices,
    'occ':occ_choices,
    'rel':rel_choices,
    'rac':rac_choices,
    'sex':sex_choices,
    'hrs':hrs_choices}

def create_new_tuple(tup_pair_old):
    inside = tup_pair_old
    print(inside)
    if inside[0]=='age': return [('age',int(inside[1]))]
    elif inside[0]=='education':
        if inside[1]=='Preschool': return [('education',0)]
        elif inside[1]=='1st-4th': return [('education',1)]
        elif inside[1]=='5th-6th': return [('education',2)]
        elif inside[1]=='7th-8th': return [('education',3)]
        elif inside[1]=='9th': return [('education',4)]
        elif inside[1]=='10th': return [('education',5)]
        elif inside[1]=='11th': return [('education',6)]
        elif inside[1]=='12th': return [('education',7)]
        elif inside[1]=='HS-grad': return [('education',8)]
        elif inside[1]=='Some-college': return [('education',9)]
        elif inside[1]=='Assoc-voc': return [('education',10)]
        elif inside[1]=='Prof-school': return [('education',11)]
        elif inside[1]=='Assoc-acdm': return [('education',12)]
        elif inside[1]=='Bachelors': return [('education',13)]
        elif inside[1]=='Masters': return [('education',14)]
        elif inside[1]=='Doctorate': return [('education',15)] 
    if inside[0]=='years_education': return [('years_education',int(inside[1]))]
    elif inside[0]=='marital_status':
        if inside[1]=='Married-spouse-absent': return [('marital_status',0)]
        elif inside[1]=='Widowed': return [('marital_status',1)]
        elif inside[1]=='Married-civ-spouse': return [('marital_status',2)]
        elif inside[1]=='Separated': return [('marital_status',3)]
        elif inside[1]=='Divorced': return [('marital_status',4)]
        elif inside[1]=='Never-married': return [('marital_status',5)]
        elif inside[1]=='Married-AF-spouse': return [('marital_status',6)]
    elif inside[0]=='occupation':
        if inside[1]=='?': return [('occupation',0)]
        elif inside[1]=='Farming-fishing': return [('occupation',1)]
        elif inside[1]=='Tech-support': return [('occupation',2)]
        elif inside[1]=='Adm-clerical': return [('occupation',3)]
        elif inside[1]=='Handlers-cleaners': return [('occupation',4)]
        elif inside[1]=='Prof-specialty': return [('occupation',5)]
        elif inside[1]=='Machine-op-inspct': return [('occupation',6)]
        elif inside[1]=='Exec-managerial': return [('occupation',7)]
        elif inside[1]=='Priv-house-serv': return [('occupation',8)]
        elif inside[1]=='Craft-repair': return [('occupation',9)]
        elif inside[1]=='Sales': return [('occupation',10)]
        elif inside[1]=='Transport-moving': return [('occupation',11)]
        elif inside[1]=='Armed-Forces': return [('occupation',12)]
        elif inside[1]=='Other-service': return [('occupation',13)]
        elif inside[1]=='Protective-serv': return [('occupation',14)]
    elif inside[0]=='relationship':
        if inside[1]=='Husband': return [('relationship',0)]
        elif inside[1]=='Wife': return [('relationship',1)]
        elif inside[1]=='Not-in-family': return [('relationship',2)]
        elif inside[1]=='Own-child': return [('relationship',3)]
        elif inside[1]=='Other-relative': return [('relationship',4)]
        elif inside[1]=='Unmarried': return [('relationship',5)]
    elif inside[0]=='race':
        if inside[1]=='Black': return [('race',0)]
        elif inside[1]=='Asian-Pac-Islander': return [('race',1)]
        elif inside[1]=='Other': return [('race',2)]
        elif inside[1]=='White': return [('race',3)]
        elif inside[1]=='Amer-Indian-Eskimo': return [('race',4)]
    elif inside[0]=='gender':
        if inside[1]=='Female': return [('gender',0)]
        elif inside[1]=='Male': return [('gender',1)]
    elif inside[0]=='hours_per_week': return [('hours_per_week',int(inside[1]))]

class HomePageView(TemplateView):
    name = 'home'
    template_name = 'income/home.html'

class FormPageView(View):
    form_class = AdultForm
    template_name = 'income/form.html'
    name = 'form'

    def get(self, request, *args, **kwargs):
        data = all_data
        return render(request, self.template_name, {'data': data})


class ResultPageView(View):
    name = 'result'
    template_name = 'income/result.html'
    pred_income='0'
    probability='0'
    def post(self, request, *args, **kwargs):
        in_put = request.POST
        iselect = {key.replace('-',''): val for key,val in in_put.items()}

        if not request.POST.getlist('age'): 
            msg='<font color="#b94a48">Required:</font><br><font color="#f8a342"> the <b>Age</b> of the Person</font>'
            page_title = 'error'
            return render(request,'income/validator.html',{'message':msg,'title':page_title,'choice':iselect,'data': all_data,})
        
        if not request.POST.getlist('education'): 
            msg='<font color="#b94a48">Required:</font><br><font color="#f8a342"> the <b>Education</b> of the Person</font>'
            page_title = 'error'
            return render(request,'income/validator.html',{'message':msg,'title':page_title,'choice':iselect,'data': all_data,})

        if not request.POST.getlist('years_education'): 
            msg='<font color="#b94a48">Required:</font><br><font color="#f8a342"> the <b>Number of years of education</b> of the Person</font>'
            page_title = 'error'
            return render(request,'income/validator.html',{'message':msg,'title':page_title,'choice':iselect,'data': all_data,})

        if not request.POST.getlist('marital_status'): 
            msg='<font color="#b94a48">Required:</font><br><font color="#f8a342"> the <b>Marital Status</b> of the Person</font>'
            page_title = 'error'
            return render(request,'income/validator.html',{'message':msg,'title':page_title,'choice':iselect,'data': all_data,})

        if not request.POST.getlist('occupation'): 
            msg='<font color="#b94a48">Required:</font><br><font color="#f8a342"> the <b>Occupation</b> of the Person</font>'
            page_title = 'error'
            return render(request,'income/validator.html',{'message':msg,'title':page_title,'choice':iselect,'data': all_data,})

        if not request.POST.getlist('relationship'): 
            msg='<font color="#b94a48">Required:</font><br><font color="#f8a342"> the <b>Relationship Status</b> of the Person</font>'
            page_title = 'error'
            return render(request,'income/validator.html',{'message':msg,'title':page_title,'choice':iselect,'data': all_data,})

        if not request.POST.getlist('race'): 
            msg='<font color="#b94a48">Required:</font><br><font color="#f8a342"> the <b>Ethicity/Race</b> of the Person</font>'
            page_title = 'error'
            return render(request,'income/validator.html',{'message':msg,'title':page_title,'choice':iselect,'data': all_data,})

        if not request.POST.getlist('gender'): 
            msg='<font color="#b94a48">Required:</font><br><font color="#f8a342"> the <b>Gender</b> of the Person</font>'
            page_title = 'error'
            return render(request,'income/validator.html',{'message':msg,'title':page_title,'choice':iselect,'data': all_data,})

        if not request.POST.getlist('hours_per_week'): 
            msg='<font color="#b94a48">Required:</font><br><font color="#f8a342"> the <b>Working Hours per Week</b> of the Person</font>'
            page_title = 'error'
            return render(request,'income/validator.html',{'message':msg,'title':page_title,'choice':iselect,'data': all_data,})



        DATA_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open('data/model.pkl', 'rb') as fin:
            pickle_model = pickle.load(fin)

        xdict = iselect #dictionary of selected values
        xlist = [(x,y) for x,y in xdict.items()] #to list

        new_tuple = []
        values_only=[]
        for i in range(1,len(xlist)): #mapping of categorical variables to a sequence of integer
            tmp1=xlist[i]
            tmp2=create_new_tuple(tmp1)
            new_tuple.append(tmp2)

            tmp3=tmp2[0]
            tmp4=tmp3[1]
            values_only.append(tmp4)


        xval=(i for i in range(1, 10))
        yval=values_only
        X_new=pd.DataFrame([xval,yval])
        #X_new=pd.DataFrame(new_tuple)


        #X_new = vectorizer.transform(new_samples)
        X_new_preds = pickle_model.predict(X_new)
        X_new_probab = pickle_model.predict_proba(X_new)
        xt=X_new_preds
        yt=X_new_probab

        str_result=str(X_new_probab[0])
        pos0=str_result.find('[')
        probability=str_result[pos0+1:9+2]
        
        if X_new_preds[0]==0 : # found
            pred_income = 'less than $50,000.00 per annum' 
        else :
            pred_income = 'more than $50,000.00 per annum' 
        print(probability)
        print(pred_income)
        #breakpoint()
        return render(request, self.template_name,{'msg':pred_income,'prob':probability,'choice':iselect,'data': all_data})

class AdultCreate(CreateView):
    model = Adult
    fields = ['age']
    name = 'adult-add'

class AdultUpdate(UpdateView):
    model = Adult
    fields = ['age']
    name = 'adult-edit'

class AdultDelete(DeleteView):
    model = Adult
    success_url = reverse_lazy('adult-list')
    name = 'adult-delete'


class AdultDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adult.objects.all()
    serializer_class = AdultSerializer
    name = 'adult-detail'

class AdultList(generics.ListCreateAPIView):
    queryset = Adult.objects.all()
    serializer_class = AdultSerializer
    name = 'adult-list'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'adults': reverse(AdultList.name,request=request),
        })






