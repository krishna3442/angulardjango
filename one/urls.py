'''from django.conf.urls import url
from one.api import Listapi,Cardapi
from django.views.generic import TemplateView


app_name= 'one'

urlpatterns = [
    url(r'^lists$', Listapi.as_view()),
    url(r'^cards$', Cardapi.as_view()),

]'''


from one.api import ListViewSet,CardViewSet
from rest_framework.routers import DefaultRouter

app_name= 'one'

router =DefaultRouter()
router.register(r'lists',ListViewSet)
router.register(r'cards',CardViewSet)

urlpatterns=router.urls
