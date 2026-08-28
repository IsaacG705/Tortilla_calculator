import streamlit as st

st.set_page_config(page_title="Calculadora de Tortillas", page_icon="🫓", layout="centered")
#textos de la pantalla principal
st.title("🫓 Calculadora de Costos y Ganancias")
st.write("Calculá rápidamente el costo de producción, el precio sugerido y la ganancia neta.")

# 2. Entrada de Costos Fijos (Constante)
st.subheader("Costos Fijos")
costo_fijo = st.number_input("Ingrese los costos fijos totales ($):", min_value=0.0, value=0.0, step=100.0)

# 3. Entrada de Cantidad y Precio (Para calcular ingresos y escala)
st.subheader("Producción(Q) y Precio de venta(P)")
col1, col2 = st.columns(2)
with col1:
    cantidad = st.number_input("Cantidad de tortillas a producir (Q):", min_value=1, value=50, step=1)
with col2:
    precio_unitario = st.number_input("Precio de venta por unidad (P):", min_value=0.0, value=500.0, step=10.0)
    
# Mostramos un resumen rápido para verificar que los inputs funcionan
st.write("---")
st.write(f"**Estado actual:** Vas a producir {cantidad} unidades con un costo fijo de ${costo_fijo:,.2f}.")

Bash
streamlit run app.py