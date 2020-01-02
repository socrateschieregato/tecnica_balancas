import json

import pytest

from django.urls import reverse


@pytest.mark.django_db
class TestSerializer:

    def test_company(self, client, company):
        response = client.get(reverse('empresa-list'))
        companys = json.loads(response.content)
        assert len(companys) == 1
        assert companys[0]['cpf_cnpj'] == company.cpf_cnpj
        assert companys[0]['ie'] == company.ie
        assert companys[0]['nome_razao'] == company.nome_razao
        assert companys[0]['nome_fantasia'] == company.nome_fantasia
        assert companys[0]['email'] == company.email
