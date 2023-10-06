from django import forms
from .models import Application,District,Branches
from django.forms.widgets import DateInput

Gender_choices=[("Male","Male"),
                ("Female","Female") ]

Materials_provided_choices=[("Debit card","Debit card"),
                            ("Credit card", "Credit card"),
                            ("Cheque book","Cheque book")]
accounttype_CHOICES=[
    ("Savings account" ,"Savings account"),
    ("Current account","Current account")
    ]
district_choices=[
    ("Ernakulam" ,"Ernakulam"),
    ("Thrissur","Thrissur"),
    ("Kottayam","Kottayam"),
    ("Kollam","Kollam"),
    ("Trivandrum","Trivandrum")
    ]
class ApplicationForm(forms.ModelForm):
    name = forms.CharField(max_length=250)
    DOB = forms.DateField()
    age = forms.IntegerField()
    Gender = forms.ChoiceField(choices=Gender_choices, widget=forms.RadioSelect)
    email = forms.EmailField(max_length=200)
    phonenumber = forms.IntegerField()
    address = forms.TextInput()
    district = forms.ChoiceField(choices=district_choices)
    branch=forms.CharField(max_length=250)
    state = forms.CharField(max_length=250)
    pincode = forms.IntegerField()
    accounttype = forms.ChoiceField( choices=accounttype_CHOICES)




    Materials_provided=forms.MultipleChoiceField(choices=Materials_provided_choices,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Application
        fields="__all__"
        labels = {'name': 'Full Name', 'dob': 'Date of Birth','age':'Age','Gender':'Gender','address':'Address','district':'District',
                  'branch':'Branch','state':'State','pincode':'Pincode','email': 'Email ID','accounttype':'Account type','Materials_provided':'Materials_provided',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'Dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'date-picker'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone number': forms.NumberInput(attrs={'class':'form-control'}),
            'address': forms.Textarea(attrs={'class':'form-control'}),
            'district': forms.TextInput(attrs={'class':'form-control'}),
            'branch': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.NumberInput(attrs={'class':'form-control'}),

            'accounttype': forms.TextInput(attrs={'class': 'form-control'}),
            'materials-provided': forms.TextInput(attrs={'class': 'form-control'}),
        }

    class Meta:
        model=District
        fields=["name"]
    class Meta:
        model=Branches
        fields=["name"]

