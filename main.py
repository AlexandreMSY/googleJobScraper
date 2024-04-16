from jobdescriptionparser.jobdescriptionparser import JobDescriptionParser
from user.userdetails import User
from user.degree import Degree
from datetime import date
from jobattributematcher.jobattributematcher import JobAttributeMatcher

parser = JobDescriptionParser("AIzaSyBznU6qeVaqrVTP08JbXqjXDQXr6qz4RjU")
test = parser.parseJobDescription(
    """
        ATIVIDADES: A pessoa estagiária será treinada para atuar com várias linguagens de programação, em atividades full stack e agindo em diferentes projetos com a supervisão de um Analista. Atuará com Flutter; Swift; Kotlin; C#.net; Node.js; Angular e JavaScript em sistemas de recomendação e Data Science, além de arquiteturas distribuídas com aplicativos.

        REQUISITOS: Inglês nível técnico (Será testado posteriormente); Conhecimento em lógica de programação; Máquina para trabalhar de casa

        DEVERÁ ESTAR CURSANDO: Deve estar no PENÚLTIMO ou ÚLTIMO ano dos seguintes cursos: Análise e Desenvolvimento de Sistemas; Ciência da Computação; Engenharia de Software ou Sistemas da Informação.

        BENEFÍCIOS: Tíquete Refeição

        REGIME DE CONTRATAÇÃO: Estágio

        INFORMAÇÕES ADICIONAIS: Jornada de segunda a sexta, por 30 horas semanais. Atuação home-office. Possibilidade de efetivação. Bolsa auxílio e VR de R$600,00.

        IDIOMAS: Inglês - Intermediário
    """
)

user = User(None, ["HTML", "CSS", "JavaScript", "mysql"], [Degree("test", "test", date(1999,8,2))], None, ["inglês"])
attributeMatcher = JobAttributeMatcher(user= user, jobAttributes=test)

#print(test)
print(attributeMatcher.attributesMatched())
