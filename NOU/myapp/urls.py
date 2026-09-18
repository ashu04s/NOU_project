from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'superadmindesh/',
        views.superadmindesh,
        name='superadmindesh'
    ),

    path(
        'base/',
        views.base,
        name='base'
    ),

    path(
        'students/',
        views.students,
        name='students'
    ),

    path(
        'teachers/',
        views.teachers,
        name='teachers'
    ),

    # ADD SESSION
    path(
        'addsession/',
        views.add_session,
        name='add_session'
    ),

    # SHOW SESSION
    path(
        'showsession/',
        views.show_session,
        name='show_session'
    ),

    # EDIT SESSION
   path(
    'editsession/<int:id>/',
    views.edit_session,
    name='edit_session'
),

    # DELETE SESSION
    path(
        'deletesession/<int:id>/',
        views.delete_session,
        name='delete_session'
    ),
]