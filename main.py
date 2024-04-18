from jobdescriptionparser.jobdescriptionparser import JobDescriptionParser
from user.userdetails import User
from user.degree import Degree
from datetime import date
from jobattributematcher.jobattributematcher import JobAttributeMatcher
from dotenv import load_dotenv
import os

load_dotenv(".env")


parser = JobDescriptionParser(os.getenv("GEMINI_API_KEY"))
test = parser.parseJobDescription(
    """
        DESCRIÇÃO

        Suas Principais Atividades

        Desenvolvimento de projetos de websites , utilizando-se das ferramentas HTML e JavaScript;
        Plataformas de gerenciamento de conteúdo na web: Fatwire, Websphere Content Management, Web Publishing, padrões HTML e Internacionalização;
        Atuação em projetos de desenvolvimento / roll-out de Web Sites ; criação/gerenciamento de conteúdo;
        Usuário da ferramenta SharePoint;

        Experiência Necessária

        Necessária Programação: JavaScript, Java, HTML;

        Desejável atuação em produção de catálogo de produtos; plataformas de catálogo de dados/produtos;

        Formação superior/técnica completa na área de TI/Sistemas.

        Local de trabalho: São Paulo, SP
        Regime de contratação de tipo: Efetivo – CLT
        Jornada: Período Integral
        Área e especialização profissional: Informática, TI, Telecomunicações - Programador / Desenvolvedor
        Nível hierárquico: Especialista

        REQUISITOS

        Escolaridade Mínima: Ensino Superior

        HABILIDADES

        Web Publishing
        Websphere Content Management
        Java
        JavaScript
        Fatwire
        Web Sites
        SharePoint
        HTML

        BENEFÍCIOS

        Trabalho Remoto
        Assistência médica
        Assistência odontológica
        Vale-refeição
        Vale-alimentação
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

# print(test)
print(attributeMatcher.attributesMatched())
