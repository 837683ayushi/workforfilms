"""WORKFORFILMSa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('pages.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('User.urls')),
    path('user/', include('django.contrib.auth.urls')),
    path('posts/', include('posts.urls')),
    path('actionvehicle/',include('actionvehicle.urls')),
    path('actors/',include('actors.urls')),
    path('amenity_adresses/',include('Amenity_Adresses.urls')),
    path('booking/',include('Booking.urls')),
    path('childartist/',include('ChildArtist.urls')),
    path('circleinvite/',include('CircleInvite.urls')),
    path('client/',include('Client.urls')),
    path('comments/',include('Comments.urls')),
    path('contactmessages/',include('ContactMessages.urls')),
    path('conversations/',include('conversations.urls')),
    path('userprofessionalinfo/',include('userprofessionalinfo.urls')),
    path('voiceoverartist/',include('VoiceOverArtist.urls')),
    path('userdetails/',include('userdetails.urls'))
]
