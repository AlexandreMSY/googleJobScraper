from jobdescriptionparser.jobdescriptionparser import JobDescriptionParser
from user.userdetails import User
from user.degree import Degree
from datetime import date
from jobattributematcher.jobattributematcher import JobAttributeMatcher

parser = JobDescriptionParser("AIzaSyBznU6qeVaqrVTP08JbXqjXDQXr6qz4RjU")
test = parser.parseJobDescription(
    """
        Por que fazer parte do #PosiTime?

        Acreditamos que a tecnologia existe para impulsionar vidas, por isso, todos os dias construímos novas soluções que tornam a vida das pessoas melhor e mais inteligente! Ágeis, vibrantes, ousados, inovadores, diversos, conectados, dinâmicos, empreendedores e resilientes: mais que uma equipe, somos o #PosiTime.

        Se você se identifica com o nosso propósito, e procura um lugar para crescer e somar, te esperamos de braços abertos!

        Responsabilidades e atribuições

        Atender a fila de chamados da Segurança da Informação no Portal de Atendimento;

        Efetuar o controle das licenças dos softwares da companhia;

        Manutenção e concessão de acesso aos principais sistemas da companhia entre;

        Orientar e fornecer suporte quanto à utilização adequada de sistemas e condutas de Segurança da Informação;

        Manutenção da documentação de procedimentos e portal de segurança da informação;

        Atuar com a manutenção dos ativos da empresa.

        Requisitos e qualificações

        Cursando Análise de sistemas, Gestão de TI, CiberSegurança e áreas correlacionadas;

        Pacote Office Intermediário;

        Conhecimentos em manutenção de equipamentos e atendimento remoto, será considerado um diferencial;

        Disponibilidade para atuar em horário comercial de segunda à sexta-feira de forma presencial em SP.

        Há mais de três décadas quebramos barreiras, conquistamos o mercado e alcançamos lares de milhões de brasileiros. Fazem parte do nosso portfólio computadores, tablets, smartphones, celulares e dispositivos de telemedicina, além de equipamentos para escolas de mais de 40 países.

        O Propósito que nos move é TORNAR A VIDA DAS PESSOAS MELHOR E MAIS INTELIGENTE COM O USO DA TECNOLOGIA.

        Somos Great Place to Work (GPTW), certificação concedida a empresas reconhecidas internacionalmente como as melhores para se trabalhar, a partir de avaliações feitas pelos próprios colaboradores. Estamos há 3 anos consecutivos certificados pela GPTW.

        Conheça mais sobre nossa cultura. Siga a página da Positivo no Linkedin: www.linkedin.com/company/positivo-tecnologia

        Buscamos profissionais que se identificam com o nosso jeito de SER e FAZER

        VALORIZAMOS AS NOSSAS PESSOAS

        Queremos reter e atrair pessoas agentes de transformação;

        Vibramos com as conquistas, reagimos nas adversidades e valorizamos as atitudes;

        SOMOS INOVADORES E DINÂMICOS

        Acolhemos ideias e transformamos em marcas e produtos de qualidade, pensando na experiência de quem vai usá-los;

        Nenhum obstáculo é tão alto quanto a nossa rapidez e flexibilidade em superá-lo;

        Somos grandes. O dinamismo e a versatilidade não se perderam no crescimento;

        EVOLUÇÃO E DESAFIOS

        Surge uma oportunidade interessante e, se preciso for, nos reinventamos para conquistá-la;

        Gostamos de desafios e conduzimos vários ao mesmo tempo;

        Temos raízes fortes. Nossa história e ética sustentam nossa constante evolução;

        CLIENTE NO CENTRO DE TUDO

        Buscamos sempre entregar além do esperado. Capricho para nós não é mero detalhe.

        Nascemos no Brasil, ousamos criar e desenvolver uma marca verde-amarela em tecnologia, e provamos que somos capazes de liderar, inovar e povoar os lares brasileiros;

        Nos orgulhamos de ter facilitado a inclusão digital e melhorado a vida de muitos brasileiros, e ainda queremos mais;

        Tecnologia é um caminho para melhorar a vida das pessoas, mas não o destino
    """
)

user = User(None, ["HTML", "CSS", "JavaScript", "mysql"], [Degree("Análise de sistemas", "test", date(1999,8,2))], None, ["inglês"])
attributeMatcher = JobAttributeMatcher(user= user, jobAttributes=test)

#print(test)
print(attributeMatcher.attributesMatched())
