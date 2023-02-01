from django.shortcuts import render
from django.views import View
# Create your views here.

# 用户注册
class RegisterView(View):
    
    # 提供用户注册页面
    def get(self, request):
        return render(request, 'register.html')

    # 实现用户注册逻辑
    def post(self, request):
        
        pass