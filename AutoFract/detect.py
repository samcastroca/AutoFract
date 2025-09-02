from ultralytics import YOLO
import os
import cv2 as cv
from PIL import Image

def predict(img, confidence, st):
    """
    Función para realizar la detección utilizando el modelo preentrenado.
    
    Parámetros:
        img: Imagen de entrada en formato OpenCV.
        confidence: Umbral de confianza para la detección.
        st: Objeto Streamlit para mostrar los resultados.
    """
   
    model_path = os.path.join(os.path.dirname(__file__), "best(2).pt")
 
    
    model = YOLO(model_path)
    
    # Realizar la predicción con el modelo
    results = model.predict(img, conf=confidence)
    result = results[0]
    
    print("\n[INFO] Número de objetos detectados:", len(result.boxes))
    
    # Generar la imagen con las detecciones dibujadas
    for r in results:
        im_array = r.plot()  # Obtiene un array BGR con las predicciones dibujadas
        im = Image.fromarray(im_array[..., ::-1])  # Convertir a RGB para mostrar correctamente
    
    st.subheader('Imagen de Salida')
    st.image(im, channels="BGR", use_container_width=True)


