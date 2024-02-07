import streamlit as st

def main():
    st.title("Criação de Sociedade: Workflow Interativo")

    st.sidebar.title("Navegação")
    opcao = st.sidebar.radio("Escolha uma etapa:", ["Introdução", "Passo a Passo", "Cuidados", "Profissionais a Consultar", "Regime de Cotas e Lucros", "Estrutura de Controle", "Regime Sucessório"])

    if opcao == "Introdução":
        st.header("Introdução")
        st.write("Este guia interativo oferece um panorama sobre a criação de uma sociedade, destacando os principais passos, cuidados e estratégias para garantir uma fundação sólida para o seu negócio.")

    elif opcao == "Passo a Passo":
        st.header("Passo a Passo para a Criação de uma Sociedade")
        
        # Adicionando um botão para a Definição do Tipo de Sociedade
        if st.button("Definição do tipo de sociedade"):
            show_tipo_sociedade()

        # Botão para Elaboração do Contrato Social
        if st.button("Elaboração do Contrato Social"):
            show_contrato_social()
        
        st.write("3. Registro da empresa nos órgãos competentes.")
        st.write("4. Obtenção do CNPJ e inscrições municipais/estaduais.")
        st.write("5. Licenças e alvarás necessários para a atividade.")
        st.write("3. Registro da empresa nos órgãos competentes.")
        st.write("4. Obtenção do CNPJ e inscrições municipais/estaduais.")
        st.write("5. Licenças e alvarás necessários para a atividade.")

    elif opcao == "Cuidados":
        st.header("Principais Cuidados")
        st.write("- Escolha cuidadosa dos sócios.")
        # Botão para Definição clara das contribuições de cada sócio
        if st.button("Definição clara das contribuições de cada sócio"):
            show_contribuicoes_socios()
        # Botão para Acordo sobre a distribuição de lucros e prejuízos
        if st.button("Acordo sobre a distribuição de lucros e prejuízos"):
            show_acordo_lucros_prejuizos()

    elif opcao == "Profissionais a Consultar":
        st.header("Profissionais a Consultar")
        st.write("- Advogado especializado em direito empresarial.")
        st.write("- Contador para orientações fiscais e contábeis.")
        st.write("- Consultor financeiro para planejamento financeiro.")

    elif opcao == "Regime de Cotas e Lucros":
        st.header("Regime de Cotas e Lucros")
        st.write("Como a divisão de cotas influencia a distribuição de lucros e a tomada de decisões na empresa.")

        # Botão para Divisão de Lucros
        if st.button("Divisão de Lucros"):
            show_divisao_lucros()
        
        # Botão para Controle e Tomada de Decisões
        if st.button("Controle e Tomada de Decisões"):
            show_controle_decisoes()

    elif opcao == "Estrutura de Controle":
        st.header("Estrutura de Controle da Empresa")
        st.write("A importância do contrato social e do acordo de acionistas para estabelecer regras claras de governança na empresa.")

        # Botão para Contrato Social
        if st.button("Contrato Social"):
            show_contrato_social()
        
        # Botão para Acordo de Acionistas
        if st.button("Acordo de Acionistas"):
            show_acordo_acionistas()

    elif opcao == "Regime Sucessório":
        st.header("Regime Sucessório")
        st.write("Orientações sobre como preparar a empresa para a sucessão, protegendo o negócio e os interesses dos herdeiros.")

        # Botão para Orientações de Sucessão
        if st.button("Orientações de Sucessão"):
            show_orientacoes_sucessao()

def show_tipo_sociedade():
    st.write("A escolha do tipo de sociedade é um dos primeiros e mais importantes passos na criação de uma empresa. Cada tipo tem suas próprias características, vantagens e desvantagens.")
    
    with st.expander("Sociedade Limitada (Ltda.)"):
        st.write("""
                 - **Características**: Limita a responsabilidade dos sócios ao valor de suas cotas, mas todos respondem solidariamente pela integralização do capital social.
                 - **Vantagens**: Proteção patrimonial dos sócios; estrutura administrativa flexível.
                 - **Desvantagens**: Necessidade de capital social mínimo não é exigida pela legislação brasileira atual.
                 - **Ideal para**: Empreendedores que buscam proteção patrimonial sem abrir mão da flexibilidade na gestão.
                 """)

    with st.expander("Sociedade Anônima (S.A.)"):
        st.write("""
                 - **Características**: Capital social dividido em ações, podendo negociá-las no mercado aberto se for de capital aberto.
                 - **Vantagens**: Captação de recursos via mercado de ações; limitação da responsabilidade dos acionistas ao preço de emissão das ações.
                 - **Desvantagens**: Estrutura administrativa e regulatória complexa.
                 - **Ideal para**: Empresas de grande porte ou que pretendem captar recursos via mercado de capitais.
                 """)

    with st.expander("Sociedade Simples"):
        st.write("""
                 - **Características**: Voltada para a prestação de serviços profissionais especializados.
                 - **Vantagens**: Simplicidade na constituição e operação.
                 - **Desvantagens**: Sócios respondem ilimitadamente pelas dívidas da sociedade.
                 - **Ideal para**: Profissionais liberais que desejam formalizar uma parceria para prestação de serviços.
                 """)

def show_contrato_social():
    st.header("Elaboração do Contrato Social")
    st.write("""
             A elaboração do contrato social é um passo fundamental na criação de uma sociedade, pois ele define as regras de funcionamento, direitos e obrigações dos sócios. Aqui estão os elementos principais que devem ser considerados:
             """)
    
    with st.expander("Informações Básicas"):
        st.write("""
                 - **Nomes completos e dados dos sócios:** CPF, RG, endereço residencial, estado civil e profissão.
                 - **Nome empresarial:** Denominação da empresa.
                 - **Objeto social:** Atividades que serão desenvolvidas pela empresa.
                 - **Endereço da sede:** Local onde a empresa será registrada.
                 """)
    
    with st.expander("Capital Social"):
        st.write("""
                 - **Valor do capital social:** Montante inicial investido na empresa.
                 - **Divisão das cotas:** Proporção do capital social que cada sócio detém.
                 """)
    
    with st.expander("Administração da Empresa"):
        st.write("""
                 - **Gestores da sociedade:** Quem será responsável pela administração da empresa.
                 - **Poderes e deveres:** Definições de responsabilidades dos administradores.
                 """)
    
    with st.expander("Regime de Lucros e Perdas"):
        st.write("""
                 - **Distribuição de lucros e prejuízos:** Como os lucros e prejuízos serão divididos entre os sócios.
                 - **Frequência de distribuição:** Periodicidade da distribuição dos lucros.
                 """)
    
    st.write("É altamente recomendável que a elaboração do contrato social seja acompanhada por um advogado especializado em direito empresarial para garantir que todos os aspectos legais sejam adequadamente abordados.")

def show_contribuicoes_socios():
    st.header("Definição clara das contribuições de cada sócio")
    st.write("""
             É crucial definir claramente as contribuições de cada sócio para a empresa. Isso não inclui apenas o capital financeiro, mas também contribuições não monetárias como conhecimento, habilidades e tempo.
             """)
    
    with st.expander("Tipos Comuns de Contribuições"):
        st.write("""
                 - **Financeira:** Dinheiro ou bens avaliáveis em dinheiro investidos na empresa.
                 - **Intelectual:** Conhecimentos específicos, habilidades ou patentes.
                 - **Física:** Bens móveis ou imóveis disponibilizados para uso da empresa.
                 - **Trabalho:** Esforço pessoal dedicado à gestão e operação da empresa.
                 """)
    
    with st.expander("Divisão de Funções"):
        st.write("""
                 - **Gestor Administrativo:** Responsável pela administração do dia a dia da empresa.
                 - **Diretor Financeiro:** Cuida das finanças, orçamentos e investimentos.
                 - **Chefe de Operações:** Supervisiona as operações diárias e a produção.
                 - **Diretor de Marketing e Vendas:** Foca no desenvolvimento de estratégias de mercado e vendas.
                 - **Especialista em Produto/Indústria:** Responsável pelo desenvolvimento de produtos e inovação.
                 """)
    
    st.write("A clareza na definição dessas contribuições e funções é essencial para a harmonia entre os sócios e o sucesso da empresa. Um acordo de sócios detalhado pode ser útil para documentar estas definições.")

def show_acordo_lucros_prejuizos():
    st.header("Acordo sobre a Distribuição de Lucros e Prejuízos")
    st.write("""
             Estabelecer um acordo claro sobre a distribuição de lucros e prejuízos é fundamental para evitar desentendimentos entre os sócios. Este acordo deve ser detalhado no contrato social ou em um documento separado.
             """)
    
    with st.expander("Exemplo de Divisão de Lucros 70/30"):
        st.write("""
                 - **Modelo de divisão:** Neste cenário, 70% dos lucros são destinados ao sócio A e 30% ao sócio B.
                 - **Base para divisão:** A divisão é baseada no acordo prévio entre os sócios, refletindo, por exemplo, diferenças em contribuições iniciais, responsabilidades na operação da empresa ou investimentos em recursos.
                 - **Considerações sobre prejuízos:** Da mesma forma, os prejuízos devem ser compartilhados nesta proporção, a menos que acordado de outra forma.
                 - **Flexibilidade:** O acordo deve permitir revisões futuras, conforme a evolução da empresa e das contribuições dos sócios.
                 - **Documentação:** É crucial documentar esse acordo de forma clara e legalmente válida.
                 """)
    
    st.write("Uma consultoria jurídica é recomendada para garantir que o acordo sobre a distribuição de lucros e prejuízos esteja em conformidade com a legislação vigente e proteja os interesses de todos os sócios.")

def show_divisao_lucros():
    st.header("Divisão de Lucros")
    st.write("""
             A divisão de cotas determina a proporção dos lucros distribuídos aos sócios. Uma divisão de cotas 70/30 implica que o sócio A recebe 70% dos lucros, enquanto o sócio B recebe 30%.
             """)
    
    with st.expander("Implicações da Divisão de Lucros 70/30"):
        st.write("""
                 - **Equidade vs. Igualdade:** Esta divisão reflete um acordo sobre o valor relativo das contribuições de cada sócio.
                 - **Incentivos:** Pode incentivar o sócio com maior participação a investir mais no sucesso da empresa.
                 - **Possíveis Desafios:** É importante que ambos os sócios estejam satisfeitos com essa divisão para evitar conflitos futuros.
                 """)
    
def show_controle_decisoes():
    st.header("Controle e Tomada de Decisões")
    st.write("""
             A divisão de cotas também afeta o controle e a tomada de decisões na empresa. Uma divisão de cotas 70/30 geralmente concede ao sócio A uma maior influência nas decisões.
             """)
    
    with st.expander("Controle Criativo e Tomada de Decisões com Cotas 70/30"):
        st.write("""
                 - **Maior Controle:** O sócio A, com 70% das cotas, tem o controle decisório, podendo influenciar fortemente a direção criativa e estratégica da empresa.
                 - **Voto de Minerva:** Em decisões importantes, o voto do sócio A pode ser decisivo.
                 - **Responsabilidade:** Com maior poder, vem também maior responsabilidade pelo sucesso ou fracasso da empresa.
                 - **Proteção ao Sócio Minoritário:** É essencial estabelecer mecanismos de proteção para o sócio B, garantindo voz nas decisões críticas.
                 """)

def show_acordo_acionistas():
    st.header("Acordo de Acionistas")
    st.write("""
             O acordo de acionistas é um complemento importante ao contrato social, especialmente em empresas com múltiplos sócios. Ele pode abordar questões específicas relacionadas ao controle e governança da empresa.
             """)

    with st.expander("Exemplo de Acordo de Acionistas - Sono Minas"):
        st.write("""
                 - **Divisão de Cotas e Controle:** O acordo de acionistas detalha a divisão de cotas e o controle da empresa, especificando os direitos e responsabilidades de cada família.
                 - **Voto de Minerva:** Pode incluir cláusulas sobre o voto de minerva para decisões críticas, equilibrando o poder entre as famílias.
                 - **Saída de Sócios:** Regula o processo de saída de sócios, incluindo a compra/venda de cotas.
                 - **Resolução de Conflitos:** Define como os conflitos serão resolvidos para evitar litígios.
                 """)

def show_orientacoes_sucessao():
    st.header("Orientações de Sucessão na Empresa Sono Minas (70/30)")

    st.write("""
             Preparar a empresa para a sucessão é crucial para garantir a continuidade dos negócios e proteger os interesses dos herdeiros, especialmente em uma empresa com divisão 70/30 entre as famílias A e B. Abaixo estão algumas orientações importantes:
             """)

    with st.expander("Passagem de Cotas para os Filhos"):
        st.write("""
                 - **Acordo Prévio:** É recomendável que os sócios estabeleçam um acordo prévio sobre a possibilidade de passagem de cotas para os filhos.
                 - **Documentação Legal:** A passagem de cotas deve ser devidamente documentada e cumprir as leis de governança da empresa.
                 - **Avaliação de Impacto:** Considere o impacto na divisão de cotas e no controle da empresa ao passar cotas para os filhos.
                 - **Educação e Preparação:** Os filhos herdeiros devem ser educados e preparados para assumir responsabilidades na empresa.
                 """)

    with st.expander("Considerações em Caso de Falecimento"):
        st.write("""
                 - **Testamento e Sucessão:** Ter um testamento que especifique a distribuição das cotas em caso de falecimento é fundamental.
                 - **Proteção dos Interesses dos Herdeiros:** Garanta que os interesses dos herdeiros sejam protegidos e que eles possam herdar as cotas de forma justa.
                 - **Seguro de Vida:** Considere a contratação de seguros de vida que possam beneficiar os herdeiros financeiramente.
                 - **Plano de Continuidade:** Elabore um plano de continuidade de negócios para lidar com a ausência de um dos sócios.
                 """)

    st.write("""
             É altamente recomendável consultar um advogado especializado em direito empresarial e sucessório para garantir que todas as questões legais e financeiras relacionadas à sucessão estejam devidamente tratadas e em conformidade com a legislação.
             """)

if __name__ == "__main__":
    main()