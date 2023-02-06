from django.urls import reverse
from django.test import TestCase

from alvo.models import Alvo


class ListaAlvosTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        alvos = 3
        for alvo_id in range(alvos):
            Alvo.objects.create(
                nome=f"Marcos {alvo_id}",
                latitude="-10.2491",
                longitude="-48.3243",
                data_expiracao="2030-02-03"
            )

        
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/adicionar/')
        self.assertEqual(response.status_code, 200)

    
    def test_lista_alvos(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')