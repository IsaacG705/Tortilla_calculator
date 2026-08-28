import streamlit as st

# 1. Configuración inicial de la página
st.set_page_config(page_title="Calculadora de Tortillas", page_icon="🫓", layout="centered")

st.title("🫓 Calculadora de Costos y Beneficios")
st.write("Para que tengas todo ordenado.")

# 2. Entrada de Costos Fijos (Constante)
st.subheader("1. Costos Fijos")
costo_fijo = st.number_input("Ingrese los costos fijos totales ($):", min_value=0.0, value=0.0, step=100.0)

# 3. Nivel de Producción y Venta (Q y P)
st.subheader("2. Nivel de Producción y Venta")
col_q, col_p = st.columns(2)
with col_q:
    cantidad_producida = st.number_input("Cantidad de tortillas a producir (Q):", min_value=1, value=20, step=1, format="%d")
with col_p:
    precio_unitario = st.number_input("Precio de venta unitario (P) ($):", min_value=0.0, value=2000.0, step=10.0)

porcentaje_ganancia = st.number_input("Margen de ganancia deseado sobre el costo (%):", min_value=0.0, value=100.0, step=5.0)

# 4. El ARU: Asistente de Rendimiento Unitario (Costo por unidad de ingrediente)
st.subheader("3. Asistente de Rendimiento Unitario (ARU)")
st.markdown("*(Calcula cuánto cuesta cada ingrediente por cada tortilla individual)*")

# Harina
st.markdown("**• Harina**")
col_h1, col_h2 = st.columns(2)
with col_h1:
    precio_harina = st.number_input("Precio total del kilo de harina ($):", min_value=0.0, value=1000.0, step=100.0)
with col_h2:
    rendimiento_harina = st.number_input("¿Cuántas tortillas rinde ese kilo?:", min_value=1.0, value=3.0, step=1.0)
costo_harina_unitario = precio_harina / rendimiento_harina

# Grasa
st.markdown("**• Grasa**")
col_g1, col_g2 = st.columns(2)
with col_g1:
    precio_grasa = st.number_input("Precio total de la grasa ($):", min_value=0.0, value=3000.0, step=100.0)
with col_g2:
    rendimiento_grasa = st.number_input("¿Para cuántas tortillas rinde?:", min_value=1.0, value=10.0, step=1.0)
costo_grasa_unitario = precio_grasa / rendimiento_grasa

# Sal
st.markdown("**• Sal**")
col_s1, col_s2 = st.columns(2)
with col_s1:
    precio_sal = st.number_input("Precio total de la sal ($):", min_value=0.0, value=1000.0, step=100.0)
with col_s2:
    rendimiento_sal = st.number_input("¿Para cuántas tortillas rinde la sal?:", min_value=1.0, value=50.0, step=1.0)
costo_sal_unitario = precio_sal / rendimiento_sal

# Carbón
st.markdown("**• Carbón**")
col_c1, col_c2 = st.columns(2)
with col_c1:
    precio_carbon = st.number_input("Precio de la bolsa de carbón ($):", min_value=0.0, value=3000.0, step=100.0)
with col_c2:
    rendimiento_carbon = st.number_input("¿Para cuántas tortillas alcanza esta bolsa?:", min_value=1.0, value=100.0, step=1.0)
costo_carbon_unitario = precio_carbon / rendimiento_carbon

# Bolsas
st.markdown("**• Bolsas**")
costo_bolsa_unitario = st.number_input("Costo de la bolsa por unidad ($):", min_value=0.0, value=50.0, step=5.0)

# 5. Cálculo del Costo Variable Total y Beneficio al hacer clic en el botón
st.divider()

if st.button("Calcular Costos y Beneficios", type="primary"):
    # Costo variable por unidad sumando todos los insumos del ARU (incluyendo sal)
    costo_variable_unitario_total = costo_harina_unitario + costo_grasa_unitario + costo_sal_unitario + costo_carbon_unitario + costo_bolsa_unitario
    
    # Costo Variable Total = CV unitario * Cantidad
    costo_variable_total = costo_variable_unitario_total * cantidad_producida
    
    # Costo Total = Costo Fijo + Costo Variable Total
    costo_total = costo_fijo + costo_variable_total
    
    # Costo Medio Total por unidad
    costo_medio_total = costo_total / cantidad_producida
    
    # Ingresos Totales = P * Q
    ingreso_total = cantidad_producida * precio_unitario
    
    # Beneficio (Ganancia Neta) = Ingresos Totales - Costo Total
    beneficio = ingreso_total - costo_total
    
    # Beneficio Unitario
    beneficio_unitario = beneficio / cantidad_producida
    
    # Precio Sugerido en base al margen de ganancia configurado
    precio_sugerido = costo_medio_total * (1 + porcentaje_ganancia / 100)
    
    # Mostrar resultados en pantalla
    st.subheader("📊 Resultados Económicos de la Tanda")
    
    col_res1, col_res2 = st.columns(2)
    col_res1.metric("Costo Variable Total", f"${costo_variable_total:,.2f}")
    col_res2.metric("Costo Total (CF + CVT)", f"${costo_total:,.2f}")
    
    col_res3, col_res4 = st.columns(2)
    col_res3.metric("Ingreso Total (P × Q)", f"${ingreso_total:,.2f}")
    col_res4.metric("Ganancia Neta", f"${beneficio:,.2f}")
    
    st.info(f"**Costo unitario total por tortilla:** ${costo_medio_total:,.2f}")
    st.success(f"**Beneficio unitario por tortilla:** ${beneficio_unitario:,.2f} por unidad")
    st.warning(f"**Precio de venta sugerido (con un {porcentaje_ganancia}% de margen):** ${precio_sugerido:,.2f} por unidad")
    
    # --- APARTADO DE GANANCIAS DIVIDIDAS ---
    st.divider()
    st.subheader("📊 Distribución de Ganancias")
    ganancia_Leilu = beneficio / 2
    ganancia_Martin = beneficio / 2
    
    col_soc1, col_soc2 = st.columns(2)
    col_soc1.metric("Ganancia para Leilu (50%)", f"${ganancia_Leilu:,.2f}")
    col_soc2.metric("Ganancia para Martin (50%)", f"${ganancia_Martin:,.2f}")

    # --- PROYECCIONES TEMPORALES ---
    st.divider()
    st.subheader("📊 Proyecciones de Ganancia:")
    st.markdown("*(Calculado asumiendo este mismo volumen por tanda)*")
    
    # Asumimos la tanda como un ciclo de producción estándar
    ganancia_semana = beneficio * 7
    ganancia_mes = beneficio * 30
    ganancia_tres_meses = beneficio * 90
    
    col_t1, col_t2, col_t3 = st.columns(3)
    col_t1.metric("Proyección Semanal", f"${ganancia_semana:,.2f}")
    col_t2.metric("Proyección Mensual", f"${ganancia_mes:,.2f}")
    col_t3.metric("Proyección Trimestral", f"${ganancia_tres_meses:,.2f}")