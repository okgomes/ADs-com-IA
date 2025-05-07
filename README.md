# ADs-com-IA
Este projeto utiliza o IBM Watson Natural Language Understanding (NLU) para analisar o histórico de navegação e compras de usuários, criando perfis detalhados que permitem a geração de recomendações de anúncios personalizados.

O que faz?
Analisa o histórico de usuários (navegação, compras e interesses) com IBM Watson NLU e recomenda anúncios personalizados.

⚙️ Como rodar?
Instale as dependências:

bash
pip install ibm-watson python-dotenv
Configure suas chaves (no arquivo .env):

env
IBM_API_KEY='sua_chave_aqui'
IBM_SERVICE_URL='sua_url_do_watson'
Execute:

bash
python main.py
📂 Estrutura
.
├── main.py              # Código principal
├── users.json           # Dados dos usuários (exemplo)
├── .env                 # Configurações (não versionado)

💡 Como usar?
python
from user_analyzer import UserAnalyzer

analyzer = UserAnalyzer('users.json')

# Pega o perfil do usuário ID 1
profile = analyzer.get_user_profile(1)  

# Recomenda anúncios
ads = analyzer.generate_personalized_ad(1)  

# Mensagem personalizada
message = analyzer.generate_personalized_message(1)  

🔗 Links Úteis
IBM Watson NLU
Python SDK

