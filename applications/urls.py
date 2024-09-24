from django.urls import path
from applications.views import index

urlpatterns = [
    path('application/', index, name='application_form'),
    #  path('thank_you/', thank_you.form_view, name='submit'),

]
