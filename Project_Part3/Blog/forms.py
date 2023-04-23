from django.forms import ModelForm
from Blog.models import NewPost, Comment

class PostForm(ModelForm):
    class Meta:
        model = NewPost
        fields= '__all__'

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'