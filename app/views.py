from django.shortcuts import get_object_or_404, redirect, render, reverse

from .models import Breed, City, Client, Medicine, Pet, Product, Provider, Vet


def home(request):
    """Renderiza la página de inicio."""
    return render(request, "home.html")


def clients_repository(request):
    """Renderiza la página con la lista de clientes."""
    clients = Client.objects.all()
    return render(request, "clients/repository.html", {"clients": clients})


def clients_form(request, id=None):
    """Renderiza y maneja el formulario para crear o editar clientes."""
    city = City.choices
    if request.method == "POST":
        client_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if client_id == "":
            saved, errors = Client.save_client(request.POST)
        else:
            client = get_object_or_404(Client, pk=client_id)
            saved, errors = client.update_client(request.POST)

        if saved:
            return redirect(reverse("clients_repo"))

        return render(
            request, "clients/form.html", {"errors": errors,
                                           "client": request.POST,
                                           "cities": city},

        )

    client = None
    if id is not None:
        client = get_object_or_404(Client, pk=id)

    return render(request, "clients/form.html", {"client": client, "cities": city})


def clients_delete(request):
    """Elimina un cliente y redirige al repositorio de clientes."""
    client_id = request.POST.get("client_id")
    client = get_object_or_404(Client, pk=int(client_id))
    client.delete()

    return redirect(reverse("clients_repo"))


def pets_repository(request):
    """Renderiza la página con la lista de mascotas."""
    pets = Pet.objects.all()
    return render(request, "pets/repository.html", {"pets": pets})


def pets_form(request, id=None):
    """Renderiza y maneja el formulario para crear o editar mascotas."""
    breed = Breed.choices
    if request.method == "POST":
        pet_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if pet_id == "":
            saved, errors = Pet.save_pet(request.POST)
        else:
            pet = get_object_or_404(Pet, pk=pet_id)
            pet.update_pet(request.POST)

        if saved:
            return redirect(reverse("pets_repo"))

        return render(
            request, "pets/form.html", {"errors": errors,
                                        "pet": request.POST,
                                        "breeds": breed},
        )

    pet = None
    if id is not None:
        pet = get_object_or_404(Pet, pk=id)

    return render(request, "pets/form.html", {"pet": pet, "breeds": breed})


def pets_delete(request):
    """Elimina una mascota y redirige al repositorio de mascotas."""
    pet_id = request.POST.get("pet_id")
    pet = get_object_or_404(Pet, pk=int(pet_id))
    pet.delete()

    return redirect(reverse("pets_repo"))


# Vista para mostrar todos los medicamentos en el repositorio
def medicines_repository(request):
    """Renderiza la página con la lista de medicamentos."""
    medicines = Medicine.objects.all()
    return render(request, "medicines/repository.html", {"medicines": medicines})

# Vista para el formulario de creación/edición de medicamentos


def medicines_form(request, id=None):
    """Renderiza y maneja el formulario para crear o editar medicamentos."""
    if request.method == "POST":
        medicine_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if medicine_id == "":
            # Guarda un nuevo medicamento
            saved, errors = Medicine.save_medicine(request.POST)
        else:
            # Actualiza un medicamento existente
            medicine = get_object_or_404(Medicine, pk=medicine_id)
            medicine.update_medicine(request.POST)

        if saved:
            # Redirige a la página del repositorio de medicamentos
            return redirect(reverse("medicines_repo"))

        # Renderiza el formulario con errores si no se pudo guardar
        return render(
            request, "medicines/form.html", {"errors": errors,
                                             "medicine": request.POST},
        )

    # Obtiene el medicamento si se está editando
    medicine = None
    if id is not None:
        medicine = get_object_or_404(Medicine, pk=id)

    # Renderiza el formulario con los datos del medicamento
    return render(request, "medicines/form.html", {"medicine": medicine})

# Vista para eliminar un medicamento


def medicines_delete(request):
    """Elimina un medicamento y redirige al repositorio de medicamentos."""
    medicine_id = request.POST.get("medicine_id")
    medicine = get_object_or_404(Medicine, pk=int(medicine_id))
    medicine.delete()

    # Redirige a la página del repositorio de medicamentos
    return redirect(reverse("medicines_repo"))


def providers_repository(request):
    """Renderiza la página con la lista de proveedores."""
    providers = Provider.objects.all()
    return render(request, "providers/repository.html", {"providers": providers})


def providers_form(request, id=None):
    """Renderiza y maneja el formulario para crear o editar proveedores."""
    if request.method == "POST":
        provider_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if provider_id == "":
            saved, errors = Provider.save_provider(request.POST)
        else:
            provider = get_object_or_404(Provider, pk=provider_id)
            provider.update_provider(request.POST)

        if saved:
            return redirect(reverse("providers_repo"))

        return render(
            request, "providers/form.html", {"errors": errors,
                                             "provider": request.POST},
        )

    provider = None
    if id is not None:
        provider = get_object_or_404(Provider, pk=id)

    return render(request, "providers/form.html", {"provider": provider})


def providers_delete(request):
    """Elimina un proveedor y redirige al repositorio de proveedores."""
    provider_id = request.POST.get("provider_id")
    provider = get_object_or_404(Provider, pk=int(provider_id))
    provider.delete()

    return redirect(reverse("providers_repo"))


def products_repository(request):
    """Renderiza la página con la lista de productos."""
    products = Product.objects.all()
    return render(request, "products/repository.html", {"products": products})


def products_form(request, id=None):
    """Renderiza y maneja el formulario para crear o editar productos."""
    if request.method == "POST":
        product_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if product_id == "":
            saved, errors = Product.save_product(request.POST)
        else:
            product = get_object_or_404(Product, pk=product_id)
            saved, errors = product.update_product(request.POST)

        if saved:
            return redirect(reverse("products_repo"))

        return render(
            request, "products/form.html", {"errors": errors,
                                            "product": request.POST},
        )

    product = None
    if id is not None:
        product = get_object_or_404(Product, pk=id)

    return render(request, "products/form.html", {"product": product})


def products_delete(request):
    """Elimina un producto y redirige al repositorio de productos."""
    product_id = request.POST.get("product_id")
    product = get_object_or_404(Product, pk=int(product_id))
    product.delete()

    return redirect(reverse("products_repo"))


# Funciones de Vet
def vets_repository(request):
    """Renderiza la página con la lista de veterinarios."""
    vets = Vet.objects.all()
    return render(request, "vets/repository.html", {"vets": vets})


def vets_form(request, id=None):
    """Renderiza y maneja el formulario para crear o editar veterinarios."""
    if request.method == "POST":
        vet_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if vet_id == "":
            saved, errors = Vet.save_vet(request.POST)
        else:
            vet = get_object_or_404(Vet, pk=vet_id)
            vet.update_vet(request.POST)

        if saved:
            return redirect(reverse("vets_repo"))

        return render(
            request, "vets/form.html", {"vet_errors": errors,
                                        "vet": request.POST},
        )

    vet = None
    if id is not None:
        vet = get_object_or_404(Vet, pk=id)

    return render(request, "vets/form.html", {"vet": vet})


def vets_delete(request):
    """Elimina un veterinario y redirige al repositorio de veterinarios."""
    vet_id = request.POST.get("vet_id")
    vet = get_object_or_404(Vet, pk=int(vet_id))
    vet.delete()

    return redirect(reverse("vets_repo"))
