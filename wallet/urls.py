from django.conf.urls import url, include
from views import home, add,login,logout,passbook,signup,transfer

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^add$', add, name='add'),
    url(r'^login$', login, name='login'),
    url(r'^signup$', signup, name='signup'),
    url(r'^logout$', logout, name='logout'),
    url(r'^passbook$', passbook, name='passbook'),
    url(r'^transfer$', transfer, name='transfer'),
]
