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

# Diccionario con las 10 preguntas genéricas y sus opciones mapeadas a los perfiles (A, B, C)
preguntas = [
    {
        "pregunta": "1. Estás en camino a un compromiso importante y tu transporte falla (se pincha una llanta, el bus se vara, hay un trancón masivo). ¿Cuál es tu reacción inicial?",
        "opciones": {
            "Me frustro muchísimo por la mala suerte y siento que el día se arruinó por completo.": "A",
            "Me lleno de ansiedad pensando en lo que van a decir los demás por mi retraso.": "B",
            "Acepto el hecho en un segundo. Aviso que llegaré tarde, busco la solución más rápida a la mano y ajusto mi plan.": "C"
        }
    },
    {
        "pregunta": "2. Estás trabajando en un proyecto (laboral o personal) y te enfrentas a un problema que parece no tener solución clara. ¿Cómo lo abordas?",
        "opciones": {
            "Me frustro y me obsesiono intentando que todo salga perfecto, aunque me tome muchísimo tiempo extra.": "A",
            "Me estreso por la presión, me bloqueo y empiezo a dudar si soy capaz de terminarlo.": "B",
            "Evalúo el problema con pragmatismo y aplico la solución más simple y efectiva que permita avanzar, aunque no sea perfecta.": "C"
        }
    },
    {
        "pregunta": "3. Faltando poco tiempo para entregar algo clave, se va la luz, se cae el internet o falla una herramienta externa. ¿Cómo lo interpretas?",
        "opciones": {
            "Como una injusticia de la vida o de la empresa proveedora que siempre me complica la existencia.": "A",
            "Como una crisis total que me genera pánico y me paraliza.": "B",
            "Como una prueba de estrés. Respiro, busco una contingencia inmediata (compartir datos, usar papel) y resuelvo con lo que tengo.": "C"
        }
    },
    {
        "pregunta": "4. Recibes una crítica dura sobre tu desempeño o sobre algo que hiciste con mucho esfuerzo. ¿Qué hace tu mente?",
        "opciones": {
            "Se pone a la defensiva inmediatamente para proteger mi orgullo y justificar por qué lo hice así.": "A",
            "Se toma el comentario de forma muy personal, arruinando mi estado de ánimo por varios días.": "B",
            "Separa el tono emocional de quien lo dice, extrae únicamente los datos que sirven para mejorar y desecha el resto.": "C"
        }
    },
    {
        "pregunta": "5. Te despiertas con cero motivación, estás cansado y tienes una lista de responsabilidades importantes por cumplir. ¿Qué haces?",
        "opciones": {
            "Pospongo todo lo que puedo. Si no tengo la energía o el ánimo correcto, no vale la pena hacer las cosas.": "A",
            "Me obligo a hacerlo, pero me quejo mentalmente y con los demás todo el día sobre lo cansado que estoy.": "B",
            "Me apoyo en la disciplina. Hago lo que tengo que hacer porque es mi deber, aceptando que hoy no daré el 100%, pero cumplo.": "C"
        }
    },
    {
        "pregunta": "6. Estás planificando un viaje importante o un evento clave para tu vida. ¿En qué se centra tu mente?",
        "opciones": {
            "En imaginar solo escenarios perfectos y molestarme si alguien sugiere que algo podría salir mal.": "A",
            "En sentir ansiedad por todo lo que desconozco y preocuparme por cosas que aún no pasan.": "B",
            "En mapear sistemáticamente qué podría salir mal (clima, retrasos, dinero) para tener planes de contingencia o plan B listos.": "C"
        }
    },
    {
        "pregunta": "7. Alguien es grosero contigo sin razón aparente en la calle o en una fila. ¿Cuánto dura tu reacción?",
        "opciones": {
            "Me arruina la mañana. Sigo pensando en lo estúpida que es la gente y le cuento la historia a todos.": "A",
            "Me asusto, me siento intimidado y me quedo con una sensación de incomodidad prolongada.": "B",
            "Me molesta unos segundos, recuerdo que mi paz mental es más valiosa que un desconocido que no controlo, y paso la página.": "C"
        }
    },
    {
        "pregunta": "8. Te encuentras con un obstáculo grande que frena tus planes a mediano plazo (un gasto imprevisto, un cambio de reglas). ¿Cuál es tu diálogo interno?",
        "opciones": {
            "¿Por qué siempre me pasan estas cosas a mí?": "A",
            "Esto es una señal de que debería abandonar este plan por completo, es muy arriesgado.": "B",
            "El obstáculo es el camino. Toca recalcular la ruta; resolver esto me dará más experiencia.": "C"
        }
    },
    {
        "pregunta": "9. Al terminar el día, ¿cómo mides si fue un 'buen día'?",
        "opciones": {
            "Si recibí halagos, reconocimiento en redes o si los demás me dieron la razón.": "A",
            "Si tuve suerte y no tuve que enfrentar ningún conflicto o problema difícil.": "B",
            "Si tomé buenas decisiones, mantuve mis valores y me enfoqué en lo que estaba bajo mi control.": "C"
        }
    },
    {
        "pregunta": "10. Lees un mensaje ambiguo de tu jefe, un cliente o tu pareja que podría interpretarse como un reclamo. ¿Qué haces?",
        "opciones": {
            "Asumo lo peor, imagino que están furiosos y empiezo a armar una defensa agresiva en mi cabeza.": "A",
            "Lo ignoro o respondo con evasivas por miedo a enfrentar una posible confrontación.": "B",
            "Leo estrictamente las palabras escritas sin añadirles tono emocional. Si necesito claridad, hago una pregunta directa.": "C"
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
