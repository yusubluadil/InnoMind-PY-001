from django import forms

from .models import Task


class AddToDoForm(forms.ModelForm):
    end_date = forms.DateField(
        label="Select a Date",
        widget=forms.DateInput(
            format='%Y-%m-%d',  # Important: HTML5 date input expects YYYY-MM-DD
            attrs={'type': 'date', 'class': 'form-control'}
        )
    )

    class Meta:
        model = Task
        fields = ('title', 'description', 'end_date')


class DetailToDoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'start_date', 'end_date',
                  'completed_date', 'status')
