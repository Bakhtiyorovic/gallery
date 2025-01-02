from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from .models import *
from .serializers import *
# Create your views here.


def Home(request):
    categories = Category.objects.all() 
    return render(request, 'index.html', {'categories': categories})




def About(request):
    description = About_description.objects.all()
    blog_1 = About_blog_1.objects.all()
    blog_2 = About_blog_2.objects.all()
    title_1 = About_title_1.objects.all()
    title_2 = About_title_2.objects.all()
    title_3 = About_title_3.objects.all()

    context = {
        'description': description, 
        'blog_1': blog_1,
        'blog_2': blog_2,
        'title_1': title_1,
        'title_2': title_2,
        'title_3': title_3,
        }
    return render(request, 'about.html', context)




def Contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')  # message ustunini ham o'qish kerak
        
        if name and  email and message:  # Malumotlar to'liq kiritilganligini tekshiramiz
            contact_data = ContactMessage(name=name, email=email, message=message)
            contact_data.save()
            return render(request, 'contact.html', {'message': 'Ma\'lumotlar muvaffaqiyatli saqlandi.'})
        else:
            return render(request, 'contact.html', {'error': 'Iltimos, barcha maydonlarni to\'ldiring.'})
    else:
        return render(request, 'contact.html')




def Timeline_page(request):
    Timeline_categories =  Timeline_category.objects.all()
    return render(request, 'timeline.html', {'Timeline_categories': Timeline_categories})


#Api views here 


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ContactMessageViewSet(ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer


class Timeline_categoryViewSet(ModelViewSet):
    queryset = Timeline_category.objects.all()
    serializer_class = Timeline_categorySerializer



class TimelineViewSet(ModelViewSet):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer 



class About_descriptionViewSet(ModelViewSet):
    queryset = About_description.objects.all()
    serializer_class = About_descriptionSerializer



class About_blog_1ViewSet(ModelViewSet):
    queryset = About_blog_1.objects.all()
    serializer_class = About_blog_1Serializer

class About_blog_2ViewSet(ModelViewSet):
    queryset = About_blog_2.objects.all()
    serializer_class = About_blog_2Serializer

class About_title_1ViewSet(ModelViewSet):
    queryset = About_title_1.objects.all()
    serializer_class = About_title_1Serializer


class About_title_2ViewSet(ModelViewSet):
    queryset = About_title_2.objects.all()
    serializer_class = About_title_2Serializer


class About_title_3ViewSet(ModelViewSet):
    queryset = About_title_3.objects.all()
    serializer_class = About_title_3Serializer