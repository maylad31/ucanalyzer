from django.shortcuts import render,get_object_or_404
from .forms import MyForm
from django.utils import timezone
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .ucvt import *
from django.http import HttpResponse,JsonResponse


def my_form_upload(request):
    if request.method == 'GET':
        form = MyForm()
    else:
        if request.is_ajax():
        # A POST request: Handle Form Upload
            form = MyForm(request.POST,request.FILES) # Bind data from request.POST into a PostForm
 
        # If data is valid, proceeds to create a new post and redirect the user
            if form.is_valid():
                use_case_name = form.cleaned_data['use_case_name']
                primary_actor = form.cleaned_data['primary_actor']
                pc1 = form.cleaned_data['pc1']
                pc2 = form.cleaned_data['pc2']
                pc3 = form.cleaned_data['pc3']
                pc4 = form.cleaned_data['pc4']
                poc1 = form.cleaned_data['poc1']
                poc2 = form.cleaned_data['poc2']
                poc3 = form.cleaned_data['poc3']
                poc4 = form.cleaned_data['poc4']

                bf1 = form.cleaned_data['bf1']
                bf2 = form.cleaned_data['bf2']
                bf3 = form.cleaned_data['bf3']
                bf4 = form.cleaned_data['bf4']
                bf5 = form.cleaned_data['bf5']
                bf6 = form.cleaned_data['bf6']
                bf7 = form.cleaned_data['bf7']
                bf8 = form.cleaned_data['bf8']
                bf9 = form.cleaned_data['bf9']
                bf10 = form.cleaned_data['bf10']
                bf11 = form.cleaned_data['bf11']
                bf12 = form.cleaned_data['bf12']
                afn1 = form.cleaned_data['afn1']
                afd1 = form.cleaned_data['afd1']
                afn2 = form.cleaned_data['afn2']
                afd2 = form.cleaned_data['afd2']
                afn3 = form.cleaned_data['afn3']
                afd3 = form.cleaned_data['afd3']
                afn4 = form.cleaned_data['afn4']
                afd4 = form.cleaned_data['afd4']
                afn5 = form.cleaned_data['afn5']
                afd5 = form.cleaned_data['afd5']
                r1=form.cleaned_data['requirements']
                pre=pc1+" "+pc2+" "+pc3+" "+pc4
                post=poc1+" "+poc2+" "+poc3+" "+poc4
                basic=bf1+" "+bf2+" "+bf3+" "+bf4+" "+bf5+" "+bf6+" "+bf7+" "+bf8+" "+bf9+" "+bf10+" "+bf11+" "+bf12
                alt=afd1+" "+afd2+" "+afd3+" "+afd4+" "+afd5
                primary_actor=primary_actor.replace(" ", "")
            #return HttpResponseRedirect('my_form1',dd)
                pinit()
                checkname(use_case_name)
                ccc1(primary_actor)
                precheck(pre)
                postcheck(post)
                sentstructure(basic)
                checkactors(primary_actor,basic)
                checkactors2(primary_actor,r1)
                sentstructure1(alt)
                checkifelse(alt)
                completeness1(r1,basic)
                sents=sent_tokenize(basic)
                dd1=False
                if len(afn1)>0 and not afn1 is None and not int(afn1[0])is None:
                    afnn1=int(afn1[0])
                    if afn1[1].isdigit() is True:
                        afnn1=int(afn1[0]+afn1[1])
                    print(str(afnn1)+"Mayank")
                    if len(sents)>=afnn1:
                        print(sents[afnn1-1])
                        compare(afd1,str(sents[afnn1-1]))
                    else:
                        dd1=True
                if len(afn2)>0 and not afn2 is None and not int(afn2[0])is None:
                    afnn1=int(afn2[0])
                    if afn2[1].isdigit() is True:
                        afnn1=int(afn2[0]+afn2[1])
                    if len(sents)>=afnn1:
                        compare(afd2,str(sents[afnn1-1]))
                    else:
                        dd1=True    
                if len(afn3)>0and not afn3 is None and not int(afn3[0])is None:
                    afnn1=int(afn3[0])
                    if afn3[1].isdigit() is True:
                        afnn1=int(afn3[0]+afn3[1])
                    if len(sents)>=afnn1:
                        compare(afd3,str(sents[afnn1-1]))
                    else:
                        dd1=True        
                if len(afn4)>0 and not afn4 is None and not int(afn4[0])is None:
                    afnn1=int(afn4[0])
                    if afn4[1].isdigit() is True:
                        afnn1=int(afn4[0]+afn4[1])
                    if len(sents)>=afnn1:
                        compare(afd4,str(sents[afnn1-1]))
                    else:
                        dd1=True        
                if len(afn5)>0 and not afn5 is None and not int(afn5[0])is None:
                    afnn1=int(afn5[0])
                    if afn5[1].isdigit() is True:
                        afnn1=int(afn5[0]+afn5[1])
                    if len(sents)>=afnn1:
                        compare(afd5,str(sents[afnn1-1]))
                    else:
                        dd1=True
                completeness(r1,basic+alt+pre+post)        
                bLine = pfinal()    
            #bLine=bLine.split(".")
                #bLine=str(bLine)
                if dd1 is True:
                    bLine=bLine+"</br> There is error in numbering in alternate flow."
                dd={'bsf':bLine}
            
            #return render(request,'blog/my_form.html',{'dd1':dd})
                print(bLine)
                return HttpResponse(bLine)
            #return render(request,'blog/my_form.html',{'form':form,'dd1':dd}) 
    return render(request, 'blog/my_form.html', {'form': form})
