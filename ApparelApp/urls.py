from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path('Login.html', views.Login, name="Login"), 
	       path('AdminLogin.html', views.AdminLogin, name="AdminLogin"), 
	       path('Register.html', views.Register, name="Register"),
	       path('Signup', views.Signup, name="Signup"),
	       path('UserLogin', views.UserLogin, name="UserLogin"),
	       path('AdminLoginAction', views.AdminLoginAction, name="AdminLoginAction"),
	       path('AddProduct.html', views.AddProduct, name="AddProduct"),
	       path('AddProductData', views.AddProductData, name="AddProductData"),
	       path('ViewOrders.html', views.ViewOrders, name="ViewOrders"),
	       path('ItemSearch.html', views.ItemSearch, name="ItemSearch"),
	       path('SearchItemData', views.SearchItemData, name="SearchItemData"),
	       path('Feedback.html', views.Feedback, name="Feedback"),
	       path('FeedbackAction', views.FeedbackAction, name="FeedbackAction"),
	       path('ViewFeedback', views.ViewFeedback, name="ViewFeedback"),
	       path('AddCart', views.AddCart, name="AddCart"),
	       path('ViewCart', views.ViewCart, name="ViewCart"),
	       path('RemoveCart', views.RemoveCart, name="RemoveCart"),
	       path('TrackOrder', views.TrackOrder, name="TrackOrder"),
	       path('Checkout', views.Checkout, name="Checkout"),
	       path('PaymentAction', views.PaymentAction, name="PaymentAction"),
	       path('About.html', views.About, name="About"),
           path('ForgotPassword.html', views.ForgotPassword, name="ForgotPassword"),
]