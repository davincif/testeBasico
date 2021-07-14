from django.forms import ModelForm, ValidationError

from .models import Classroom


class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ['name']

    def clean(self):
        if not self.cleaned_data.get('name'):
            raise ValidationError("Campo 'nome' precisa estar presente")
