from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
'''End Of Import'''
#---------------------------------------------------------------------#


urlpatterns=[



#################################################################################################################################################################################
#URL FOR  LOGOUT
#################################################################################################################################################################################

    #LOGOUT URLS
    #path('^logout/$', views.logout, {"next_page": '/'}),
    

#################################################################################################################################################################################
#URL FOR   DRIVER'S  SIGINUP-PAGE
#################################################################################################################################################################################

    #DRIVER'S  SIGNUP-PAGE!
    #url(r'^accounts/', include('registration.backends.simple.urls')),
    

#################################################################################################################################################################################
#URL FOR  LANDING-PAGE
#################################################################################################################################################################################

    #LANDING Page url!
    
    #This is the landing-page url pattern having the ( ^ )-sign at the start means nothing comes before the defined url which will make it the index page##
    
    url(r'^driver/home',views.landing, name = 'landing'),

#################################################################################################################################################################################
#URL FOR  DRIVER'S HOME-PAGE
#################################################################################################################################################################################

    #DRIVER'S HOME-PAGE url!
    
    #This is the home-page url for driver
    
    url(r'^$',views.driver, name = 'drivers home page'),

#################################################################################################################################################################################
#URL FOR   DRIVER'S PROFILE-PAGE
#################################################################################################################################################################################

    #DRIVER'S PROFILE-PAGE url!
    
    url(r'^driver/profile',views.dprofile, name = 'driver profile page'),

#################################################################################################################################################################################
#URL FOR   DRIVER'S  DESTINATION-PAGE
#################################################################################################################################################################################

    #DRIVER'S  DESTINATION Page url!
    
    url(r'^driver/destination',views.ddestination, name = 'driver pick destination page'),

#################################################################################################################################################################################
#URL FOR   DRIVER'S  CONTACT-PAGE
#################################################################################################################################################################################

    #DRIVER'S  CONTACT-PAGE!
       
    url(r'^driver/contact',views.dcontact, name = 'driver contact-info page'),

#################################################################################################################################################################################
#URL FOR ABOUT-PAGE
#################################################################################################################################################################################

    #ABOUT-PAGE url!
    
    url(r'^about',views.about, name = 'about page for app'),

#################################################################################################################################################################################

]