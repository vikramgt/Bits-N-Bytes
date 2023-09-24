from .forms import BullyingReportForm
from django.shortcuts import render, HttpResponse, redirect
from .models import user_id
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CRUDFORM
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
# from myapp.backends import EmailBackend
from .authentication import EmailBackend

import pdb
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import QuizResponse
from .serializers import QuizResponseSerializer
from .models import FAQ
import tensorflow as tf
# from tensorflow import keras
from tensorflow.keras.models import load_model
import numpy as np

# Adjust the path accordingly
loaded_model = load_model('best_model.h5')


def HomePage(request):
    return render(request, 'home.html')


def foucsmode(request):
    return render(request, 'focusMode.html')


def SignIn(request):
    print(request.method)
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = EmailBackend().authenticate(request=request, email=email, password=password,
                                           model=user_id, backend='myapp.backends.EmailBackend')
        print("user is ", user)
        if user:
            request.session['user'] = str(user).upper()
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return render(request, 'signin.html')
    return render(request, 'signin.html')


def TakeTest(request):
    return render(request, 'taketest.html')


def SignUp(request):
    form = CRUDFORM(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('taketest')
    context = {
        "form": form
    }
    return render(request, 'signup.html', context)


def Logout(request):
    logout(request)
    request.session.flush()
    return redirect('home')
# Create your views here.


def MyApi(request):
    return render(request, 'my-api-endpoint.html')


def MentalHealth(request):
    faqs = FAQ.objects.all()
    return render(request, 'MentalHealth.html', {'faqs': faqs})


class QuizResponseView(APIView):
    def post(self, request):
        serializer = QuizResponseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            breakpoint()
            input_data = request.data[serializer]

            # Preprocess the input data if needed (e.g., convert to NumPy array)
            input_data = np.array(input_data)

            # Make predictions using the loaded model
            predictions = loaded_model.predict(input_data)

            return Response({'predictions': predictions.tolist()}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def report_bullying(request):
    if request.method == 'POST':
        form = BullyingReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = BullyingReportForm()

    return render(request, 'report_bullying.html', {'form': form})


def thank_you(request):
    return render(request, 'thank_you.html')
