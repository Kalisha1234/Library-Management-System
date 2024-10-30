from django import forms
from .models import Book, Member, Borrow

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = '__all__'
        widgets = {
            'borrow_date': forms.DateInput(attrs={'type': 'date'}),
            # 'due_date': forms.DateInput(attrs={'type': 'date'}),
        }