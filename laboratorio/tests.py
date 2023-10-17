from django.test import TestCase
from django.urls import reverse

from .models import Laboratorio
# Create your tests here.


class LaboratorioTests(TestCase):
    databases = '__all__'
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(
            nombre='Laboratorio1', 
            ciudad="Ciudad 1", 
            pais="País 1", 
            )

    def test_model_content(self):
        self.assertEqual(self.laboratorio.nombre, "Laboratorio1")
        self.assertEqual(self.laboratorio.ciudad, "Ciudad 1")
        self.assertEqual(self.laboratorio.pais, "País 1")
    
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/insertar/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("mostrar"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mostrar.html')
        self.assertContains(response, "Información de Laboratorios")