import json
import os

def atualizar_vanguard():
    print("🚀 Vanguard System v4.1.2: Sincronização Cirúrgica...")
    
    try:
        # 1. Carrega os dados do JSON (Mesmo que esteja vazio, o script entende)
        with open('obras_config.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        info = dados.get('obra_info', {'titulo': 'Academia High Performance'})
        
        # 2. Prepara o novo bloco que será injetado no HTML
        novo_bloco = f"""<h4 style="text-align: center; color: #fff; font-family: 'Cinzel', serif;">{info['titulo']}</h4>
                <p style="text-align: center; color: #ccc; font-size: 0.9em; padding: 10px;">
                    Projeto finalizado com padrão de excelência Naldo Revestimentos. 
                    Assista ao resultado final desta execução de alto padrão.
                </p>
"""

        # 3. Lê o seu HTML atual
        with open('index.html', 'r', encoding='utf-8') as f:
            html_puro = f.read()

        # 4. AS TAGS DE CORTE (Onde o erro acontecia por estarem vazias)
        tag_inicio = ""
        tag_fim = ""

        # 5. A Lógica de Substituição Blindada
        if tag_inicio in html_puro and tag_fim in html_puro:
            parte_superior = html_puro.split(tag_inicio)[0]
            parte_inferior = html_puro.split(tag_fim)[-1]
            
            # Monta o site de volta com a nova informação no meio
            html_final = parte_superior + novo_bloco + parte_inferior
            
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(html_final)
            print("✨ SUCESSO: O site foi atualizado e o erro foi corrigido!")
        else:
            print("❌ ERRO: Não achei as tags no seu HTML. Verifique se você salvou o HTML que te mandei.")

    except Exception as e:
        print(f"❌ ERRO CRÍTICO NO MOTOR: {e}")

if __name__ == "__main__":
    atualizar_vanguard()