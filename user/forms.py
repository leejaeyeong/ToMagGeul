from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from .models import TMUser, TMAuthor
from .managers import TMUserManager
from genre.models import Genre

class PhoneField(forms.MultiValueField):
    def __init__(self, **kwargs):
        # Define one message for all fields.
        error_messages = {
            'incomplete': 'Enter a country calling code and a phone number.',
        }
        # Or define a different message for each field.
        fields = (
            forms.CharField(
                error_messages={'incomplete': 'Enter a country calling code.'},
                validators=[RegexValidator(r'^[0-9]{2,4}$', 'Enter a valid country calling code.'),],
                required=True,
            ),
            forms.CharField(
                error_messages={'incomplete': 'Enter a phone number.'},
                validators=[RegexValidator(r'^[0-9]{3,4}$', 'Enter a valid phone number.')],
                required=True,
            ),
            forms.CharField(
                validators=[RegexValidator(r'^[0-9]{,4}$', 'Enter a valid extension.')],
                required=True,
            ),
        )
        super().__init__(
            error_messages=error_messages, fields=fields,
            require_all_fields=False, **kwargs
        )

class UserCreationForm(forms.ModelForm):
    # 사용자 생성 폼
    email = forms.EmailField(
        label=_('Email'),
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Email address'),
                'required': 'True',
            }
        ),
        max_length = 255
    )
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password'),
                'required': 'True',
            }
        ),
        max_length = 30,
        min_length = 8,
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password confirmation'),
                'required': 'True',
            }
        ),
        max_length = 30,
        min_length = 8,
    )
    nickname = forms.CharField(
        label=_('Nickname'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nickname'),
                'required': 'True',
            }
        ),
        max_length = 50
    )

    name = forms.CharField(
        label=_('Name'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Name'),
                'required': 'True',
            }
        ),
        max_length = 30
    )

    date_of_birth = forms.SplitDateTimeField(
        label=_('Date of Birth'),
        required=True,
        widget=forms.DateInput(
            attrs={
                'type' : 'date',
                'class': 'form-control',
                'required': 'True',
            },
            format='%Y-%m-%d'
        ),
        input_date_formats='%Y-%m-%d'
    )

    phone_number = PhoneField()

    address = forms.CharField(
        label=_('Address'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('address'),
            }
        ),
        max_length = 200
    )

    prefer_genre = forms.ModelMultipleChoiceField(Genre.objects)

    is_author = forms.BooleanField(
        label=_('Register Author'),
        widget=forms.CheckboxInput(
            attrs={
                'onchange':"setDisplay()",
                'required': 'False',
            }
        )
    )

    class Meta:
        model = TMUser
        fields = (  'email', 
                    'password1', 
                    'password2', 
                    'nickname', 
                    'name', 
                    'date_of_birth',
                    'phone_number',
                    'address',
                    'prefer_genre',)

    def clean_password2(self):
        # 두 비밀번호 입력 일치 확인
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.email = TMUserManager.normalize_email(self.cleaned_data['email'])
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class AuthorCreationForm(forms.ModelForm):
    # 작가 생성 폼

    class Meta:
        model = TMAuthor
        fields = (  'author_name', 
                    'introduce', 
                    'page_link', 
                    'sns_link', 
                    'portfolio',)

# class UserChangeForm(forms.ModelForm):
#     # 비밀번호 변경 폼
#     password = ReadOnlyPasswordHashField(
#         label=_('Password')
#     )

#     class Meta:
#         model = TMUser
#         fields = ('email', 'password', 'last_name', 'first_name', 'is_active', 'is_superuser')

#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]