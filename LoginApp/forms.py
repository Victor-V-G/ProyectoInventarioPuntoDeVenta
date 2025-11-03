from django import forms

class LoginForm(forms.Form):

    UsernameField = forms.CharField(
        label="Ingresa tu username"
    )

    PasswordField = forms.CharField(
        label="Ingresa tu password"
    )

    class Meta:
        fields = ['UsernameField', 'PasswordField']