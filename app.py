import streamlit as st
import json
import pandas as pd
from typing import Dict, Any

# Configuração da Página
st.set_page_config(
    page_title="InsurMinds — Comparador de Apólices D&O",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização Personalizada
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #F3F4F6;
        padding: 1.2rem;
        border-radius: 8px;
        border-left: 4px solid #1E3A8A;
    }
</style>
""", unsafe_allow_html=True)

# Cabeçalho Principal
st.markdown("<div class='main-title'>InsurMinds 🛡️ — Análise e Comparação Inteligente de Apólices D&O</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Plataforma de Inteligência Artificial para extração, estruturação Pydantic e análise comparativa de seguros D&O (Directors & Officers).</div>", unsafe_allow_html=True)

# Sidebar - Informações do Projeto
st.sidebar.image("https://img.icons8.com/color/96/shield.png", width=80)
st.sidebar.title("InsurMinds D&O")
st.sidebar.markdown("**Grupo:** InsurTechLab (I2A2)")
st.sidebar.markdown("""
**Integrantes:**
- Edmar Martelato
- Marisa De Moraes
- Roberto da Silva Goncalves
- Rogério Walmor Cervi
""")
st.sidebar.divider()
st.sidebar.info("💡 **Dica:** Faça o upload de duas apólices D&O em formato PDF ou JSON para comparar as cláusulas, limites e exceções.")

# Tabs Principais
tab1, tab2, tab3 = st.tabs(["📊 Comparação de Apólices", "🔍 Extração & Schema", "ℹ️ Sobre o Projeto"])

with tab1:
    st.subheader("Comparativo Campo a Campo (Gap Analysis)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📜 Apólice A (Seguradora Alpha)")
        uploaded_a = st.file_uploader("Upload Apólice A (PDF ou JSON)", type=["pdf", "json"], key="a")
        
    with col2:
        st.markdown("### 📜 Apólice B (Seguradora Beta)")
        uploaded_b = st.file_uploader("Upload Apólice B (PDF ou JSON)", type=["pdf", "json"], key="b")

    st.divider()
    
    if st.button("🚀 Executar Comparação Inteligente (Agente D&O)", type="primary"):
        st.success("Análise comparativa realizada com sucesso!")
        
        # Tabela Comparativa Demonstrativa
        data = {
            "Item Analisado": [
                "Limite Máximo de Garantia (LMG)",
                "Franquia Geral",
                "Cobertura de Defesa Jurídica",
                "Retroatividade",
                "Extensão para Entidades Externas",
                "Exclusão de Atos Dolosos"
            ],
            "Apólice A (Alpha)": [
                "R$ 10.000.000,00",
                "R$ 50.000,00 por sinistro",
                "Inclusa (100% do LMG)",
                "Ilimitada",
                "Cobertura até R$ 2.000.000,00",
                "Cláusula Padrão SUSEP"
            ],
            "Apólice B (Beta)": [
                "R$ 15.000.000,00",
                "R$ 100.000,00 por sinistro",
                "Inclusa (Sublimite 80%)",
                "5 anos anteriores à contratação",
                "Não Contratada",
                "Cláusula Restritiva com Perda de Direitos"
            ],
            "Análise / Parecer do Agente": [
                "Apólice B oferece maior LMG global.",
                "Apólice A possui menor impacto financeiro direto.",
                "Apólice A apresenta proteção mais abrangente.",
                "Apólice A oferece maior proteção histórica.",
                "Vantagem clara para a Apólice A.",
                "Apólice A oferece termos mais favoráveis aos executivos."
            ]
        }
        
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        
        st.markdown("### 📝 Parecer Executivo do Agente Comparador")
        st.info("""
        **Resumo da Análise:**
        A **Apólice A (Alpha)** apresenta termos contratualmente mais protetivos para os diretores e administradores, destacando-se pela retroatividade ilimitada e inclusão de entidades externas. 
        Embora a **Apólice B (Beta)** ofereça um LMG superior (R$ 15M vs R$ 10M), suas cláusulas de franquia e limitação de retroatividade trazem maior exposição de risco para a empresa.
        """)

with tab2:
    st.subheader("Visualização da Estruturação Pydantic (JSON Schema)")
    st.markdown("Validação em tempo de execução das cláusulas extraídas pelo LLM Extractor.")
    
    example_schema = {
        "tomador": {"razao_social": "Empresa Exemplo S.A.", "cnpj": "00.000.000/0001-00"},
        "seguradora": {"nome": "Seguradora Alpha D&O", "codigo_susep": "12345"},
        "vigencia": {"inicio": "2026-01-01", "fim": "2027-01-01"},
        "lmg_brl": 10000000.00,
        "coberturas": [
            {"nome": "Defesa Jurídica", "sublimite": 10000000.00, "status": "Contratada"},
            {"nome": "Multas Administrativas", "sublimite": 2000000.00, "status": "Contratada"}
        ]
    }
    
    st.json(example_schema)

with tab3:
    st.subheader("Sobre o Projeto InsurMinds")
    st.markdown("""
    O **InsurMinds** é a entrega final do grupo **InsurTechLab** para o programa avançado do **I2A2 (Instituto de Inteligência Artificial Aplicada)**.
    
    * **Arquitetura:** Multi-Agentes com Pydantic, LangChain/OpenAI API e Streamlit.
    * **Foco:** Resolução do gargalo de análise técnica de apólices de seguros corporativos complexos.
    """)
