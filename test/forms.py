from django import forms


TICKET_CHOICES = [
    ("early-bird", "Early Bird Pass"),
    ("standard", "Standard Pass"),
    ("vip", "VIP Pass"),
    ("student", "Student Pass"),
]

QUANTITY_CHOICES = [
    ("1", "1 Ticket"),
    ("2", "2 Tickets"),
    ("3", "3 Tickets"),
    ("4", "4 Tickets"),
    ("5", "5 Tickets"),
    ("more", "More than 5 (Contact us)"),
]

class TicketForm(forms.Form):
    ticket_type = forms.ChoiceField(
        choices=TICKET_CHOICES,
        widget=forms.RadioSelect,
        label="Ticket Type"
    )
    first_name = forms.CharField(max_length=100, label="First Name")
    last_name = forms.CharField(max_length=100, label="Last Name")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(max_length=20, label="Phone")
    company = forms.CharField(max_length=150, label="Company")
    job_title = forms.CharField(max_length=150, label="Job Title")
    quantity = forms.ChoiceField(choices=QUANTITY_CHOICES, label="Number of Tickets")
    dietary = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3}),
        required=False,
        label="Dietary Restrictions"
    )
    special_requests = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3}),
        required=False,
        label="Special Requests"
    )
    terms = forms.BooleanField(label="Agree to Terms and Conditions")
    newsletter = forms.BooleanField(required=False, label="Subscribe to newsletter")



