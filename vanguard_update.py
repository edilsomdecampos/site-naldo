import json
import re

def atualizar_vanguard():
    print("🚀 Vanguard System v2.0: Iniciando limpeza e atualização...")
    
    try:
        # 1. Carregar os dados da 'colinha' (JSON)
        with open('obras_config.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()

        # Pegamos os dados do Card 01
        info = dados['card_01']

        # 2. Criamos o bloco de código PERFEITO (sem sobras)
        novo_bloco_tecnico = f"""<div class="card-engenharia">
                <div class="video-box">
                    <video controls muted loop>
                        <source src="assets/video/{info['video']}" type="video/mp4">
                    </video>
                </div>
                <div class="info-box-tecnica">
                    <h4>Assentamento Técnico - Obra Recente</h4>
                    <ul class="lista-5-itens">
                        <li><strong>01. Revestimento:</strong> {info['piso']}</li>
                        <li><strong>02. Junta:</strong> {info['junta']}</li>
                        <li><strong>03. Argamassa:</strong> {info['argamassa']}</li>
                        <li><strong>04. Metragem:</strong> {info['metro']}</li>
                        <li><strong>05. Paginação:</strong> {info['pag']}</li>
                    </ul>
                </div>
            </div>"""

        # 3. A MÁGICA: O Python agora limpa TUDO entre as tags de feed e coloca o novo
        # Isso impede a duplicidade de uma vez por todas
        padrao = r'(<div class="container-feed-tecnico" id="feed-python">)(.*?)(</div>)'
        html_limpo = re.sub(padrao, rf'\1\n            {novo_bloco_tecnico}\n        \3', html, flags=re.DOTALL)

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html_limpo)
        
        print("✅ SUCESSO: Site limpo e atualizado. Sem duplicidade.")

    except Exception as e:
        print(f"❌ ERRO TÉCNICO: {e}")

if __name__ == "__main__":
    atualizar_vanguard()