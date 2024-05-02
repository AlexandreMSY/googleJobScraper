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
        Área e especialização profissional: Informática, TI, Telecomunicações - Programador / Desenvolvedor
        Nível hierárquico: Estagiário
        Lugar de trabalho: São Paulo, SP
        Regime de contratação de tipo Estágio
        Jornada Parcial manhãs
J       á pensou em estagiar área de TI de uma empresa que é referência em soluções de tecnologia para o mundo corporativo na América Latina? Estamos em busca de um estagiário (a) com perfil para fazer parte do nosso time. Se você possui um perfil dinâmico e flexível, tem vontade de aprender, facilidade para trabalhar em grupo, conhecimento básico em linguagem de programação e inglês avançado. Esta é a oportunidade perfeita para você desenvolver suas habilidades e colaborar com uma empresa sólida e em crescimento acelerado. Suas principais responsabilidades: • Auxiliar na manutenção e desenvolvimento de sistemas (interno ou projetos externos) • Colaborar com a equipe de desenvolvimento para criar e implementar novas funcionalidades. • Participar na resolução de problemas técnicos • Suporte técnico O que você precisa ter tecnicamente: • Graduação em andamento em cursos de: Ciência da Computação, Engenharia da Computação, Análise de Sistemas ou áreas correlatas direcionadas para área de TI. • Conhecimento básico em pelo menos uma das principais linguagens de programação (JS, Java, .Net , Python, Pascal, C++) • Conhecimento em Banco de Dados Relacionais • Inglês avançado ou técnico Nós buscamos estagiários que tenham: • Flexibilidade • Vontade em aprender • Facilidade em trabalhar em grupo • Relacionamento interpessoal Nossos benefícios: - Bolsa-auxílio de R$1.400,00 - Vale-transporte de quantas conduções você precisar sem desconto nenhum; - Vale-refeição flexível (CAJU) de R$35,00/dia para você usar em mercados ou restaurantes - GYMPASS para cuidar do corpo e da mente - Assistência médica Bradesco com 50% de desconto na mensalidade - Assistência Odontológica Sulamérica - DayOff no do seu aniversário Informações adicionais: Horário: 09:00 às 16:00hrs, com 1h de almoço. Localização: Av. Paulista                  
    """
)

print(json)

