import streamlit as st

st.set_page_config(
    page_title="Timeline - Volatilidad del Tipo de Cambio en Compras",
    page_icon="💱",
    layout="centered"
)

st.title("💱 Timeline: Volatilidad del tipo de cambio en Compras y Logística")
st.write(
    "Mueve el slider para ver cómo la volatilidad del tipo de cambio impacta "
    "las compras, las negociaciones con proveedores y las decisiones del área de logística."
)

# --------------------------------------------------------------------
# 1) IMÁGENES DEL TIMELINE
# --------------------------------------------------------------------
# Reemplaza USUARIO, REPO y BRANCH por los tuyos.
# Ejemplo:
#   USUARIO = "LuisCamposD"
#   REPO   = "Sesion1-Isil"
#   BRANCH = "main"
#
# Y reemplaza "img1.png"... por los nombres reales dentro de /timeline_images

IMAGES = [
    "https://raw.githubusercontent.com/USUARIO/REPO/BRANCH/timeline_images/img1.png",  # Fase 1
    "https://raw.githubusercontent.com/USUARIO/REPO/BRANCH/timeline_images/img2.png",  # Fase 2
    "https://raw.githubusercontent.com/USUARIO/REPO/BRANCH/timeline_images/img3.png",  # Fase 3
    "https://raw.githubusercontent.com/USUARIO/REPO/BRANCH/timeline_images/img4.png",  # Fase 4
    "https://raw.githubusercontent.com/USUARIO/REPO/BRANCH/timeline_images/img5.png",  # Fase 5
]

# --------------------------------------------------------------------
# 2) CONTENIDO DEL TIMELINE (VOLATILIDAD TC EN COMPRAS/LOGÍSTICA)
# --------------------------------------------------------------------

TIMELINE = [
    {
        "titulo": "1️⃣ Escenario estable: planificación de compras",
        "resumen": (
            "El tipo de cambio se mueve poco y de forma predecible. "
            "Compras puede planificar con relativa tranquilidad."
        ),
        "bullets": [
            "Presupuestos anuales definidos con un tipo de cambio referencial.",
            "Contratos en soles o dólares sin mucha discusión sobre quién asume el riesgo.",
            "Vigencia de cotizaciones más larga (7, 15 o 30 días).",
            "Impacto del tipo de cambio en el costo total es bajo o manejable."
        ],
    },
    {
        "titulo": "2️⃣ Inicio de la volatilidad: alertas para logística y compras",
        "resumen": (
            "El tipo de cambio empieza a subir y bajar con más fuerza en cortos periodos. "
            "Compras y logística empiezan a sentir presión."
        ),
        "bullets": [
            "Los proveedores acortan la vigencia de sus cotizaciones (24–48 horas).",
            "Se vuelve más difícil sostener los precios aprobados en comités o budgets.",
            "Órdenes de compra emitidas en soles se encarecen si el dólar sube antes del pago.",
            "Aumentan las re–cotizaciones y los correos de ajuste de precio."
        ],
    },
    {
        "titulo": "3️⃣ Impacto directo en negociaciones y contratos",
        "resumen": (
            "La volatilidad ya pega de frente en las negociaciones: "
            "la discusión pasa a ser quién asume el riesgo cambiario."
        ),
        "bullets": [
            "Proveedores piden cláusulas de ajuste: 'tipo de cambio al día de la factura o del pago'.",
            "Compras debe negociar bandas de tipo de cambio o topes de variación.",
            "Se evalúa contratar en dólares vs soles según la naturaleza del gasto.",
            "Mayor presión para cerrar rápido las aprobaciones internas (si no, el precio cambia)."
        ],
    },
    {
        "titulo": "4️⃣ Estrategias de mitigación desde Compras / Logística",
        "resumen": (
            "El área de compras ya no solo cotiza: gestiona el riesgo cambiario con estrategias "
            "operativas y de negociación."
        ),
        "bullets": [
            "Compras anticipadas o consolidadas para aprovechar momentos de tipo de cambio favorable.",
            "Coordinación con Finanzas para usar tipos de cambio forward o proyecciones oficiales.",
            "Diversificación de proveedores y monedas (por ejemplo, no depender solo de USD).",
            "Negociación de cláusulas de revisión de precios con reglas claras y documentadas."
        ],
    },
    {
        "titulo": "5️⃣ Madurez: uso de analítica e IA para decidir cuándo y cómo comprar",
        "resumen": (
            "La volatilidad se gestiona de forma más sofisticada: se usan datos, analítica "
            "e incluso IA para decidir el mejor momento y la mejor forma de comprar."
        ),
        "bullets": [
            "Modelos que simulan escenarios de tipo de cambio y su impacto en el costo total de compra.",
            "Priorización de órdenes críticas vs postergables según el riesgo cambiario.",
            "Dashboards para ver el impacto del tipo de cambio en el presupuesto y en el margen del negocio.",
            "Integración con IA para sugerir estrategias: comprar ahora, negociar en otra moneda, "
            "fraccionar vs consolidar compras, etc."
        ],
    },
]

CAPTIONS = [
    "Escenario estable",
    "Inicio de la volatilidad",
    "Impacto en negociaciones",
    "Estrategias de mitigación",
    "Madurez: analítica e IA",
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

# Imagen asociada a ese punto
st.image(
    IMAGES[idx],
    caption=CAPTIONS[idx],
    use_container_width=True,
)

st.markdown(f"**Resumen:** {item['resumen']}")

st.markdown("**¿Qué pasa en esta etapa?**")
for bullet in item["bullets"]:
    st.markdown(f"- {bullet}")

# Barra de progreso “visual” del avance en el timeline
st.progress(idx / 4)
