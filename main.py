from geminiTools.job_description_parser import JobDescriptionParser
from user.userdetails import User
from user.degree import Degree
from datetime import date
from jobattributematcher.job_attribute_matcher import JobAttributeMatcher
from dotenv import load_dotenv
import os

load_dotenv(".env")

descriptionParser = JobDescriptionParser(os.getenv("GEMINI_API_KEY"))
json = descriptionParser.parseJobDescription(
    """
        Estágio

        Sobre F1 Commerce

        F1 Commerce é uma empresa que atua no mercado de plataforma de ecommerce há mais de 14 anos no mercado.

        A empresa fornece soluções de ecommerce para empresas de grande porte, atendendo clientes como: JBL, Sanremo, Positivo, Compaq, VAIO, Alpar, Frahm dentre outros.

        Estágio Desenvolvimento FrontEnd HTML/CSS/JS

        A vaga é para atuação no desenvolvimento de interfaces de lojas virtuais.

        Localidade:

        Durante Pandemia:

        Remoto

        Pós Pandemia:

        Flexível

        Nível:

        Estágiário

        Contratação:

        Estágio

        Salário:

        R$ 1.200

        Carga Horária:

        Estágio: 30 horas / semana

        Benefícios:

        » Vale Alimentação ou Vale Refeição

        » Vale Transporte ou estacionamento

        » Seguro de vida

        » Auxílio Home Office (durante pandemia)

        » Desconto em Graduação, Pós-Graduação, Mestrado na UNISINOS

        Atividades:
        • Codificação de interfaces em HTML/CSS/JS para lojas virtuais a partir de layouts em AI/PSD/PNG

        Requisitos:
        • Disposição para enfrentar e implementar a criatividade de designers
        • Superior em curso (independente do semestre) ou curso técnico ligado a área
        • Capacidade de desenvolvimento HTML sem a utilização de software WYSIWYG
        • CSS
        • Software de corte e edição de imagens (Photoshop/Fireworks)
        • Javascript

        Requisitos obrigatórios:
        • Comprometimento
        • Bom humor
        • Dinamismo
        • Boa capacidade de relacionamento interpessoal (trabalho em equipe)
        • Vontade de aprender
        • Capacidade de concentração e foco na resolução de tarefas

        É Diferencial:
        • Ter trabalhado em projetos de e-commerce
        • Conhecimento / Noções de PHP                              
    """
)

print(json)

