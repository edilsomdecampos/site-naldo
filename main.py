import instaloader
import os

# =========================================================
# CONFIGURAÇÕES DE DIRETOR - AGÊNCIA DE DESIGN COM IA
# =========================================================
# Recomendo usar uma conta secundária para evitar bloqueios no seu perfil pessoal
USER_INSTA = "SEU_USUARIO" 
PASS_INSTA = "SUA_SENHA" 
PERFIL_ALVO = "perfqtpisos"

ARQUIVO_HTML = "index.html"
PASTA_DESTINO = "assets/video"

def agente_ia_puxar_instagram():
    """
    Agente autônomo para captura de vídeos e atualização 
    automática do memorial técnico.
    """
    L = instaloader.Instaloader(
        download_videos=True, 
        download_video_thumbnails=False,
        save_metadata=False,
        post_metadata_txt_pattern=""
    )

    try:
        # AUTENTICAÇÃO: Vital para evitar Erro 401 Unauthorized
        print(f"🔐 [IA] Autenticando Agente no Instagram...")
        L.login(USER_INSTA, PASS_INSTA) 
        
        print(f"📡 [IA] Conectando ao perfil @{PERFIL_ALVO}...")
        profile = instaloader.Profile.from_username(L.context, PERFIL_ALVO)
        
        # Pega o vídeo mais recente do feed
        for post in profile.get_posts():
            if post.is_video:
                if not os.path.exists(PASTA_DESTINO):
                    os.makedirs(PASTA_DESTINO)
                
                print(f"✅ [IA] Vídeo de obra detectado: {post.date_local}")
                L.download_post(post, target=PASTA_DESTINO)
                
                # Identifica o arquivo .mp4 baixado
                arquivos = [f for f in os.listdir(PASTA_DESTINO) if f.endswith('.mp4')]
                if arquivos:
                    # Ordena por data de modificação para pegar o mais recente
                    arquivos.sort(key=lambda x: os.path.getmtime(os.path.join(PASTA_DESTINO, x)), reverse=True)
                    video_nome = arquivos[0]
                    
                    # DISPARA A INJEÇÃO NO HTML
                    injetar_no_site(video_nome)
                break # Processa apenas o vídeo mais recente para manter a agilidade

    except Exception as e:
        print(f"❌ Erro Crítico na Automação: {e}")

def injetar_no_site(video_nome):
    """
    Lógica de escrita autônoma no HTML para Memorial Técnico.
    """
    caminho_video = f"{PASTA_DESTINO}/{video_nome}"
    
    # O bloco técnico com os 5 itens exigidos pelo Diretor
    novo_card = f"""
            <div class="card-engenharia">
                <div class="video-box">
                    <video controls muted loop>
                        <source src="{caminho_video}" type="video/mp4">
                    </video>
                </div>
                <div class="info-box-tecnica">
                    <h4>Assentamento Técnico - @{PERFIL_ALVO}</h4>
                    <ul class="lista-5-itens">
                        <li><strong>01. Revestimento:</strong> Porcelanato Técnico (Alta Performance)</li>
                        <li><strong>02. Junta:</strong> 1mm (Niveladores de Precisão)</li>
                        <li><strong>03. Argamassa:</strong> AC3 Branca (Uso Profissional)</li>
                        <li><strong>04. Metragem:</strong> Verificada em Projeto de Campo</li>
                        <li><strong>05. Paginação:</strong> Alinhamento Técnico de Elite</li>
                    </ul>
                </div>
            </div>
            """

    if os.path.exists(ARQUIVO_HTML):
        with open(ARQUIVO_HTML, "r", encoding="utf-8") as f:
            conteudo = f.read()

        if "" in conteudo:
            # Insere o novo card antes do marcador (mantendo o marcador para o próximo vídeo)
            conteudo_atualizado = conteudo.replace("", novo_card)
            
            with open(ARQUIVO_HTML, "w", encoding="utf-8") as f:
                f.write(conteudo_atualizado)
            print("✨ [IA] MEMORIAL TÉCNICO ATUALIZADO NO NAVEGADOR!")
        else:
            print("⚠️ Erro: Marcador não encontrado no HTML.")
    else:
        print("❌ Erro: Arquivo index.html não localizado na raiz.")

if __name__ == "__main__":
    agente_ia_puxar_instagram()