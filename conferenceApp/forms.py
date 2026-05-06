from django import forms
from .models import Conference

class ConferenceFormModel(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ["name", "location", "start_date", "end_date", "description", "theme"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }
        
class ConferenceForm(forms.Form):
    name = forms.CharField(max_length=200)
    location = forms.CharField(max_length=200)
    start_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    description = forms.CharField(widget=forms.Textarea)
    theme = forms.ChoiceField(choices=Conference.THEME_CHOICES)