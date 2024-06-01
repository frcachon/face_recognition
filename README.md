## Prototipo de software de reconocimiento facial
### Entrega 3 de Ethical Hacking

- Clonar el repositorio usando `git clone`.

- Instalar el módulo DeepFace usando `pip install deepface`.

- Correr el script usando `python deepface_recognition.py -i1 PATH_IMAGE_1 -i2 PATH_IMAGE_2`.

#### Argumentos
- Los argumentos `-i1 (--image1)` y `-i2 (--image2)` son requeridos.

- El argumento `own_db` refiere a si las imágenes son ambas de la base de datos local, la cual, por su etiquetado actúa como groundtruth de la predicción. En caso de que se usen ambas imágenes de la db, es recomendable agregar al comando de ejecución: `--own_db True` así se podrá saber si la predicción realizada fue correcta o no. Este argumento tiene `False` como valor por defecto, por lo que sólo se mostrará el resultado de la predicción en consola.

#### Ejemplo de uso
Un posible comando a utilizar, con imagenes de la base de datos etiquetada es el siguiente:

`python deepface_recognition.py -i1 ./database/Forlan2.jpg -i2 ./database/Cavani3.jpg --own_db True`