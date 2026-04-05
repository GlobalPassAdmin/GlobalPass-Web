from django.shortcuts import render
from .models import Service # استدعاء موديل الخدمات القديم

def home(request):
    # جلب جميع الخدمات المخزنة مسبقاً في قاعدة البيانات
    services = Service.objects.all()
    
    # إرسال البيانات إلى ملف التصميم index.html
    return render(request, 'index.html', {'services': services})
