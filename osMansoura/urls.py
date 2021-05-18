from django.urls import path
from osMansoura import views

urlpatterns = [
    path('', views.home),
    path('student/<studentId>', views.getStudent),
    path('allstudents/', views.getAllStudents),
    path('create/student/', views.createStudent),
    path('edit/student/<studentId>', views.editStudent),
    path('delete/student/<studentId>', views.deleteStudent)

]   