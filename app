import streamlit as st
from collections import Counter

# Configuración básica de la interfaz
st.set_page_config(page_title="Test de Estoicismo Operativo", page_icon="🏛️", layout="centered")

st.title("🏛️ Test de Estoicismo Operativo")
st.markdown("""
Evalúa cómo operas bajo presión en el mundo real. 
Elige la respuesta que describa tu reacción **más natural e instintiva**, no la que suene mejor en la teoría.
""")
st.divider()

# Diccionario con las 10 preguntas y sus opciones mapeadas a los perfiles (A, B, C)
preguntas = [
    {
        "pregunta": "1. Estás a la mitad de una ruta exigente y una llanta se raja de forma imprevista, retrasando tu cronograma. ¿Cuál es tu reacción inicial?",
        "opciones": {
            "Me frustro muchísimo por la mala suerte y siento que el día de entrenamiento se arruinó.": "A",
            "Me preocupo por si lograré llegar a tiempo o si el clima empeorará mientras reparo.": "B",
            "Acepto el hecho en un segundo. Saco mis herramientas, aplico la solución más rápida a la mano y sigo.": "C"
        }
    },
    {
        "pregunta": "2. Estás desarrollando una arquitectura de software compleja y te enfrentas a un cuello de botella. ¿Cómo lo resuelves?",
        "opciones": {
            "Me obsesiono intentando diseñar la solución teórica más perfecta y elegante posible, aunque tome semanas.": "A",
            "Me estreso por la presión y pruebo diferentes cosas al azar esperando que alguna funcione.": "B",
            "Evalúo el problema con pragmatismo y aplico la solución más simple y efectiva para que el engranaje gire.": "C"
        }
    },
    {
        "pregunta": "3. Un servidor externo o base de datos falla justo antes de la entrega de un proyecto. ¿Cómo lo interpretas?",
        "opciones": {
            "Como una injusticia del sistema o del proveedor que siempre me complica la vida.": "A",
            "Como una crisis que me genera pánico y me hace dudar de mis capacidades.": "B",
            "Como la prueba de estrés perfecta para demostrar mi capacidad de resolución y hacer el sistema tolerante a fallos.": "C"
        }
    },
    {
        "pregunta": "4. Recibes una retroalimentación bastante dura sobre la gestión de uno de tus proyectos. ¿Qué hace tu mente?",
        "opciones": {
            "Se pone a la defensiva inmediatamente para proteger mi reputación y justificar mis decisiones.": "A",
            "Se toma el comentario de forma personal, afectando mi estado de ánimo el resto del día.": "B",
            "Separa el tono emocional de la otra persona, extrae únicamente los datos objetivos útiles y desecha el ruido.": "C"
        }
    },
    {
        "pregunta": "5. Tienes un día con cero motivación, estás cansado y debes cumplir con un bloque de entrenamiento o estudio. ¿Qué haces?",
        "opciones": {
            "Pospongo la sesión. Si no tengo la energía correcta, no vale la pena hacerlo a medias.": "A",
            "Me obligo a hacerlo mientras me quejo mentalmente todo el tiempo sobre lo miserable que es.": "B",
            "Me apoyo en la disciplina. Ejecuto el trabajo porque es lo que dicta mi sistema, aceptando que hoy no será mi mejor rendimiento.": "C"
        }
    },
    {
        "pregunta": "6. Estás planificando un viaje de varios días o el lanzamiento de una herramienta técnica. ¿En qué te enfocas?",
        "opciones": {
            "En visualizar el éxito total y pensar en lo increíble que será cuando todo salga bien.": "A",
            "En sentir ansiedad por todo lo que desconozco y dudar si estoy realmente preparado.": "B",
            "En mapear sistemáticamente los puntos de fallo (clima, hardware, bugs) para tener planes de contingencia listos.": "C"
        }
    },
    {
        "pregunta": "7. Alguien comete una imprudencia en el tráfico o es grosero contigo. ¿Cuánto dura tu reacción?",
        "opciones": {
            "Me arruina la mañana. Sigo pensando en lo estúpida que es la gente y lo comento más tarde.": "A",
            "Me asusto y me quedo con una sensación de nerviosismo prolongada.": "B",
            "Me molesta unos segundos, recuerdo que mi tiempo es valioso para gastarlo en lo que no controlo, y paso la página.": "C"
        }
    },
    {
        "pregunta": "8. Te encuentras con un obstáculo físico o técnico que parece insuperable. ¿Cuál es tu diálogo interno?",
        "opciones": {
            "¿Por qué me pasa esto a mí justo ahora?": "A",
            "Creo que esto es una señal de que debería abandonar este camino.": "B",
            "El obstáculo es el camino. Resolver esto es exactamente lo que necesito para subir al siguiente nivel.": "C"
        }
    },
    {
        "pregunta": "9. Al evaluar el éxito de un día de trabajo, ¿qué métrica utilizas?",
        "opciones": {
            "Cuántos aplausos, reconocimiento o validación externa recibí.": "A",
            "Si tuve suerte y no ocurrió ningún problema grave.": "B",
            "Si tomé buenas decisiones, mantuve mi disciplina y me enfoqué en lo que estaba bajo mi control.": "C"
        }
    },
    {
        "pregunta": "10. Lees un correo ambiguo de un cliente o superior que podría interpretarse como queja. ¿Qué haces?",
        "opciones": {
            "Asumo lo peor, imagino que están furiosos y empiezo a armar una defensa mental.": "A",
            "Lo ignoro por miedo a enfrentar una posible confrontación.": "B",
            "Leo estrictamente las palabras. No añado historias emocionales. Si necesito claridad, hago una pregunta directa.": "C"
        }
    }
]

# Inicializamos la lista para guardar los resultados
respuestas_usuario = []

# Formulario para evitar recargas incesantes
with st.form("cuestionario_estoico"):
    for i, q in enumerate(preguntas):
        st.subheader(q["pregunta"])
        # Mostramos las opciones (las llaves del diccionario)
        opciones_texto = list(q["opciones"].keys())
        respuesta_seleccionada = st.radio("Selecciona tu reacción:", opciones_texto, key=f"q_{i}", label_visibility="collapsed")
        
        # Guardamos la letra correspondiente (A, B o C)
        respuestas_usuario.append(q["opciones"][respuesta_seleccionada])
        st.write("---")
        
    submitted = st.form_submit_button("Generar Reporte de mi Sistema Operativo", use_container_width=True)

# Lógica de evaluación una vez se envía el formulario
if submitted:
    st.header("📊 Tu Reporte de Sistema Operativo Mental")
    
    # Contamos las respuestas
    conteo = Counter(respuestas_usuario)
    total_A = conteo.get("A", 0)
    total_B = conteo.get("B", 0)
    total_C = conteo.get("C", 0)
    
    # Mostramos el desglose
    col1, col2, col3 = st.columns(3)
    col1.metric("Perfil A (Emoción/Ego)", f"{total_A}/10")
    col2.metric("Perfil B (Ansiedad)", f"{total_B}/10")
    col3.metric("Perfil C (Estoicismo)", f"{total_C}/10")
    
    st.divider()
    
    # Determinamos la categoría dominante
    max_respuestas = max(total_A, total_B, total_C)
    
    if max_respuestas == total_C:
        st.success("🎯 **DIAGNÓSTICO: TIENES UN SISTEMA OPERATIVO ESTOICO.**")
        st.write("""
        Valoras el pragmatismo, separas los hechos objetivos de las historias emocionales y no desperdicias recursos mentales en lo que no controlas. 
        Eres funcional, resiliente y tienes la capacidad de utilizar los problemas técnicos o físicos como herramientas directas para mejorar tu diseño y tu rendimiento.
        """)
    elif max_respuestas == total_A:
        st.error("🔥 **DIAGNÓSTICO: ENFOQUE IMPULSADO POR EL EGO Y LA EMOCIÓN.**")
        st.write("""
        Gastas demasiada energía luchando contra realidades que no puedes cambiar. Te frustras rápidamente cuando los sistemas externos 
        o las personas no cumplen tus expectativas exactas. El reto aquí es soltar la necesidad de perfección externa y enfocarte en tu propia ejecución.
        """)
    else:
        st.warning("🌪️ **DIAGNÓSTICO: ENFOQUE IMPULSADO POR LA ANSIEDAD.**")
        st.write("""
        Tu mente gasta muchos recursos anticipando desastres que aún no ocurren. Te preocupas en exceso por el futuro y te dejas paralizar 
        por la fricción del entorno, lo que reduce drásticamente tu eficiencia. El objetivo debe ser anclarte al momento presente y resolver los problemas paso a paso.
        """)
