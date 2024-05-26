from django.test import TestCase
from django.shortcuts import reverse
from app.models import Client
from app.models import Vet


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

# Test de Veterinario
class VetsTest(TestCase):
    def test_can_create_vet(self):
            response = self.client.post(
                reverse("vets_form"),
                data={
                    "name": "Joaquin Munos",
                    "phone": "22165438",
                    "address": "20 y 60",
                    "email": "joaquin10@hotmail.com",
                    "especialidad": "general",
                },
            )
            vets = Vet.objects.all()
            self.assertEqual(len(vets), 1)

            self.assertEqual(vets[0].name, "Joaquin Munos")
            self.assertEqual(vets[0].phone, "22165438")
            self.assertEqual(vets[0].address, "20 y 60")
            self.assertEqual(vets[0].email, "joaquin10@hotmail.com")
            self.assertEqual(vets[0].speciality, "general")

            self.assertRedirects(response, reverse("vets_repo"))

    def test_validation_invalid_especialidad(self):
            response = self.client.post(
                reverse("vets_form"),
                data={
                    "name": "Joaquin Munos",
                    "phone": "22165438",
                    "address": "20 y 60",
                    "email": "joaquin10@hotmail.com",
                    "especialidad": "",
                },
            )

            self.assertContains(response, "Por favor seleccione una especialidad")