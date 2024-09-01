# Blog
 

Este es un blog basico realizado en Django, este permite a los usuarios ver, buscar, filtrar, y editar publicaciones. Los usuarios pueden también agregar nuevas publicaciones.

Funcionalidades Implementadas

Listar Publicaciones:
    Visualiza una lista de todas las publicaciones.
    Implementa paginación para navegar entre páginas de publicaciones.

Buscar Publicaciones:
    Permite a los usuarios buscar publicaciones por título o contenido.
    Incluye filtros por categoría y fecha de publicación.

Filtrar Publicaciones:
    Los usuarios pueden filtrar las publicaciones por categoría.
    Permite filtros por fecha de publicación.

Ver Detalles de una Publicación:
    Muestra detalles completos de una publicación específica.
    Incluye información como el título, contenido, fecha de publicación, categoría y autor.

Editar Publicación:
    Permite editar una publicación existente.
    Los cambios se guardan y se reflejan en la vista de detalles de la publicación.

Agregar Nueva Publicación:
    Permite a los usuarios agregar nuevas publicaciones al blog.

Instalación y Ejecución Local
   Clonar el repositorio
git clone https://github.com/JoelSantaM/Blog.git

    Navegar al directorio del repositorio
cd Blog

    Crear y activar un entorno virtual
python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate     # Windows

    Instalar dependencias
pip install -r requirements.txt

    Aplicar migraciones
python manage.py migrate

    Iniciar el servidor de desarrollo
python manage.py runserver