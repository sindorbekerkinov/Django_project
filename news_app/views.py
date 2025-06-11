from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .custom_permission import OnlyLoggedSuperUser

from .forms import InputForm
from .models import Category, News, Advertisement


# Create your views here.
def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {'news_list': news_list}

    return render(request,"news/news_list.html",context=context)
#
# def news_detail(request, id):
#     news = get_object_or_404(News, id=id,status=News.Status.Published)
#     context = {'news': news}
#     return render(request,"news_detail.html",context=context)
#

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'news': news,
        }
    return render(request, "news/news_detail.html", context=context)




class HomePageView(TemplateView):
    model = News
    template_name = 'news/index.html'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:4]
        context['latest_list'] = News.published.all().order_by('-publish_time')[4:8]
        context['uzb_news'] = News.published.all().filter(category__name= "Uzbekistan").order_by('-publish_time')[0]
        context['uzb_news1'] = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[1]
        context['uzb_news2'] = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[2]
        context['uzb_news3'] = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[3]
        context['uzb_news4'] = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[4]
        context['uzb_news5'] = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[5]
        context['uzb_news6'] = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[6]
        context['uzb_news7'] = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[7]
        context['uzb_news8'] = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[8]
        context['uzb_news9'] = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[9]
        context['uzb_news10'] = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[10]
        context['uzb_news11'] = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[11]


        context['world_news'] = News.published.all().filter(category__name="Jahon").order_by('-publish_time')[0:4]
        context['sport1'] = News.published.all().filter(category__name="Sport").order_by('-publish_time')[0]
        context['sport2'] = News.published.all().filter(category__name="Sport").order_by('-publish_time')[1]
        context['sport3'] = News.published.all().filter(category__name="Sport").order_by('-publish_time')[2]
        context['sport4'] = News.published.all().filter(category__name="Sport").order_by('-publish_time')[3]
        context['techno_news'] = News.published.all().filter(category__name="Fan_texnika").order_by('-publish_time')
        context['ads'] = Advertisement.objects.all().filter(status=News.Status.Published)[0]
        return context

class UzbPageView(ListView):
    model = News
    template_name = 'news/uzb.html'
    context_object_name = 'news_list'
    def get_queryset(self):
        return News.published.filter(category__name='Uzbekistan')

    def get_www(self):
        return News.published.filter(category__name='Sport')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        www = self.get_www()
        context['uzb_news'] = queryset[0]
        context['uzb_news1'] = queryset[1]
        context['uzb_news2'] = queryset[2]
        context['uzb_news3'] = queryset[3]
        context['uzb_news4'] = queryset[4]
        context['uzb_news5'] = queryset[5]
        context['uzb_news6'] = queryset[6]
        context['uzb_news7'] = queryset[7]
        context['uzb_news8'] = queryset[8]
        context['uzb_news9'] = queryset[9]
        context['uzb_news10'] = queryset[10]
        context['uzb_news11'] = queryset[11]
        context['ads'] = Advertisement.objects.all().filter(status=News.Status.Published)[0]
        context['sport1'] = www[0]
        context['sport2'] = www[1]
        context['sport3'] = www[2]
        context['sport4'] = www[3]
        return context



class JahonPageView(ListView):
    model = News
    template_name = 'news/jahon.html'
    context_object_name = 'news_list'
    def get_jahon(self):
        return News.published.filter(category__name='Jahon')
    def get_sport(self):
        return News.published.filter(category__name='Sport')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_jahon()
        www = self.get_sport()
        context['jahon1'] = queryset[0]
        context['jahon2'] = queryset[1]
        context['jahon3'] = queryset[2]
        context['ads'] = Advertisement.objects.all().filter(status=News.Status.Published)[0]
        context['sport1'] = www[0]
        context['sport2'] = www[1]
        context['sport3'] = www[2]
        context['sport4'] = www[3]
        return context

class SportPageView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'news_list'
    def get_sport(self):
        return News.published.filter(category__name='Sport')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        www = self.get_sport()
        context['ads'] = Advertisement.objects.all().filter(status=News.Status.Published)[0]
        context['sport1'] = www[0]
        context['sport2'] = www[1]
        context['sport3'] = www[2]
        context['sport4'] = www[3]
        return context

class FanPageView(ListView):
    model = News
    template_name = 'fan-texnika.html'
    context_object_name = 'news/news_list'
    def get_fan(self):
        return News.published.filter(category__name='Fan_texnika')
    def get_sport(self):
        return News.published.filter(category__name='Sport')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        www = self.get_sport()
        fan = self.get_fan()
        context['ads'] = Advertisement.objects.all().filter(status=News.Status.Published)[0]
        context['sport1'] = www[0]
        context['sport2'] = www[1]
        context['sport3'] = www[2]
        context['sport4'] = www[3]
        context['fan1'] = fan[0]
        context['fan2'] = fan[1]
        context['fan3'] = fan[2]
        return context



class ContactView(TemplateView):
    template_name = 'news/contact.html'
    def post(self, request, *args, **kwargs):
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return self.render_to_response(self.get_context_data(form=form))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = InputForm()
        return context

# <<<<<<<< Bu ham bir variant
# class ContactPageView(CreateView):
#     form_class = InputForm
#     template_name = 'contact.html'
#     success_url = reverse_lazy('home')

class NewsUpdateView(OnlyLoggedSuperUser,UpdateView):
    model = News
    fields = ('title', 'body', 'image','category', 'status',)
    template_name = 'crud/news_edit.html'
    success_url = reverse_lazy('home')
class NewsDeleteView(OnlyLoggedSuperUser,DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('home')
class NewsCreateView(OnlyLoggedSuperUser,CreateView):
    model = News
    template_name = 'crud/news_create.html'
    fields = ('title', 'slug', 'body', 'image','category', 'status',)
    success_url = reverse_lazy("home")






#
# def home_page(request):
#     latest_news = News.published.all().filter(status=News.Status.Published)[:3]
#     latest_news1 = News.published.all().filter(status=News.Status.Published)[3]
#     latest_news2 = News.published.all().filter(status=News.Status.Published)[4]
#     latest_news3 = News.published.all().filter(status=News.Status.Published)[5]
#     latest_news4 = News.published.all().filter(status=News.Status.Published)[6]
#
#     fan_news = News.published.all().filter(category__name="Fan_texnika")[:5]
#     uzb_news = News.published.all().filter(category__name="Uzbekistan")[0]
#     uzb_news1 = News.published.all().filter(category__name="Uzbekistan")[1]
#     uzb_news2 = News.published.all().filter(category__name="Uzbekistan")[2]
#     uzb_news3 = News.published.all().filter(category__name="Uzbekistan")[3]
#     uzb_news4 = News.published.all().filter(category__name="Uzbekistan")[4]
#     uzb_news5 = News.published.all().filter(category__name="Uzbekistan")[5]
#     uzb_news6 = News.published.all().filter(category__name="Uzbekistan")[6]
#     uzb_news7 = News.published.all().filter(category__name="Uzbekistan")[7]
#     uzb_news8 = News.published.all().filter(category__name="Uzbekistan")[8]
#     uzb_news9 = News.published.all().filter(category__name="Uzbekistan")[9]
#     uzb_news10 = News.published.all().filter(category__name="Uzbekistan")[10]
#     uzb_news11 = News.published.all().filter(category__name="Uzbekistan")[11]
#     ads = Advertisement.published.all().filter(status=News.Status.Published)[0]
#     sport1 = News.published.all().filter(category__name="Sport")[0]
#     sport2 = News.published.all().filter(category__name="Sport")[1]
#     sport3 = News.published.all().filter(category__name="Sport")[2]
#     sport4 = News.published.all().filter(category__name="Sport")[3]
#     context = {
#         'latest_news': latest_news,
#         'latest_news1': latest_news1,
#         'latest_news2': latest_news2,
#         'latest_news3': latest_news3,
#         'latest_news4': latest_news4,
#         'fan_news': fan_news,
#         'uzb_news': uzb_news,
#         'uzb_news1' : uzb_news1,
#         'uzb_news2': uzb_news2,
#         'uzb_news3': uzb_news3,
#         'uzb_news4': uzb_news4,
#         'uzb_news5': uzb_news5,
#         'uzb_news6': uzb_news6,
#         'uzb_news7': uzb_news7,
#         'uzb_news8': uzb_news8,
#         'uzb_news9': uzb_news9,
#         'uzb_news10': uzb_news10,
#         'uzb_news11' : uzb_news11,
#         'ads': ads,
#         'sport1': sport1,
#         'sport2': sport2,
#         'sport3': sport3,
#         'sport4': sport4
#
#     }
#     return render(request,'index.html', context=context)

# def jahon_page(request):
#     sport1 = News.objects.filter(category__name="Sport")[0]
#     sport2 = News.objects.filter(category__name="Sport")[1]
#     sport3 = News.objects.filter(category__name="Sport")[2]
#     sport4 = News.objects.filter(category__name="Sport")[3]
#     ads = Advertisement.objects.filter(status=News.Status.Published)[0]
#     jahon1 = News.objects.filter(category__name="Jahon")[0]
#     jahon2 = News.objects.filter(category__name="Jahon")[1]
#     jahon3 = News.objects.filter(category__name="Jahon")[2]
#
#     context = {
#         'sport1': sport1,
#         'sport2': sport2,
#         'sport3': sport3,
#         'sport4': sport4,
#         'ads': ads,
#         'jahon1': jahon1,
#         "jahon2": jahon2,
#         "jahon3": jahon3,
#     }
#     return render(request,'jahon.html', context=context)

#
# def uzb_page(request):
#     uzb_news = News.published.all().filter(category__name="Uzbekistan")[0]
#     uzb_news1 = News.published.all().filter(category__name="Uzbekistan")[1]
#     uzb_news2 = News.published.all().filter(category__name="Uzbekistan")[2]
#     uzb_news3 = News.published.all().filter(category__name="Uzbekistan")[3]
#     uzb_news4 = News.published.all().filter(category__name="Uzbekistan")[4]
#     uzb_news5 = News.published.all().filter(category__name="Uzbekistan")[5]
#     uzb_news6 = News.published.all().filter(category__name="Uzbekistan")[6]
#     uzb_news7 = News.published.all().filter(category__name="Uzbekistan")[7]
#     uzb_news8 = News.published.all().filter(category__name="Uzbekistan")[8]
#     uzb_news9 = News.published.all().filter(category__name="Uzbekistan")[9]
#     uzb_news10 = News.published.all().filter(category__name="Uzbekistan")[10]
#     uzb_news11 = News.published.all().filter(category__name="Uzbekistan")[11]
#     sport1 = News.published.all().filter(category__name="Sport")[0]
#     sport2 = News.published.all().filter(category__name="Sport")[1]
#     sport3 = News.published.all().filter(category__name="Sport")[2]
#     sport4 = News.published.all().filter(category__name="Sport")[3]
#     ads = Advertisement.published.all().filter(status=News.Status.Published)[0]
#
#     context = {
#         'uzb_news': uzb_news,
#         'uzb_news1': uzb_news1,
#         'uzb_news2': uzb_news2,
#         'uzb_news3': uzb_news3,
#         'uzb_news4': uzb_news4,
#         'uzb_news5': uzb_news5,
#         'uzb_news6': uzb_news6,
#         'uzb_news7': uzb_news7,
#         'uzb_news8': uzb_news8,
#         'uzb_news9': uzb_news9,
#         'uzb_news10': uzb_news10,
#         'uzb_news11': uzb_news11,
#         'sport1': sport1,
#         'sport2': sport2,
#         'sport3': sport3,
#         'sport4': sport4,
#         'ads': ads
#     }
#
#     return render(request,'uzb.html', context=context)

# def contact_page(request):
#     form = InputForm(request.POST)
#     if request.POST and form.is_valid():
#         form.save()
#         return redirect("home")
#     context = {
#         "form": form
#     }
#     return render(request,'contact.html',context=context)


# def sport_page(request):
#     sport1 = News.objects.filter(category__name="Sport")[0]
#     sport2 = News.objects.filter(category__name="Sport")[1]
#     sport3 = News.objects.filter(category__name="Sport")[2]
#     sport4 = News.objects.filter(category__name="Sport")[3]
#     ads = Advertisement.objects.filter(status=News.Status.Published)[0]
#
#
#     context = {
#         'sport1': sport1,
#         'sport2': sport2,
#         'sport3': sport3,
#         'sport4': sport4,
#         'ads': ads
#     }
#     return render(request,'sport.html',context=context)


# def fan_page(request):
#     sport1 = News.objects.filter(category__name="Sport")[0]
#     sport2 = News.objects.filter(category__name="Sport")[1]
#     sport3 = News.objects.filter(category__name="Sport")[2]
#     sport4 = News.objects.filter(category__name="Sport")[3]
#     ads = Advertisement.objects.filter(status=News.Status.Published)[0]
#     fan1 = News.objects.filter(category__name="Fan_texnika")[0]
#     fan2 = News.objects.filter(category__name="Fan_texnika")[1]
#     fan3 = News.objects.filter(category__name="Fan_texnika")[2]
#
#     context = {
#         'sport1': sport1,
#         'sport2': sport2,
#         'sport3': sport3,
#         'sport4': sport4,
#         'ads': ads,
#         'fan1': fan1,
#         'fan2': fan2,
#         'fan3': fan3
#
#     }
#     return render(request,'fan-texnika.html', context=context)
