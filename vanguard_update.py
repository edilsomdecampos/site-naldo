import json

def atualizar_vanguard():
    print("🚀 Vanguard System v3.0: Sincronização Blindada...")
    
    try:
        with open('obras_config.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()

        info = dados['card_01']
        
        # Criamos o conteúdo técnico puro
        novo_conteudo = f"""
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

        # Lógica de substituição por "âncoras" fixas
        start_tag = '<div class="container-feed-tecnico" id="feed-python">'
        end_tag = '</div>\n    </section>' # Esta âncora garante que ele não saia da seção
        
        parte_inicial = html.split(start_tag)[0]
        parte_final = html.split(end_tag)[-1]
        
        # Remontagem perfeita do arquivo
        html_final = f"{parte_inicial}{start_tag}{novo_conteudo}\n        </div>\n    </section>{parte_final}"

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html_final)
        
        print("✅ Sucesso: O site foi higienizado e atualizado.")

    except Exception as e:
        print(f"❌ Erro no Script: {e}")

if __name__ == "__main__":
    atualizar_vanguard()