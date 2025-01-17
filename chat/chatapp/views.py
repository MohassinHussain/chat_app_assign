from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from chatapp.models import Users
import json
from chatapp.models import Message

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        
        if Users.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            hashed_password = make_password(password)
            new_user = Users(email=email, name=name, password=hashed_password)
            new_user.save()
            messages.success(request, 'Sign-up successful! Please log in.')
            return redirect('login')
    
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = Users.objects.get(email=email)
            if check_password(password, user.password):
                request.session['currentName'] = user.name
                messages.success(request, 'Login successful!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials.')
        except Users.DoesNotExist:
            messages.error(request, 'User does not exist.')
    
    return render(request, 'login.html')

def home(request):
    current_name = request.session.get('currentName', 'Guest')
    all_users = Users.objects.all()
    return render(request, 'index.html', {"all_users": all_users, "currentName": current_name})


# SENDING AND RECEIVINF MSGS

@csrf_exempt  # for secure commu.
def send_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            sender_name = data.get('sender')
            receiver_name = data.get('receiver')
            message_text = data.get('message')

            if not sender_name or not receiver_name or not message_text:
                return JsonResponse({'error': 'All fields are required.'}, status=400)
            sender = get_object_or_404(Users, name=sender_name) # if page lost / not user
            receiver = get_object_or_404(Users, name=receiver_name) 

            message = Message(sender=sender, receiver=receiver, message=message_text)
            message.save()

            return JsonResponse({'status': 'Message sent successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid HTTP method.'}, status=405)
    
    
def get_messages(request, sender_name, receiver_name):
    try:
        sender = get_object_or_404(Users, name=sender_name)
        receiver = get_object_or_404(Users, name=receiver_name)

        messages = Message.objects.filter(
            sender=sender, receiver=receiver
        ) | Message.objects.filter(
            sender=receiver, receiver=sender
        ).order_by('timestamp')

        message_list = [
            {
                'sender': msg.sender.name,
                'receiver': msg.receiver.name,
                'message': msg.message,
                'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            }
            for msg in messages
        ]
        return JsonResponse({'messages': message_list})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
