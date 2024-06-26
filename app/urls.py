from django.urls import path

from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("clientes/", view=views.clients_repository, name="clients_repo"),
    path("clientes/nuevo/", view=views.clients_form, name="clients_form"),
    path("clientes/editar/<int:id>/",
         view=views.clients_form, name="clients_edit"),
    path("clientes/eliminar/", view=views.clients_delete, name="clients_delete"),
    
    path("productos/", view=views.products_repository, name="products_repo"),
    path("productos/nuevo/", view=views.products_form, name="products_form"),
    path("productos/editar/<int:id>/",
         view=views.products_form, name="products_edit"),
    path("productos/eliminar/", view=views.products_delete, name="products_delete"),

    # URLS del modelo Vet
    path("veterinario/", view=views.vets_repository, name="vets_repo"),
    path("veterinario/nuevo/", view=views.vets_form, name="vets_form"),
    path("veterinario/editar/<int:id>/", view=views.vets_form, name="vets_edit"),
    path("veterinario/eliminar/", view=views.vets_delete, name="vets_delete"),

    path("proveedores/", view=views.providers_repository, name="providers_repo"),
    path("proveedores/nuevo/", view=views.providers_form, name="providers_form"),
    path("proveedores/editar/<int:id>/",
         view=views.providers_form, name="providers_edit"),
    path("proveedores/eliminar/", view=views.providers_delete,
         name="providers_delete"),
    path("medicamentos/", view=views.medicines_repository, name="medicines_repo"),
    path("medicamentos/nuevo/", view=views.medicines_form, name="medicines_form"),
    path("medicamentos/editar/<int:id>/",
         view=views.medicines_form, name="medicines_edit"),
    path("medicamentos/eliminar/",
         view=views.medicines_delete, name="medicines_delete"),

    # agregamos las urls de nuestras views para mascotas
    path("mascotas/", view=views.pets_repository, name="pets_repo"),
    path("mascotas/nuevo/", view=views.pets_form, name="pets_form"),
    path("mascotas/editar/<int:id>/",
         view=views.pets_form, name="pets_edit"),
    # path('pets/form/<int:pet_id>/', views.pets_form, name='pets_edit'),
    path("mascotas/eliminar/", view=views.pets_delete, name="pets_delete"),

]
