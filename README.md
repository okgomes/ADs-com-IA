# ADs-com-IA
Este projeto utiliza o IBM Watson Natural Language Understanding (NLU) para analisar o histórico de navegação e compras de usuários, criando perfis detalhados que permitem a geração de recomendações de anúncios personalizados.


Funcionalidades Principais
Análise de texto avançada com IBM Watson NLU

Criação de perfis de usuário baseados em:

Interesses explícitos

Comportamento de navegação

Histórico de compras

Sistema de recomendação de anúncios personalizados

Geração de mensagens customizadas para cada usuário

Pré-requisitos
Python 3.8+

Conta no IBM Cloud com serviço Natural Language Understanding ativado

Chaves de API do Watson NLU

Instalação
Clone o repositório:

bash
git clone https://github.com/seu-usuario/personalized-recommendation-system.git
cd personalized-recommendation-system
Crie um ambiente virtual (recomendado):

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
Instale as dependências:

bash
pip install -r requirements.txt
Configuração
Renomeie o arquivo .env.example para .env

Insira suas credenciais do IBM Watson NLU:

IBM_API_KEY='sua_api_key_aqui'
IBM_SERVICE_URL='sua_url_de_serviço_aqui'
Prepare seu arquivo de dados de usuários seguindo o formato em users.json

Uso
Execute o sistema principal:

python
python main.py
Exemplo de Uso Programático
python
from user_analyzer import UserAnalyzer

# Inicializa o analisador
analyzer = UserAnalyzer('users.json')

# Obtém o perfil de um usuário
profile = analyzer.get_user_profile(1)

# Gera recomendações
ads = analyzer.generate_personalized_ad(1)

# Gera mensagem personalizada
message = analyzer.generate_personalized_message(1)
Estrutura do Projeto
.
├── README.md               # Documentação principal
├── main.py                 # Script principal de demonstração
├── user_analyzer.py        # Classe principal de análise
├── users.json              # Banco de dados de usuários exemplo
├── requirements.txt        # Dependências do projeto
├── .env.example            # Modelo de configuração
└── LICENSE                 # Licença do projeto
Banco de Dados de Usuários
O sistema espera um arquivo JSON no seguinte formato:

json
{
  "users": [
    {
      "id": 1,
      "name": "Nome do Usuário",
      "email": "email@exemplo.com",
      "interests": ["lista", "de", "interesses"],
      "browsing_history": [
        {
          "page_title": "Título da Página",
          "content": "Conteúdo textual para análise",
          "timestamp": "2023-01-01T00:00:00"
        }
      ],
      "purchase_history": [
        {
          "product": "Nome do Produto",
          "category": "categoria",
          "date": "2023-01-01"
        }
      ]
    }
  ]
}
Banco de Dados de Anúncios
Os anúncios são armazenados internamente na classe UserAnalyzer, organizados por categorias. Você pode modificar diretamente no código ou implementar um sistema de carregamento externo.

Contribuição
Faça um fork do projeto

Crie sua branch (git checkout -b feature/nova-feature)

Commit suas mudanças (git commit -am 'Adiciona nova feature')

Push para a branch (git push origin feature/nova-feature)

Abra um Pull Request

Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.

Recursos Adicionais
Documentação IBM Watson NLU

IBM Cloud

Python SDK for IBM Watson
