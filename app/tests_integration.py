from django.test import TestCase
from django.shortcuts import reverse
from app.models import Client, Product, Provider


class HomePageTest(TestCase):
    def test_use_home_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

class ProviderTest(TestCase):

    def test_can_create_provider(self):
            response = self.client.post(
                reverse("providers_form"),
                data={
                "name": "Pepe Gonzales",
                "email": "pepe@hotmail.com",
                "address": "7 entre 13 y 44",
            },
            )
            provider = Provider.objects.all()

            self.assertEqual(len(provider), 1)
            self.assertEqual(provider[0].name, "Pepe Gonzales")
            self.assertEqual(provider[0].email, "pepe@hotmail.com")
            self.assertEqual(provider[0].address, "7 entre 13 y 44")

            self.assertRedirects(response, reverse("providers_repo"))

    def test_validation_errors_create_provider(self):
        response = self.client.post(
            reverse("providers_form"),
            data={},
        )
        self.assertContains(response, "Por favor ingrese un nombre")
        self.assertContains(response, "Por favor ingrese un email") 
        self.assertContains(response, "Por favor ingrese una direccion")
   

#class ClientsTest(TestCase):
#    def test_repo_use_repo_template(self):
#        response = self.client.get(reverse("clients_repo"))
#        self.assertTemplateUsed(response, "clients/repository.html")

#    def test_repo_display_all_clients(self):
#        response = self.client.get(reverse("clients_repo"))
#        self.assertTemplateUsed(response, "clients/repository.html")

#    def test_form_use_form_template(self):
#        response = self.client.get(reverse("clients_form"))
#        self.assertTemplateUsed(response, "clients/form.html")

#    def test_can_create_client(self):


# class HomePageTest(TestCase):
#     def test_use_home_template(self):
#         response = self.client.get(reverse("home"))
#         self.assertTemplateUsed(response, "home.html")


# class ClientsTest(TestCase):
#     def test_repo_use_repo_template(self):
#         response = self.client.get(reverse("clients_repo"))
#         self.assertTemplateUsed(response, "clients/repository.html")

#     def test_repo_display_all_clients(self):
#         response = self.client.get(reverse("clients_repo"))
#         self.assertTemplateUsed(response, "clients/repository.html")

#     def test_form_use_form_template(self):
#         response = self.client.get(reverse("clients_form"))
#         self.assertTemplateUsed(response, "clients/form.html")

#     def test_can_create_client(self):
#         response = self.client.post(
#             reverse("clients_form"),
#             data={
#                 "name": "Juan Sebastian Veron",
#                 "phone": "221555232",
#                 "address": "13 y 44",
#                 "email": "brujita75@hotmail.com",
#             },
#         )
#         clients = Client.objects.all()
#         self.assertEqual(len(clients), 1)

#         self.assertEqual(clients[0].name, "Juan Sebastian Veron")
#         self.assertEqual(clients[0].phone, "221555232")
#         self.assertEqual(clients[0].address, "13 y 44")
#         self.assertEqual(clients[0].email, "brujita75@hotmail.com")

#         self.assertRedirects(response, reverse("clients_repo"))

#     def test_validation_errors_create_client(self):
#         response = self.client.post(
#             reverse("clients_form"),
#             data={},
#         )

#         self.assertContains(response, "Por favor ingrese un nombre")
#         self.assertContains(response, "Por favor ingrese un teléfono")
#         self.assertContains(response, "Por favor ingrese un email")

#     def test_should_response_with_404_status_if_client_doesnt_exists(self):
#         response = self.client.get(reverse("clients_edit", kwargs={"id": 100}))
#         self.assertEqual(response.status_code, 404)

#     def test_validation_invalid_email(self):
#         response = self.client.post(
#             reverse("clients_form"),
#             data={
#                 "name": "Juan Sebastian Veron",
#                 "phone": "221555232",
#                 "address": "13 y 44",
#                 "email": "brujita75",
#             },
#         )

#         self.assertContains(response, "Por favor ingrese un email valido")

#     def test_edit_user_with_valid_data(self):
#         client = Client.objects.create(
#             name="Juan Sebastián Veron",
#             address="13 y 44",
#             phone="221555232",
#             email="brujita75@hotmail.com",
#         )

#         response = self.client.post(
#             reverse("clients_form"),
#             data={
#                 "id": client.id,
#                 "name": "Guido Carrillo",
#             },
#         )

#         # redirect after post
#         self.assertEqual(response.status_code, 302)

#         editedClient = Client.objects.get(pk=client.id)
#         self.assertEqual(editedClient.name, "Guido Carrillo")
#         self.assertEqual(editedClient.phone, client.phone)
#         self.assertEqual(editedClient.address, client.address)
#         self.assertEqual(editedClient.email, client.email)

class ProductsTest(TestCase):
    def test_can_create_product(self):
        response = self.client.post(
            reverse("products_form"),
            data={
                "name": "NombreProducto",
                "type": "TipoProducto",
                "price": 8,
            },
        )
        products = Product.objects.all()
        self.assertEqual(len(products), 1)

        self.assertEqual(products[0].name, "NombreProducto")
        self.assertEqual(products[0].type, "TipoProducto")
        self.assertEqual(products[0].price, 8)

        self.assertRedirects(response, reverse("products_repo"))

    def test_create_product_negative_product(self):
        response = self.client.post(
            reverse("products_form"),
            data={
                "name": "NombreProducto",
                "type": "TipoProducto",
                "price": -8,
            },
        )
        self.assertContains(response, "Por favor ingrese un precio")

    def test_create_product_no_product(self):
        response = self.client.post(
            reverse("products_form"),
            data={
                "name": "NombreProducto",
                "type": "TipoProducto",
                "price": 0,
            },
        )
        self.assertContains(response, "Por favor ingrese un precio")