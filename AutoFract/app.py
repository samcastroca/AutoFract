import streamlit as st
import cv2 as cv
import numpy as np
from PIL import Image
import detect

def main():
    # Configuración de la sidebar con estilo
    st.sidebar.title("Opciones")
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
            width:300px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
            width:300px;
            margin-left:-300px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # Título principal
    st.header("AutoFract: Detección Asistida de Fracturas Óseas")
        
    st.sidebar.markdown("----")
    confidence = st.sidebar.slider("Confianza", min_value=0.0, max_value=1.0, value=0.35)
        
    img_file_buffer = st.sidebar.file_uploader("Sube una imagen", type=['jpg','jpeg','png'], key=0)
    DEMO_IMAGE = os.path.join(os.path.dirname(__file__), "IMG0002444.jpg")
    
    if img_file_buffer is not None:
        # Convertir el contenido a un arreglo numpy
        file_bytes = np.asarray(bytearray(img_file_buffer.read()), dtype=np.uint8)
        img = cv.imdecode(file_bytes, 1)
        image = np.array(Image.open(img_file_buffer))
    else:
        img = cv.imread(DEMO_IMAGE)
        image = np.array(Image.open(DEMO_IMAGE))
    
    st.sidebar.text("Imagen Original")
    st.sidebar.image(image, use_column_width=True)
        
    # Ejecutar la detección y mostrar el resultado
    detect.predict(img, confidence, st)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
