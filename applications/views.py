from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from .models import ApplicationForm
from django.conf import settings

def index(request):
    if request.method == "POST":
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        place = request.POST.get('place')
        district = request.POST.get('district')
        modules = request.POST.getlist('modules')

        # Save application
        application = ApplicationForm.objects.create(
            name=name,
            email=email,
            phone=phone,
            qualification=qualification,
            experience=experience,
            place=place,
            district=district,
            marketing_module=modules
        )

        # Prepare email content for admin
        subject_admin = "New Application Submitted"
        message_admin = f"""
        You have received a new application.
        Name: {application.name}
        Email: {application.email}
        Phone: {application.phone}
        Qualification: {application.qualification}
        Experience: {application.experience}
        Place: {application.place}
        District: {application.district}
        Modules: {', '.join(application.marketing_module)}
        """
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.RECIPIENT_EMAIL]

        # Send email to admin
        send_mail(subject_admin, message_admin, from_email, recipient_list)

        # Prepare email content for client
        subject_client = "Application Received"
        message_client = f"""
        Dear {application.name},
        Thank you for your application! We have received the following information:
        Name: {application.name}
        Email: {application.email}
        Phone: {application.phone}
        Qualification: {application.qualification}
        Experience: {application.experience}
        Place: {application.place}
        District: {application.district}
        Modules: {', '.join(application.marketing_module)}
        We will review your application and get back to you soon.
        Best regards,
        Your Company Name
        """

        # Send email to client
        try:
            send_mail(subject_client, message_client, from_email, [application.email])
        except BadHeaderError:
            print("Invalid header found.")
        except Exception as e:
            print(f"Error sending email to client: {e}")

        return render(request, 'thank_you.html')

    return render(request, 'application_form.html')
