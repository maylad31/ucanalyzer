from django import forms


class MyForm(forms.Form):
    use_case_name = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':20}),required=False)
    primary_actor = forms.CharField(max_length=256,required=False,widget=forms.TextInput(attrs={'class':"form-control",'size':20}))
    
    pc1 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    pc2 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    pc3 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    pc4 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    
    poc1 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    poc2 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    poc3 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    poc4 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    
    bf1 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    bf2 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    bf3 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    bf4 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    bf5 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    bf6 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    bf7 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    bf8 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    bf9 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    bf10 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    bf11 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    bf12 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'class':"form-control",'size':70}),required=False)
    
    afn1 = forms.CharField(max_length=3,widget=forms.TextInput(attrs={'class':"form-control",'size':4}),required=False)
    afd1 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'id':'afd1','class':"form-control af",'size':70}),required=False)
    afn2 = forms.CharField(max_length=3,widget=forms.TextInput(attrs={'class':"form-control",'size':4}),required=False)
    afd2 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'id':'afd2','class':"form-control",'size':70}),required=False)
    afn3 = forms.CharField(max_length=3,widget=forms.TextInput(attrs={'class':"form-control",'size':4}),required=False)
    afd3 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'id':'afd3','class':"form-control",'size':70}),required=False)
    afn4 = forms.CharField(max_length=3,widget=forms.TextInput(attrs={'class':"form-control",'size':4}),required=False)
    afd4 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'id':'afd4','class':"form-control",'size':70}),required=False)
    afn5 = forms.CharField(max_length=3,widget=forms.TextInput(attrs={'class':"form-control",'size':4}),required=False)
    afd5 = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'id':'afd5','class':"form-control",'size':70}),required=False)
    requirements = forms.CharField( widget=forms.Textarea(attrs={'rows': 9, 'cols': 100}),required=False)
    
