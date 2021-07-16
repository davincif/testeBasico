from django.forms import ModelForm, ValidationError

from .models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'teacher']

    def clean(self):
        if not self.cleaned_data.get('name'):
            raise ValidationError("Campo 'nome' precisa estar presente")

        if not self.cleaned_data.get('teacher'):
            raise ValidationError("Campo 'professor' precisa estar presente")
