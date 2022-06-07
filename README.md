# Proyecto Final
Autor: Eduardo Romero
-----------------------------

La aplicación cuenta con

●	NavBar  donde se pueden observar los botones de acceso a diferentes modulos ( Perfil/Mensajeria/Anuncios/Login/Logout/Posteos/Pages )   
●	Home    donde visualizamos los posteos realizados por los usuarios, además de contener Anuncios por parte de la administración
●	About   en la parte inferior derecha contamos con un hipervinculo que nos lleva a la página de about donde podremos saber un poco más del creador
●	Pages   un listado resumido de los posteos donde el administrador puede ver los usuarios creadores, fechas, etc, además de ver detalle y editar/borrar
●	Login   un login para usuarios/admin
●	Signup  una página de registro para ser miembro del blog
●	Messages  un sistema de mensajeria donde los usuarios se pueden comunicar entre si, se puede acceder al mismo a través del modulo mensajería o bien, clickeando algún comentario de otro usuario, y desde la lista de usuarios ( que se puede ver en la parte inferior derecha de la web), el sistema de mensajería además, muestra en el inicio cuando el usuario tiene mensajes sin leer, y puede acceder por hipervinculo clickeando dicho texto, el módulko de mensajeria cuenta con 3 submodulos, donde podrá ver los mensajes enviados, no leidos y enviar un mensaje.
●	Profile una página para el perfil donde el usuario tiene la posibilidad de modificar su avatar, de agregar datos personales como nombre y apellido, cambiar su email o contraseña.
●	Logout  un logout para terminar la sesión del usuario.
●	Get pages donde vemos el listado de paginas que puede acceder el admin.
●	Get page  para poder editar/borrar posteos.
●	Create page donde podemos crear posteos desde el modulo mis post.
●	Update Page El usuario puede modificar su propio post para actualizar información. (Solo el admin tiene la potestad de editar cualquier post)
●	Delete page El usuario puede eliminar su propio post. (Solo el admin tiene la potestad de borrar cualquier post)
●	Get profile Obtencion del perfil para actualizarlo.
●	Update profile Se podrá actualizar el avatar, y datos de la cuenta.
●	Validaciones:
La aplicación además, posee validaciones para que un usuario común no tenga acceso a donde si los tiene el admin, estos usuarios al ser creados, son asignados automaticamente un grupo "Usuarios comunes", si bien no ven las opciones que tiene un admin, si intentan ingresar por URL no podrán ya que hay validaciones en todo el sitio. Lo mismo sucede con un usuario no registrado, este será siempre redirigido a la pagina de login si intenta realizar alguna acción que no tiene permitida como usuario no-registrado.
La aplicación cuenta con un sector de anuncios especialmente para administradores, donde los mismos tendrán la posibilidad de hacer un anuncio rápido a traves de la aplicación con un formato básico, o bien con formato de texto avanzado (texto enriquecido) a través de la administración de Django. Los anuncios creados son vistos por todos los visitantes de la pagina en el inicio, ya sean usuarios registrados o no.

También cuenta con un sistema de comentarios donde podremos opinar de los posteos que realizan los usuarios estableciendo así también una comunicación donde se podrán expresar opiniones, mostrando el usuario, el comentario y la fecha, además los usuarios con selecconables y esto nos da la opcion de enviarles un mensaje privado para comunicarnos de una manera más directa.
