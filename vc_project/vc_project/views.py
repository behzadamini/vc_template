from . import urls
from django.shortcuts import render

def home(request):
    content = {
        'fullname': 'بهزاد امینی',
        'email': 'BehzadAmini.dev@gmail.com',
        'phone': '+98912123456',
        'address': 'تهران، خیابان شهید محمدی، پلاک 123'
        }
    return render(request, 'index.html', content)

def blog(request):
    return render(request, 'blog-details.html')