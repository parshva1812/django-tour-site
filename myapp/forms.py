from django import forms
from django.db.models.fields import CharField
from myapp.models import Customer, Gallery,Tour,Booking,Tourist


class Gallery_form(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ["image","description"]
class Tour_form(forms.ModelForm):
    
    class Meta:
        model = Tour
        
        exclude = []
class DateInput(forms.DateInput):
    input_type = 'date'
class Booking_form(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ["customer","Payment_Method","Payment_status","Amount"]
        widgets = {
            'From_date': DateInput(),
            


        }
        labels = {
        "From_date": "Date"
         }
class Tourist_form(forms.ModelForm):
    class Meta:
        model =Tourist
        exclude =["Lname"]

