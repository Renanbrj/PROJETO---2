# Class
# UniversidadeFluxo

# Aluno, Disciplina , Professor , Sala de aula

class Fluxo:       
  def __init__(self, aluno, disciplina, professor, sala_de_aula ):
        self.aluno = aluno 
        self.disciplina = disciplina  
        self.professor = professor
        self.sala_de_aula = sala_de_aula
  pass

aluno1 = Fluxo('Renan','Física de Reatores','Su Jian','G205')
aluno2 = Fluxo('Isadora','Transcal','Ademir','G201') 
aluno3 = Fluxo('Alanna','Cálculo III','Vlad','A201') 
print(aluno1.aluno,aluno1.disciplina,aluno1.professor,aluno1.sala_de_aula)
print(aluno2.aluno,aluno2.disciplina,aluno2.professor,aluno2.sala_de_aula) 
print(aluno3.aluno,aluno3.disciplina,aluno3.professor,aluno3.sala_de_aula)
 












