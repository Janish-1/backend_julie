from django.views import View
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import User
import random
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sendemail(request):
    try:
        email = request.POST.get('email')
        
        # Generate OTP
        otp = ''.join(random.choices('0123456789', k=4))

        # Compose email
        subject = 'Login OTP'
        message = f'Your OTP for Login is: {otp}'
        from_email = 'noreply@ramo.co.in'  # Get sender email from settings
        recipient_list = [email]

        # Send email
        send_mail(subject, message, from_email, recipient_list)

        return JsonResponse({'message': 'Email sent successfully','otp':otp})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
