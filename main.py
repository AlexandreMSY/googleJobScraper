from jobdescriptionparser.jobdescriptionparser import JobDescriptionParser

parser = JobDescriptionParser("")
test = parser.parseJobDescription(
    """
        A área de “Desenvolvimento” é responsável pelo desenvolvimento de softwares de gestão incríveis.

        Seus principais objetivos são desenvolver soluções que geram resultado para nossos clientes, com velocidade, qualidade e facilidade de uso.

        Como Desenvolvedor Front-end você terá a responsabilidade de desenvolver soluções para aperfeiçoar a interface de nossos softwares e

        otimizar a experiência de uso nossos clientes utilizando Javascript, CSS, HTML e jQuery, e conseguirá enxergar os resultados do seu trabalho na prática.

        A faixa salarial inicial é de R$ 3.139,46 a R$ 5.523,17 conforme experiência anterior.

        O Desenvolvedor Java progride em um plano de carreira com níveis de Júnior, Pleno, Sênior e Master. A progressão na carreira depende da avaliação de desempenho trimestral e ao subir de nível, você ganha um aumento na remuneração fixa e assume cada vez mais desafios.

        Responsabilidades e atribuições

        Qual será seu papel na Nomus?

        Desenvolver interfaces de usuário atraentes e funcionais com foco na experiência do usuário.
        Colaborar com designers e desenvolvedores back-end para traduzir requisitos de negócios em soluções técnicas.
        Estar constantemente atento às novas tecnologias e tendências do mercado, propondo melhorias e atualizações para os projetos existentes.
        Participar ativamente do processo de planejamento e brainstorming para novos projetos, contribuindo com ideias e sugestões técnicas.
        Otimizar o desempenho das interfaces, garantindo tempos de carregamento rápidos e uma navegação fluida.


        Requisitos e qualificações

        Qual é o perfil desejado pela Nomus?

        Estamos buscando uma pessoa:

        Com graduação concluída em Sistemas de Informação, Ciência da Computação, Informática, Análise de Sistemas ou áreas afins.
        Que tenha disponibilidade para trabalhar 40 horas por semana com horário flexível.
        Com conhecimento em Javascript, CSS e HTML.
        Familiaridade com ferramentas de controle de versão.
        Com experiência profissional em desenvolvimento Front-end.
        Com iniciativa, vontade de aprender e comprometimento.
        Que tenha conhecimento de inglês no mínimo intermediário para leitura e escrita.
        Aceitamos candidatos de todo o Brasil. Candidatos com residência no Rio de Janeiro terão regime híbrido. Candidatos com residência fora do Rio de Janeiro terão regime de trabalho home-office de forma permanente.


        Informações adicionais

        E quais são as vantagens de fazer parte da equipe da Nomus?

        ⭐Seguro de vida em grupo.
        🍽️Cartão flexível Caju: você escolhe se vai usar em mercados ou restaurantes!
        👨‍⚕️Plano de saúde
        🦷Plano odontológico
        💻Auxílio home-office
        📚Auxílio educação
        💰Bônus semestral alinhado com a avaliação de desempenho e resultado da Nomus
        🎯Plano de carreira
        ⏰Horário flexível
        🏠Home-office
        💻Equipamentos fornecidos pela empresa
        💪🏻Gympass
        🎉Day off
        👶Licença maternidade e paternidade estendida 
        👨🏻‍💻Auxílio-coworking
        🎒Auxílio-creche para filhos
    """
)

print(test['skills']['hard'])
