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
    Clona el repositorio a tu máquina local:
    https://github.com/JoelSantaM/Blog.git

    Aplica las migraciones:
    python manage.py migrate

    Ejecuta el servidor de desarrollo:
    python manage.py runserver

    Abre tu navegador y navega a http://127.0.0.1:8000/ para ver el blog en funcionamiento.