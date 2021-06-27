from django import forms
from  WebApp.models import Team,Player,Matches

class TeamForm(forms.ModelForm):
    class Meta:
        model=Team
        fields=["tname","logourl","state"]


class PlayerForm(forms.ModelForm):
    class Meta:
        model=Player
        fields='__all__'

class MatchesForm(forms.ModelForm):
    class Meta:
        model=Matches
        fields='__all__'