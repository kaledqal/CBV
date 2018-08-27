from django import forms
from basic_app.models import School,Student

class SchoolForm(models.ModelForm):
    class Meta():
        model = School
        fields = '__all__'
