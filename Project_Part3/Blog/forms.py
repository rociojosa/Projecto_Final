from django.forms import ModelForm
from models import NewPost

class PostForm(ModelForm):
    class Meta:
        model = NewPost
        fields= '__all__'