import os
import random
from deepface import DeepFace

# Directorio de la base de datos
db = './database'

# Obtener todas las imagenes de la base de datos
image_files = [f for f in os.listdir(db) if f.endswith('.jpg')]

def facial_recognition(image1: str, image2: str, own_db: bool) -> None:
    # Asegurarse que sean distintas
    if image1 == image2:
        print("Las imagenes deben ser distintas.")
        return

    # Compararlas usando DeepFace
    try:
        result = DeepFace.verify(image1, image2)
    except:
        print("Error al comparar las imagenes.")
        return

    # Mostrar los resultados
    print("Son la misma persona." if result["verified"] else "Persona distinta.")

    # Verificar si la prediccion fue correcta
    if own_db:
        if image1[-11:-5] == image2[-11:-5] and result["verified"] == True:
            print("La prediccion fue correcta (está bien que haya dicho que sí son la misma persona).\n")
        elif image1[-11:-5] != image2[-11:-5] and result["verified"] == False:
            print("La prediccion fue correcta (está bien que haya dicho que no son la misma persona).\n")
        elif image1[-11:-5] == image2[-11:-5] and result["verified"] == False:
            print("La prediccion fue incorrecta (está mal que haya dicho que no son la misma persona).\n")
        else:
            print("La prediccion fue incorrecta (está mal que haya dicho que sí son la misma persona).\n")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='DeepFace Recognition')
    parser.add_argument('-i1', '--image1', required=True, type=str, help='Path de la primera imagen')
    parser.add_argument('-i2','--image2', required=True, type=str, help='Path de la segunda imagen')
    parser.add_argument('--own_db', type=bool, default=False, help='Path de la base de datos')
    args = parser.parse_args()

    img1_path = args.image1
    img2_path = args.image2
    own_db = args.own_db

    facial_recognition(img1_path, img2_path, own_db)