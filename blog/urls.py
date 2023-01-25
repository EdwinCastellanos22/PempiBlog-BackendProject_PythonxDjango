
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.conf.urls import handler500, handler404
from django.contrib.auth.views import LoginView, LogoutView
from blog1.views import register, index, home, about, contact, profile, update_image, update_profile, save

handler404= 'app1.views.error_404'
handler500= 'app1.views.error_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('index/', login_required(index), name='index'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', login_required(profile), name='profile'),
    path('about/', login_required(about), name='about'),
    path('contact/', login_required(contact), name='contact'),
    path('upimage/', update_image),
    path('upprofile/', update_profile),
    path('save/', save),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
