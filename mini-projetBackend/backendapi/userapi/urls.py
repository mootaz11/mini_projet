from django.conf.urls import url
from userapi.views import create_user_view,user_details_view,login_user_view,update_user_view,predictImageApple_view,predictImageTomate_view,predictImageStrawberry_view
app_name="user"

urlpatterns=[
    url(r'register/',create_user_view,name="register"),
    url(r'get/',user_details_view,name="get_user"),
    url(r'login',login_user_view,name="login_user"),
    url(r'update/',update_user_view,name="update_user"),
    url(r'predictTomatoImage',predictImageTomate_view,name="predict_Tomato"),
    url(r'predictAppleImage',predictImageApple_view,name="predict_Apple"),
    url(r'predictStrawberryImage',predictImageStrawberry_view,name="predict_strawberry"),
]