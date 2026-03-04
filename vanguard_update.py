import json
import re

def atualizar_vanguard():
    print("🚀 Vanguard System: Iniciando atualização técnica...")
    
    try:
        # 1. Carregar Dados
        with open('obras_config.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()

        # 2. Preparar o Novo Card (Baseado no seu HTML original)
        info = dados['card_01']
        novo_card = f"""
            <div class="card-engenharia">
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

        # 3. Injeção Cirúrgica (Protegendo a Galeria Estática)
        padrao = r'(<div class="container-feed-tecnico" id="feed-python">)(.*?)(</div>)'
        html_atualizado = re.sub(padrao, rf'\1{novo_card}\n        \3', html, flags=re.DOTALL)

        # 4. Salvar
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html_atualizado)
        
        print("✅ Sucesso: Memorial Técnico atualizado sem alterar a Galeria de Fotos.")

    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    atualizar_vanguard()