from django.forms import ModelForm, ValidationError

from .models import Teacher


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'classroom']

    def clean(self):
        if not self.cleaned_data.get('name'):
            raise ValidationError("Campo 'nome' precisa estar presente")

        if not self.cleaned_data.get('classroom'):
            raise ValidationError("Campo 'classes' precisa estar presente")
