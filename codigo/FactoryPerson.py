from codigo.Background import Background

class FactoryPerson:

    @staticmethod
    def get_personagem(personagem_name:str, position=(0,0)):
        match personagem_name:
            case 'imglevelfull':
                return [Background('imglevelfull', position)]