import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions, KeywordsOptions, CategoriesOptions

# Configuração do Watson NLU
authenticator = IAMAuthenticator('API_KEY')
nlu = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)
nlu.set_service_url('SERVICE_URL')

class UserAnalyzer:
    def __init__(self, users_file='users.json'):
        self.users = self.load_users(users_file)
        self.ads_database = {
            'tecnologia': [
                {"id": 1, "title": "Novo Smartphone com IA", "content": "Experimente o poder da inteligência artificial no seu bolso!"},
                {"id": 2, "title": "Notebook Ultrafino", "content": "Trabalhe e jogue com alta performance"}
            ],
            'esportes': [
                {"id": 3, "title": "Tênis Esportivo", "content": "Conforto e desempenho para seus treinos"},
                {"id": 4, "title": "Assinatura Esportiva", "content": "Acesso a todos os jogos ao vivo"}
            ],
            'moda': [
                {"id": 5, "title": "Coleção Outono/Inverno", "content": "As peças mais desejadas da estação"},
                {"id": 6, "title": "Desconto em Acessórios", "content": "Até 40% off em bolsas e sapatos"}
            ],
            'culinária': [
                {"id": 7, "title": "Kit de Panelas Premium", "content": "Cozinhe como um chef profissional"},
                {"id": 8, "title": "Curso de Culinária Online", "content": "Aprenda 50 receitas exclusivas"}
            ]
        }
    
    def load_users(self, filename):
        """Carrega a base de usuários do arquivo JSON"""
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)['users']
    
    def analyze_user_texts(self, user_id):
        """Analisa os textos do histórico do usuário com Watson NLU"""
        user = next((u for u in self.users if u['id'] == user_id), None)
        if not user:
            return None
        
        combined_text = " ".join([item['content'] for item in user['browsing_history']])
        
        try:
            response = nlu.analyze(
                text=combined_text,
                features=Features(
                    keywords=KeywordsOptions(limit=10),
                    categories=CategoriesOptions(limit=5)
                )
            ).get_result()
            return response
        except Exception as e:
            print("Erro na análise:", str(e))
            return None
    
    def get_user_profile(self, user_id):
        """Cria um perfil detalhado do usuário com base nas análises"""
        analysis = self.analyze_user_texts(user_id)
        user = next((u for u in self.users if u['id'] == user_id), None)
        
        if not user or not analysis:
            return None
        
        keywords = [kw['text'] for kw in analysis.get('keywords', [])]
        categories = [cat['label'].split('/')[-1] for cat in analysis.get('categories', [])]
        
        profile = {
            "user_id": user_id,
            "name": user['name'],
            "detected_interests": list(set(keywords + categories)),
            "explicit_interests": user['interests'],
            "combined_interests": list(set(user['interests'] + keywords + categories)),
            "purchase_history": user['purchase_history']
        }
        
        return profile
    
    def generate_personalized_ad(self, user_id):
        """Gera anúncios personalizados baseados no perfil do usuário"""
        profile = self.get_user_profile(user_id)
        if not profile:
            return None
        
        matched_ads = []
        for interest in profile['combined_interests']:
            if interest in self.ads_database:
                matched_ads.extend(self.ads_database[interest])
        
        unique_ads = []
        seen_ids = set()
        for ad in matched_ads:
            if ad['id'] not in seen_ids:
                seen_ids.add(ad['id'])
                unique_ads.append(ad)
        
        return unique_ads[:3]
    
    def generate_personalized_message(self, user_id):
        """Cria mensagem personalizada para o usuário"""
        profile = self.get_user_profile(user_id)
        if not profile:
            return "Ola! Temos novidades para voce!"
        
        main_interests = profile['combined_interests'][:2]
        last_purchase = profile['purchase_history'][-1]['category'] if profile['purchase_history'] else None
        
        if last_purchase:
            message = f"Ola {profile['name']}! Baseado no seu interesse em {', '.join(main_interests)} "
            message += f"e sua ultima compra de {last_purchase}, temos estas recomendacoes especiais:"
        else:
            message = f"Ola {profile['name']}! Vimos que voce se interessa por {', '.join(main_interests)}. "
            message += "Temos estas ofertas especiais para voce:"
        
        return message

# Exemplo de uso
if __name__ == "__main__":
    analyzer = UserAnalyzer()
    
    # Análise para o usuário João (ID 1)
    user_id = 1
    print("\n" + "="*50)
    print(f"ANALISE PARA O USUARIO {user_id}".center(50))
    print("="*50)
    
    profile = analyzer.get_user_profile(user_id)
    print("\nPerfil detectado:")
    print(json.dumps(profile, indent=2, ensure_ascii=False))
    
    print("\nMensagem personalizada:")
    print(analyzer.generate_personalized_message(user_id))
    
    print("\nAnuncios recomendados:")
    for ad in analyzer.generate_personalized_ad(user_id):
        print(f"\n- {ad['title']}: {ad['content']}")
    
    # Análise para o usuário Maria (ID 2)
    user_id = 2
    print("\n" + "="*50)
    print(f"ANALISE PARA O USUARIO {user_id}".center(50))
    print("="*50)
    
    profile = analyzer.get_user_profile(user_id)
    print("\nPerfil detectado:")
    print(json.dumps(profile, indent=2, ensure_ascii=False))
    
    print("\nMensagem personalizada:")
    print(analyzer.generate_personalized_message(user_id))
    
    print("\nAnuncios recomendados:")
    for ad in analyzer.generate_personalized_ad(user_id):
        print(f"\n- {ad['title']}: {ad['content']}")
