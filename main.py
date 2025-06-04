import data
import helpers


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def test_set_route(self):
        # Adicionar implementação em S8
        print("Função criada para definir a rota")
        pass

    def test_select_plan(self):
        # Adicionar implementação em S8
        print("Função criada para selecionar o plano")
        pass

    def test_fill_phone_number(self):
        # Adicionar implementação em S8
        print("Função criada para preencher o número de telefone")
        pass

    def test_fill_card(self):
        # Adicionar implementação em S8
        print("Função criada para preencher o cartão")
        pass

    def test_comment_for_driver(self):
        # Adicionar implementação em S8
        print("Função criada para adicionar comentário para o motorista")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar implementação em S8
        print("Função criada para o pedido de cobertor e lenços")
        pass

    def test_order_2_ice_creams(self):
        # Adicionar implementação em S8
        number_of_ice_creams = 2
        for count in range(number_of_ice_creams):
            print("Função criada para definir o pedido do sorvete")
        pass

    def test_car_search_model_appears(self):
        # Adicionar implementação em S8
        print("Função criada para verificar se o modelo do carro aparece")
        pass
