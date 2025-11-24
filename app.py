import streamlit as st

st.set_page_config(
    page_title="Timeline - Volatilidad del Tipo de Cambio en Compras",
    page_icon="💱",
    layout="centered"
)

st.title("💱 Timeline: Evolución del análisis de la volatilidad del tipo de cambio")
st.write(
    "Mueve el slider para ver cómo, a lo largo de los años, ha evolucionado el análisis "
    "de la volatilidad del tipo de cambio y su impacto en el área de Compras y Logística."
)

# --------------------------------------------------------------------
# 1) IMÁGENES DEL TIMELINE (YA CON TUS URLs)
# --------------------------------------------------------------------
IMAGES = [
    "https://raw.githubusercontent.com/LuisCamposD/timeline_s1/main/timeline_images/img1.png",  # punto 1
    "https://raw.githubusercontent.com/LuisCamposD/timeline_s1/main/timeline_images/img2.jpg",  # punto 2
    "https://raw.githubusercontent.com/LuisCamposD/timeline_s1/main/timeline_images/img3.png",  # punto 3
    "https://raw.githubusercontent.com/LuisCamposD/timeline_s1/main/timeline_images/img4.png",  # punto 4
    "https://raw.githubusercontent.com/LuisCamposD/timeline_s1/main/timeline_images/img5.png",  # punto 5
]

CAPTIONS = [
    "Años 80–90: enfoque básico",
    "Años 2000: apertura y exposición",
    "2008–2012: crisis y gestión del riesgo",
    "2013–2019: digitalización y analítica",
    "2020 en adelante: IA y decisiones inteligentes",
]

# --------------------------------------------------------------------
# 2) CONTENIDO DEL TIMELINE (EVOLUCIÓN HISTÓRICA)
# --------------------------------------------------------------------
TIMELINE = [
    {
        "titulo": "1️⃣ Años 80–90: tipo de cambio y compras casi desconectados",
        "resumen": (
            "En esta etapa el análisis de la volatilidad era mínimo. "
            "El tipo de cambio se veía como un dato macro, no como un insumo clave "
            "para las decisiones de logística."
        ),
        "bullets": [
            "Planeación de compras principalmente basada en experiencia y listas de precios históricas.",
            "Poca apertura comercial: menor participación de proveedores internacionales.",
            "El tipo de cambio se revisaba esporádicamente, no todos los días.",
            "No existían políticas claras sobre quién asumía el riesgo cambiario (proveedor vs empresa).",
        ],
    },
    {
        "titulo": "2️⃣ Años 2000: apertura comercial y mayor exposición al dólar",
        "resumen": (
            "Con la globalización y el aumento de importaciones, el tipo de cambio empieza "
            "a impactar directamente los costos logísticos."
        ),
        "bullets": [
            "Más compras en dólares (equipos, repuestos, tecnología, mobiliario importado).",
            "Compras empieza a comparar cotizaciones en distintas monedas, pero el análisis es manual (Excel básico).",
            "Se empiezan a usar tipos de cambio referenciales para presupuestos, pero sin escenarios de volatilidad.",
            "Mayor sensibilidad en los márgenes: variaciones de centavos ya impactan el costo total de los proyectos.",
        ],
    },
    {
        "titulo": "3️⃣ 2008–2012: crisis financiera y prioridad al riesgo cambiario",
        "resumen": (
            "La crisis global y los saltos bruscos del tipo de cambio obligan a formalizar "
            "la gestión del riesgo cambiario en compras y contratos."
        ),
        "bullets": [
            "Logística y Finanzas comienzan a trabajar juntos para definir TC de referencia y bandas de variación.",
            "Aparecen cláusulas específicas: ajuste de precio por tipo de cambio, vigencia corta de cotizaciones.",
            "Se analizan escenarios básicos: ¿qué pasa si el dólar sube 5%, 10% durante el proyecto?",
            "Compras prioriza cerrar rápidamente órdenes de compra críticas para evitar descalce entre aprobación y pago.",
        ],
    },
    {
        "titulo": "4️⃣ 2013–2019: digitalización, BI y monitoreo diario del tipo de cambio",
        "resumen": (
            "Las empresas adoptan ERPs, dashboards y reportes automáticos. "
            "El tipo de cambio se vuelve un indicador operativo para logística."
        ),
        "bullets": [
            "Dashboards de compras que muestran el impacto del tipo de cambio en el presupuesto y en el costo por contrato.",
            "Actualización diaria del tipo de cambio en sistemas (ERP) y en las plantillas de cuadros comparativos.",
            "Uso de modelos estadísticos simples para proyectar TC anual y armar presupuestos más realistas.",
            "Compras empieza a definir estrategias: adelantar o postergar compras según tendencias de tipo de cambio.",
        ],
    },
    {
        "titulo": "5️⃣ 2020 en adelante: disrupciones globales, analítica avanzada e IA",
        "resumen": (
            "Con la pandemia y los choques globales, la volatilidad del tipo de cambio se combina con "
            "rupturas de cadena de suministro. Compras necesita decisiones más inteligentes y rápidas."
        ),
        "bullets": [
            "Uso de analítica avanzada e IA para simular escenarios de tipo de cambio y su efecto en costos logísticos.",
            "Modelos que recomiendan: comprar ahora vs esperar, cambiar de proveedor, negociar en otra moneda o ajustar incoterms.",
            "Integración de datos de mercado (TC, commodities, fletes internacionales) con datos internos de consumo y stock.",
            "El rol de Compras/Logística evoluciona: de ejecutor de órdenes a gestor estratégico del riesgo cambiario y de suministro.",
        ],
    },
]

# --------------------------------------------------------------------
# 3) SLIDER DEL TIMELINE
# --------------------------------------------------------------------
step = st.slider(
    "Selecciona la etapa del timeline:",
    min_value=1,
    max_value=5,
    value=1,
    step=1,
)

idx = step - 1
item = TIMELINE[idx]

st.subheader(item["titulo"])

st.image(
    IMAGES[idx],
    caption=CAPTIONS[idx],
    use_container_width=True,
)

st.markdown(f"**Resumen:** {item['resumen']}")

st.markdown("**¿Qué pasa en esta etapa?**")
for bullet in item["bullets"]:
    st.markdown(f"- {bullet}")

st.progress(idx / 4)
