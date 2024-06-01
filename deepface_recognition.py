import os
import random
from deepface import DeepFace

# Directorio de la base de datos
db = './database'

# Obtener todas las imagenes de la base de datos
image_files = [f for f in os.listdir(db) if f.endswith('.jpg')]

for _ in range(15):
    # Seleccionar dos imagenes aleatorias
    img1_path = random.choice(image_files)
    img2_path = random.choice(image_files)

    # Asegurarse que sean distintas
    while img1_path == img2_path:
        img2_path = random.choice(image_files)

    # Compararlas usando DeepFace
    try:
        result = DeepFace.verify(os.path.join(db, img1_path), os.path.join(db, img2_path))
    except:
        continue

    # Mostrar los resultados
    print("Son la misma persona." if result["verified"] else "Persona distinta.")

    # Verificar si la prediccion fue correcta
    if img1_path[:6] == img2_path[:6] and result["verified"] == True:
        print("La prediccion fue correcta (está bien que haya dicho que sí son la misma persona).\n")
    elif img1_path[:6] != img2_path[:6] and result["verified"] == False:
        print("La prediccion fue correcta (está bien que haya dicho que no son la misma persona).\n")
    elif img1_path[:6] == img2_path[:6] and result["verified"] == False:
        print("La prediccion fue incorrecta (está mal que haya dicho que no son la misma persona).\n")
    else:
        print("La prediccion fue incorrecta (está mal que haya dicho que sí son la misma persona).\n")