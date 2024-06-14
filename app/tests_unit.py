from django.test import TestCase

from app.models import Breed, Client, Medicine, Pet, Product, Provider, Vet


class ProviderModelTest(TestCase):
    def test_update_provider_address_with_error(self):
        Provider.save_provider(
            {
                "name": "Pepe Gonzales",
                "email": "pepe@hotmail.com",
                "address": "7 entre 13 y 44",
            }
        )
        provider = Provider.objects.get(pk=1)
        
        self.assertEqual(provider.address, "7 entre 13 y 44")
        
        # Intentar actualizar la dirección con un valor inválido (cadena vacía)
        success, errors = provider.update_provider({"address": ""})

        # Verificar que la actualización no fue exitosa
        self.assertFalse(success) 

        # Verificar que se generaron errores 
        self.assertIsNotNone(errors)  


# class ClientModelTest(TestCase):
#     def test_can_create_and_get_client(self):
#         Client.save_client(
#             {
#                 "name": "Juan Sebastian Veron",
#                 "phone": "221555232",
#                 "address": "13 y 44",
#                 "email": "brujita75@hotmail.com",
#             }
#         )
#         clients = Client.objects.all()
#         self.assertEqual(len(clients), 1)

#         self.assertEqual(clients[0].name, "Juan Sebastian Veron")
#         self.assertEqual(clients[0].phone, "221555232")
#         self.assertEqual(clients[0].address, "13 y 44")
#         self.assertEqual(clients[0].email, "brujita75@hotmail.com")

#     def test_can_update_client(self):
#         Client.save_client(
#             {
#                 "name": "Juan Sebastian Veron",
#                 "phone": "221555232",
#                 "address": "13 y 44",
#                 "email": "brujita75@hotmail.com",
#             }
#         )
#         client = Client.objects.get(pk=1)

#         self.assertEqual(client.phone, "221555232")

#         client.update_client({"phone": "221555233"})

#         client_updated = Client.objects.get(pk=1)

#         self.assertEqual(client_updated.phone, "221555233")

#     def test_update_client_with_error(self):
#         Client.save_client(
#             {
#                 "name": "Juan Sebastian Veron",
#                 "phone": "221555232",
#                 "address": "13 y 44",
#                 "email": "brujita75@hotmail.com",
#             }
#         )
#         client = Client.objects.get(pk=1)

#         self.assertEqual(client.phone, "221555232")

#         client.update_client({"phone": ""})

#         client_updated = Client.objects.get(pk=1)

#         self.assertEqual(client_updated.phone, "221555232")

class ClientModelTest(TestCase):
    def test_can_create_and_get_client(self):
        response = Client.save_client(
            {
                "name": "234#~$",
                "phone": "221555232",
                "address": "13 y 44",
                "email": "brujita75@hotmail.com",
            }
        )
        clients = Client.objects.all()
        self.assertEqual(len(clients),0)
        self.assertEqual(response[1]["name"],"El nombre solo puede contener letras y espacios")



class MedicineModelTest(TestCase):
    def test_can_create_and_get_medicine(self):
        success, errors = Medicine.save_medicine(
            {
                "name": "Amoxicilina",
                "description": "Antibiotico de amplio espectro",
                "dose": "6",
            }
        )
        self.assertTrue(success)
        self.assertIsNone(errors)
        
        medicines = Medicine.objects.all()
        self.assertEqual(len(medicines), 1)

        self.assertEqual(medicines[0].name, "Amoxicilina")
        self.assertEqual(medicines[0].description, "Antibiotico de amplio espectro")
        self.assertEqual(medicines[0].dose, 6)

    def test_update_medicine_with_invalid_dose_zero(self):
        Medicine.save_medicine(
            {
                "name": "Amoxicilina",
                "description": "Antibiotico de amplio espectro",
                "dose":"0",
            }
        )
        medicinas = Medicine.objects.all()
        self.assertEqual(len(medicinas), 0)

    def test_update_medicine_with_invalide_dose(self):
        response = Medicine.save_medicine(
            {
                "name": "Amoxicilina",
                "description": "Antibiotico de amplio espectro",
                "dose":"11",
            }
        )
        medicinas=Medicine.objects.all()
        self.assertEqual(len(medicinas),0)
        self.assertEqual(response[1]['dose'],'La dosis debe estar entre 1 a 10')


    def test_update_medicine_with_invalid_dose_negative(self):
        response = Medicine.save_medicine(
            {
                "name": "Amoxicilina",
                "description": "Antibiotico de amplio espectro",
                "dose":"-5",
            }
        )
        medicinas = Medicine.objects.all()
        self.assertEqual(len(medicinas), 0)
        self.assertEqual(response[1]['dose'],'La dosis debe ser un número entero positivo')

        
#Test de veterinario
class VetModelTest(TestCase):
    def test_can_create_and_get_vet(self):
        Vet.save_vet(
            {
                "name": "Tomas Sbert",
                "phone": "2314557290",
                "address": "La Plata 43",
                "email": "tomasbret_dx@hotmail.com",
                "especialidad": "general",
            }
        )

        vets = Vet.objects.all()

        self.assertEqual(len(vets), 1)

        self.assertEqual(vets[0].name, "Tomas Sbert")
        self.assertEqual(vets[0].phone, "2314557290")
        self.assertEqual(vets[0].address, "La Plata 43")
        self.assertEqual(vets[0].email, "tomasbret_dx@hotmail.com")
        self.assertEqual(vets[0].speciality, "general")

    def test_can_delete_vet(self):
        vet = Vet.objects.create(
            name="Tomas Sbert",
            phone="2314557290",
            address="La Plata 43",
            email="tomasbret_dx@hotmail.com",
            speciality="general"
        )

        # Eliminar el veterinario
        vet.delete()

        # Verificar que el veterinario haya sido eliminado
        vets = Vet.objects.all()
        self.assertEqual(len(vets), 0)

        
    def test_can_create_and_get_speciality(self):
        response = Vet.save_vet(
            {
                "name": "234#~$",
                "phone": "221555232",
                "address": "13 y 44",
                "email": "brujita75@hotmail.com",
                "especialidad":"",
            }
        )
        vets = Vet.objects.all()
        self.assertEqual(len(vets),0)
        self.assertEqual(response[1]["especialidad"],"Por favor seleccione una especialidad")
        
class ProductModelTest(TestCase):
    def test_can_create_and_get_product(self):
        Product.save_product(
            {
                "name": "NombreProducto",
                "type": "TipoProducto",
                "price": 8,
            }
        )

        products = Product.objects.all()
        self.assertEqual(len(products), 1)

        self.assertEqual(products[0].name, "NombreProducto")
        self.assertEqual(products[0].type, "TipoProducto")
        self.assertEqual(products[0].price, 8)

    def test_create_product_with_negative_product(self):
        response = Product.save_product(
            {
                "name": "NombreProducto",
                "type": "TipoProducto",
                "price": -8,
            }
        )

        products = Product.objects.all()
        self.assertEqual(len(products), 0)
        self.assertEqual(response[1]["price"], "El precio debe ser mayor a cero")


    def test_create_product_with_no_product(self):
        response = Product.save_product(
            {
                "name": "NombreProducto",
                "type": "TipoProducto",
                "price": 0,
            }
        )
        
        products = Product.objects.all()
        self.assertEqual(len(products), 0)
        self.assertEqual(response[1]["price"], "El precio debe ser mayor a cero")


# Agrego test unitarios para punto 5 actividad 3
# cambios por nueva rama  feature-agregaropcionesrazamascota
class PetModelTest(TestCase):
    def setUp(self):
        # Crea un cliente para ser el dueño de la mascota
        self.client = Client.objects.create(
            name="Test Client", phone="221555232", email="test@test.com", address="13 y 44")

    def test_create_pet(self):
        # Crea una nueva mascota
        pet = Pet.objects.create(
            name="Test Pet", breed=Breed.DOG, birthday="2022-01-01")

        # Verifica que la mascota se haya guardado en la base de datos
        self.assertEqual(Pet.objects.count(), 1)
        self.assertEqual(Pet.objects.first(), pet)

    def test_breed_choices(self):
        # Crea mascotas con cada opción de raza
        pet_dog = Pet.objects.create(
            name="Dog Pet", breed=Breed.DOG, birthday="2022-01-01")
        pet_cat = Pet.objects.create(
            name="Cat Pet", breed=Breed.CAT, birthday="2022-01-01")
        pet_bird = Pet.objects.create(
            name="Bird Pet", breed=Breed.BIRD, birthday="2022-01-01")

        # Verifica que las mascotas se hayan guardado con las razas correctas
        self.assertEqual(pet_dog.breed, Breed.DOG)
        self.assertEqual(pet_cat.breed, Breed.CAT)
        self.assertEqual(pet_bird.breed, Breed.BIRD)
