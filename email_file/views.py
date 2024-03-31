from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage

def sendMail(request):

    # create a variable to keep track of the form
    messageSent = False

    # check if form has been submitted
    if request.method == 'POST':

        form = EmailForm(request.POST, request.FILES)

        # check if data from the form is clean
        if form.is_valid():
            cd = form.cleaned_data
            subject = "This is an sample heading of my mail"
            message = cd['message']
            recipient = cd['recipient']
            cc = cd.get('cc')
            bcc = cd.get('bcc')

            email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient], cc=[cc], bcc=[bcc])

            attachment = request.FILES.get('attachment')
            if attachment:
                email.attach(attachment.name, attachment.read(), attachment.content_type)

            # send the email
            email.send()

            # set the variable initially created to True
            messageSent = True

    else:
        form = EmailForm()

    return render(request, 'index.html', {'form': form, 'messageSent': messageSent})