# Class
# UniversidadeFluxo

# Aluno, Disciplina , Professor , Sala de aula

'''A Classe UniFluxo é classe pai, as restantes são todas subclasses '''

class UniFluxo:
        def __init__(self, instituicao='Universidade Fluxo'):
                self.instituicao = instituicao

        def mostrar(self):
                print(f'Estuda em: {self.instituicao}')
class Membros(UniFluxo):                                                  # A classe "Membros" é a classe onde há o cadastro inicial com o Nome e a Idade
        def __init__(self, *args):
                super().__init__()
                self.nome = args[0]
                self.idade = args[1]

        def mostrar(self):
                        print(30 * '#')
                        print(f'{self.nome} tem {self.idade} de idade')
                        super().mostrar()
                        
                         
class Professor(Membros):                                              # A classe "Professor" é a classe onde há o cadastro de todo professor e tudo o que remete à ele
        def __init__(self, cargo, sala, horario , dia,*args):  
                super().__init__(*args)
                self.cargo = cargo
                self.sala = sala
                self.horario = horario
                self.dia = dia
        def mostrar(self):
                        super().mostrar()
                        print(f'É docente de :{self.cargo}')

class Aluno(Membros):                                                    # A classe "Aluno" é a classe que representa todos os estudantes e algumas informações sobre eles 
        def __init__(self, curso ,*args):
                super().__init__(*args)
                self.curso = curso 

        def mostrar(self):
                        super().mostrar()
                        print(f'Cursa {self.curso}')
                        print(30 *'#')

professor1 = Professor('Física I', 'A201', '10:30', 'Segunda-Feira', 'Valdecir', 31)
professor2 = Professor('Física II', 'B114', '14:30', 'Terça-Feira', 'Juremar', 31)
professor3 = Professor('Física III', 'B037', '19:30', 'Quarta-Feira', 'Daciolo', 31)
aluno1 = Aluno('Engenharia Nuclear', 'Renan Ferreira', 19)
aluno2 = Aluno('Engenharia de Produção', 'Matheus Melo', 20)
aluno3 = Aluno('Engenharia Nuclear', 'Isadora Campolina', 19)

membros = [professor1, professor2, professor3,aluno1,aluno2,aluno3]

for membro in membros:
        membro.mostrar()



 
