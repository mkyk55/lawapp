from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about', views.about_page, name='about'),
    path('contact', views.contact_us, name='contact'),
    path('criminal-cases', views.criminal_cases, name='criminal'),
    path('civil-cases', views.civil_cases, name='civil'),
    path('matrimonial-cases', views.matrimonial_cases, name='matrimonial'),
    path('family-cases', views.family_cases, name='family'),
    path('cyber-cases', views.cyber_cases, name='cyber'),
    path('mediation', views.mediation_cases, name='mediation'),
    path('negotiable', views.negotiable_cases, name='negotiable'),
    path('labour', views.labour_cases, name='labour'),
    path('team', views.team, name='team'),

] 