from django import forms

'''class Details(forms.Form):
    username=forms.CharField(label='username', max_length=50)
    password=forms.CharField(label='password', max_length=50)
'''
class Posts_Details(forms.Form):
    title=forms.CharField(label='title',max_length=200)
    post=forms.CharField(label='post',max_length=500)
class User_Signup(forms.Form):
    username=forms.CharField(label='username',max_length=200)
    password=forms.CharField(label='passwoed',max_length=500)
