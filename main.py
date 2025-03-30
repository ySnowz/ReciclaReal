# 1. Streamlit DEVE ser o primeiro import (não pode ter nada antes)
import streamlit as st

# 2. set_page_config() DEVE ser o primeiro comando Streamlit (nada antes, nem comentários)
st.set_page_config(
    page_title="ReciclaReal",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="auto"  # Correção ortográfica importante aqui
)

# 3. Agora outros imports (depois do page_config)
import pandas as pd
import os
from datetime import datetime, timedelta

# Configurações
ARQUIVO_PRINCIPAL = "registros_reciclagem.csv"
PASTA_RELATORIOS = "relatorios"
os.makedirs(PASTA_RELATORIOS, exist_ok=True)

# Lista de Materiais
MATERIAIS = [
    "Papelao", 
    "Papel branco", 
    "Plastico", 
    "Sucata", 
    "Aluminio mole", 
    "Aluminio duro", 
    "Aco", 
    "Cobre misto", 
    "Cobre Mel", 
    "Metal", 
    "Para-choque", 
    "PUC", 
    "Fio", 
    "Placa", 
    "Bateria", 
    "Chumbo"
]

# CSS Customizado para Mobile
st.markdown("""
    <style>
        /* Ajustes gerais para mobile */
        @media (max-width: 768px) {
            /* Formulários ocupam 100% da tela */
            .stNumberInput, .stSelectbox, .stTextInput {
                width: 100% !important;
            }
            /* Espaçamento reduzido */
            .main .block-container {
                padding: 0.5rem !important;
            }
            /* Tamanho de fonte maior em inputs */
            input {
                font-size: 16px !important;
            }
        }
        /* Botões mais largos em mobile */
        .stButton>button {
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Funções do Sistema
def registrar_material(tipo, quantidade_kg, valor_por_kg):
    """Registra entrada de material com peso em KG"""
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    novo_registro = {
        "data": data_hora,
        "tipo": tipo,
        "quantidade_kg": float(quantidade_kg),
        "valor_por_kg": float(valor_por_kg),
        "valor_total": float(quantidade_kg) * float(valor_por_kg)
    }
    df = pd.DataFrame([novo_registro])
    df.to_csv(ARQUIVO_PRINCIPAL, mode="a", header=not os.path.exists(ARQUIVO_PRINCIPAL), index=False)

def gerar_relatorio(tipo_relatorio):
    try:
        dados = pd.read_csv(ARQUIVO_PRINCIPAL)
        
        # Converter a coluna 'data' para string se necessário
        dados["data"] = dados["data"].astype(str)
        
        if tipo_relatorio == "diário":
            data_filtro = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
            dados_filtrados = dados[dados["data"].str.startswith(data_filtro)]
            nome_arquivo = f"{PASTA_RELATORIOS}/relatorio_diario_{data_filtro}.csv"
        else:
            dados["data"] = pd.to_datetime(dados["data"])  # Converter para datetime
            dados["mês"] = dados["data"].dt.month
            dados_filtrados = dados[dados["mês"] == datetime.now().month]
            nome_arquivo = f"{PASTA_RELATORIOS}/relatorio_mensal_{datetime.now().strftime('%Y-%m')}.csv"
        
        dados_filtrados.to_csv(nome_arquivo, index=False)
        return nome_arquivo
    except FileNotFoundError:
        return None
def calcular_estatisticas():
    """Calcula estatísticas consolidadas"""
    try:
        dados = pd.read_csv(ARQUIVO_PRINCIPAL)
        if dados.empty:
            return None
        estatisticas = dados.groupby("tipo").agg(
            total_kg=("quantidade_kg", "sum"),
            valor_total=("valor_total", "sum"),
            media_kg_dia=("quantidade_kg", "mean")
        ).reset_index()
        return estatisticas.sort_values("total_kg", ascending=False)
    except FileNotFoundError:
        return None

# Sidebar (Menu)
with st.sidebar:
    st.title("♻️ ReciclaReal")
    menu = st.radio(
        "Menu",
        ["Registrar Entrada", "Relatórios", "Estatísticas"],
        label_visibility="collapsed"
    )

# Páginas
if menu == "Registrar Entrada":
    st.header("📝 Registrar Material")
    with st.form(key="form_registro"):
        col1, col2 = st.columns(2)
        with col1:
            tipo_material = st.selectbox("Tipo de Material", MATERIAIS)
            quantidade_kg = st.number_input(
                "Peso (KG)",
                min_value=0.01,
                step=0.5,
                format="%.2f",
                key="peso"
            )
        with col2:
            valor_por_kg = st.number_input(
                "Valor por KG (R$)",
                min_value=0.01,
                step=0.01,
                format="%.2f",
                key="valor"
            )
        
        if st.form_submit_button("💾 Salvar", use_container_width=True):
            registrar_material(tipo_material, quantidade_kg, valor_por_kg)
            st.toast(f"✅ {quantidade_kg} KG de {tipo_material} salvos!", icon="✅")

elif menu == "Relatórios":
    st.header("📊 Relatórios")
    col1, col2 = st.columns(2, gap="small")
    with col1:
        if st.button("📅 Gerar Relatório Diário", use_container_width=True):
            arquivo = gerar_relatorio("diário")
            if arquivo:
                with open(arquivo, "rb") as f:
                    st.download_button(
                        "⬇️ Baixar CSV Diário",
                        f,
                        file_name=os.path.basename(arquivo),
                        use_container_width=True
                    )
            else:
                st.warning("Nenhum dado disponível", icon="⚠️")
    
    with col2:
        if st.button("📆 Gerar Relatório Mensal", use_container_width=True):
            arquivo = gerar_relatorio("mensal")
            if arquivo:
                with open(arquivo, "rb") as f:
                    st.download_button(
                        "⬇️ Baixar CSV Mensal",
                        f,
                        file_name=os.path.basename(arquivo),
                        use_container_width=True
                    )
            else:
                st.warning("Nenhum dado disponível", icon="⚠️")

elif menu == "Estatísticas":
    st.header("📈 Estatísticas")
    estatisticas = calcular_estatisticas()
    
    if estatisticas is not None:
        tab1, tab2 = st.tabs(["📋 Tabela", "📊 Gráfico"])
        
        with tab1:
            st.dataframe(
                estatisticas.style.format({
                    "total_kg": "{:.2f} KG",
                    "valor_total": "R$ {:.2f}",
                    "media_kg_dia": "{:.2f} KG/dia"
                }),
                use_container_width=True,
                hide_index=True
            )
        
        with tab2:
            st.bar_chart(
                estatisticas,
                x="tipo",
                y="total_kg",
                use_container_width=True
            )
    else:
        st.warning("Nenhum dado registrado ainda", icon="⚠️")

# Rodapé
st.markdown("---")
st.caption("Sistema ReciclaReal ♻️ | Desenvolvido para gestão de materiais recicláveis por Luan Oliveira")