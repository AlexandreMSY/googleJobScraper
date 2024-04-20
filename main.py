from geminiTools.job_description_parser import JobDescriptionParser
from user.userdetails import User
from user.degree import Degree
from datetime import date
from jobattributematcher.job_attribute_matcher import JobAttributeMatcher
from dotenv import load_dotenv
import os

load_dotenv(".env")


parser = JobDescriptionParser(os.getenv("GEMINI_API_KEY"))
test = parser.parseJobDescription(
    """
        A Aliare está entre as maiores empresas de software para o agronegócio do país. Nascemos no agro e somos especialistas em levar tecnologia para gestão de empresas e propriedades rurais.

        Estamos com nossos clientes, pra fazer o campo acontecer. Temos orgulho de ajudar a construir o presente e o futuro do agronegócio.

        Responsabilidades e atribuições
        • Auxiliar nos processos de desenvolvimento de novos produtos e na manutenção dos sistemas já existentes, e mantendo os sistemas de acordo com metodologias e técnicas pré-estabelecidas, visando atender aos objetivos estabelecidos quanto a qualidade, custos e prazos.

        Requisitos e qualificações
        • Graduação completa ou em andamento em sistemas de informação, ciência da computação, sistemas para internet ou afins.
        • Desejável experiência em GeneXus.

        Informações adicionais

        O que a Aliare proporciona?!

        Um time integrado e preparado para novos desafios, que atua com credibilidade e transparência, com objetivo de evoluirmos de forma contínua para facilitar o trabalho de quem alimenta o mundo. Priorizando sempre em nossas ações a ética, o relacionamento, a realização, o comprometimento e inovação.

        Plano de Saúde Nacional;

        Plano Odontológico Nacional;

        Seguro de Vida;

        Parceria com academias;

        Vale Flexível, Alimentação/Refeição;

        Vale Transporte;

        Auxílio Deslocamento/ Home Office;

        Universidade Corporativa;

        Auxílio Educação;

        Premiação por atingimento de resultado anuais;

        Bônus por Indicação;

        Premiação por tempo de casa;

        Presente aos filhos recém-nascidos dos #Aliados;

        Presente exclusivo no seu aniversário;

        Em nossas unidades, você vai encontrar um ambiente super legal, e claro que não poderia faltar, aquele café quentinho .

        Nós somos um ecossistema de tecnologia com um só : facilitar o trabalho de quem alimenta o mundo!

        E o que isso significa?

        Que por meio da inovação, tecnologia e pessoas apaixonadas pelo que fazem, estamos ultrapassando as fronteiras e moldando o agronegócio do futuro.

        Nos tornaremos a 1ª Big Tech Agro do Brasil! E para isso, estamos reunindo verdadeiros #Aliados para trilharem essa trajetória de conquistas com a gente. Aqui, valorizamos ideias diferentes, pois é como reproduzimos resultados únicos. Queremos pessoas dispostas a abraçarem o nosso Jeito Aliare de Ser.

        Bateu aquela curiosidade para entender um pouco mais sobre nossa cultura e dia-a-dia? Confere um spoiler do que te espera por aqui Aliverso particular

        E tem mais! Já somamos:

        6 unidades físicas espalhadas pelo Brasil

        +900 colaboradores

        +50% do share de mercado de distribuição de insumos agrícolas

        +65 mil usuários

        +5 mil estabelecimentos

        Atuação em 22 estados + DF

        Perde tempo não, faça parte do nosso Aliverso
    """
)

user = User(
    None,
    ["HTML", "CSS", "JavaScript", "mysql", "Java"],
    [Degree("Análise de sistemas", "test", date(1999, 8, 2))],
    None,
    ["inglês"],
)
attributeMatcher = JobAttributeMatcher(user=user, jobAttributes=test)
print(attributeMatcher.attributesMatched())
