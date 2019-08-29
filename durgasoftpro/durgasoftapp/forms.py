from django import forms
from multiselectfield import MultiSelectFormField


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Enter your Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )
    rating = forms.IntegerField(
        label="Enter your rating",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Rating'
            }
        )
    )
    feedback = forms.CharField(
        label="Enter your Feedback",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your valuable feedback'
            }
        )
    )


class EnquiryForm(forms.Form):
    name = forms.CharField(
        label="Enter your Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )

    email = forms.EmailField(
        label="Enter your e-Mail ID",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your e-Mail ID'
            }
        )
    )

    mobile = forms.IntegerField(
        label="Enter your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Mobile Number'
            }
        )
    )

    Gender_Choices = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect, choices=Gender_Choices
    )

    COURSES_CHOICES = (
        ('Py', "Python"),
        ('Dj', "Django"),
        ('RA', "REST API"),
        ('Fl', "Flask"),
        ('UI', "UI")
    )
    courses = MultiSelectFormField(choices=COURSES_CHOICES)

    SHIFTS_CHOICES = (
        ('morning', 'Morning Shift'),
        ('Afternoon', 'Afternoon Shift'),
        ('Evening', 'Evening Shift'),
        ('Night', 'Night Shift'),
    )
    shifts = MultiSelectFormField(choices=SHIFTS_CHOICES)

    start_date = forms.DateField(
        widget=forms.SelectDateWidget()
    )
