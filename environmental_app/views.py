from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  # 正确导入消息框架
from .models import ForumPost, Comment  # 确保正确导入 Comment 模型


# 定义一个名为home的函数，接收一个参数request
def home(request):
    # 使用render函数渲染home.html页面，并返回给用户
    return render(request, 'home.html')

# 定义一个函数，用于返回土壤水分健康页面
def soil_water_health(request):
    # 使用render函数，将请求渲染到soil_water_health.html页面
    return render(request,'soil_water_health.html')

# 定义一个名为pollution_causes的函数，接收一个参数request
def pollution_causes(request):
    # 返回一个渲染pollution_causes.html模板的响应
    return render(request, 'pollution_causes.html')

# 定义一个函数，用于处理请求，返回actions_to_take.html页面
def actions_to_take(request):
    return render(request, 'actions_to_take.html')

# 定义一个名为forum的函数，接收一个参数request
def forum(request):
    # 从数据库中获取所有的ForumPost对象
    posts = ForumPost.objects.all()
    # 将获取到的对象传递给名为forum.html的模板，并返回渲染后的页面
    return render(request, 'forum.html', {'posts': posts})

def more(request):
    return render(request, 'more.html')

def industrial_pollution(request):
    return render(request, 'industrial_pollution.html')

def domestic_pollution(request):
    return render(request, 'domestic_pollution.html')

def agricultural_pollution(request):
    return render(request, 'agricultural_pollution.html')

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            ForumPost.objects.create(title=title, content=content)
            messages.success(request, '帖子发布成功！')  # 正确使用消息框架
            return redirect('forum')
        else:
            messages.error(request, '标题和内容不能为空！')
    return render(request, 'forum.html')

def create_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(ForumPost, id=post_id)
        content = request.POST.get('content')
        if content:
            Comment.objects.create(post=post, content=content)
            messages.success(request, '评论发布成功！')
        else:
            messages.error(request, '评论内容不能为空！')
    return redirect('forum')
