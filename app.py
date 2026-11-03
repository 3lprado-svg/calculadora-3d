```python
import streamlit as st

# Configuração da página e visualização no celular/navegador
st.set_page_config(
    page_title="Precificador 3D",
    page_icon="🖨️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Estilização leve para botões e caixas de resultado
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🖨️ Precificador de Impressão 3D")
st.write("Calcule o valor ideal de venda para suas peças impressas de forma simples e rápida.")

# --- BARRA LATERAL: PARÂMETROS OPERACIONAIS ---
st.sidebar.header("⚙️ Custos Base da Operação")
st.sidebar.write("Ajuste os valores abaixo conforme sua realidade:")

preco_kg = st.sidebar.number_input("Preço do kg do Filamento (R$)", value=90.0, step=5.0)
tarifa_kwh = st.sidebar.number_input("Tarifa de Energia kWh (R$)", value=1.00, step=0.05)
potencia_kw = st.sidebar.number_input("Consumo Média da Impressora (kW)", value=0.12, step=0.01, help="0.12 kW = 120W")
taxa_depreciacao = st.sidebar.number_input("Depreciação por Hora (R$)", value=1.00, step=0.25)
valor_hora_mao_obra = st.sidebar.number_input("Sua Hora Técnico/Acabamento (R$)", value=30.0, step=5.0)
custo_embalagem = st.sidebar.number_input("Custo de Embalagem por Peça (R$)", value=3.00, step=0.50)
multiplicador = st.sidebar.number_input("Multiplicador de Lucro / Taxas", value=2.2, step=0.1)

st.markdown("---")

# --- CORPO PRINCIPAL: ENTRADA DE DADOS DA PEÇA ---
st.subheader("📦 Dados da Peça Fatiada")

col1, col2 = st.columns(2)

with col1:
    peso_g = st.number_input("Peso total da peça (gramas)", value=150.0, step=10.0, help="Inclua o peso dos suportes e brim/raft")
    horas_impressao = st.number_input("Tempo de impressão (horas)", value=6.0, step=0.5)

with col2:
    horas_mao_obra = st.number_input("Sua mão de obra (horas)", value=0.5, step=0.1, help="Tempo gasto fatiando, limpando e embalando")

# --- LÓGICA DE CÁLCULO ---
# Custo do material com 15% de margem de perda/suporte
custo_material = (peso_g / 1000) * preco_kg * 1.15
# Custo de energia consumida
custo_energia = (potencia_kw * horas_impressao) * tarifa_kwh
# Custo de depreciação/manutenção da máquina
custo_depreciacao = horas_impressao * taxa_depreciacao
# Custo da sua mão de obra
custo_mao_obra = horas_mao_obra * valor_hora_mao_obra
# Custo total de fabricação
custo_total = custo_material + custo_energia + custo_depreciacao + custo_mao_obra + custo_embalagem
# Preço final sugerido
preco_venda = custo_total * multiplicador

st.markdown("---")

# --- EXIBIÇÃO DE RESULTADOS ---
if st.button("📊 CALCULAR PREÇO DE VENDA", type="primary"):
    st.subheader("💡 Resumo Financeiro")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.metric("🧵 Material (com perdas)", f"R$ {custo_material:.2f}")
        st.metric("⚡ Energia Elétrica", f"R$ {custo_energia:.2f}")
        st.metric("🛠️ Depreciação da Máquina", f"R$ {custo_depreciacao:.2f}")
        
    with col_b:
        st.metric("🎨 Mão de Obra / Acabamento", f"R$ {custo_mao_obra:.2f}")
        st.metric("📦 Embalagem & Insumos", f"R$ {custo_embalagem:.2f}")
        st.metric("🧾 CUSTO TOTAL DE PRODUÇÃO", f"R$ {custo_total:.2f}")
        
    st.markdown("---")
    st.success(f"### 🚀 PREÇO DE VENDA SUGERIDO: **R$ {preco_venda:.2f}**")
    st.caption("O preço sugerido considera o multiplicador para cobrir taxas de cartão/plataformas e gerar lucro líquido real.")
```
