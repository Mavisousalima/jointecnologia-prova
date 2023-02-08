from django.urls import reverse
from django.test import TestCase

from alvo.models import Alvo
from alvo.forms import AlvoForm


class ListaAlvosTest(TestCase):

    def setUp(self):
        self.alvo = Alvo.objects.create(
                nome="Marcos 1",
                latitude="-10.2491",
                longitude="-48.3243",
                data_expiracao="2030-02-03")

        
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/adicionar/')
        self.assertEqual(response.status_code, 200)


    
    def test_lista_alvos(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    
    def test_remove_alvo_view(self):
        response = self.client.get(reverse('remover_alvo', kwargs={'pk': self.alvo.pk}))

        self.assertFalse(Alvo.objects.filter(pk=self.alvo.pk).exists())

        self.assertEqual(response.status_code, 302)

        self.assertEqual(response.url, reverse('index'))
