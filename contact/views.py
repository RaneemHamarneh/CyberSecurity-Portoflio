from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django_ratelimit.decorators import ratelimit
from .forms import ContactForm


@ratelimit(key='ip', rate='5/m', block=True)
def contact_view(request):
    sent = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            to_email = getattr(settings, "CONTACT_EMAIL_TO", "")
            if to_email:
                send_mail(
                    subject=f"Portfolio Contact: {form.cleaned_data['name']}",
                    message=form.cleaned_data["message"],
                    from_email=form.cleaned_data["email"],
                    recipient_list=[to_email],
                    fail_silently=True,
                    )
        sent = True
        form = ContactForm() # reset
    else:
        form = ContactForm()


    return render(request, "contact/contact.html", {"form": form, "sent": sent})