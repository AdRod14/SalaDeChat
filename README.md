
# Sala de Chat - Proyecto de Comunicación entre Procesos

![Proyecto en acción](https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/267_Python_logo-512.png) <!-- Puedes agregar una imagen o un GIF de tu proyecto aquí -->

## Descripción General del Proyecto

La idea central de este proyecto es desarrollar una sala de chat que se inspira en las prácticas de la Unidad III de la clase de Sistemas Operativos: IPC (Comunicación Entre Procesos). El objetivo es aplicar los conocimientos adquiridos en el curso para crear una sala de chat que permita la comunicación simultánea entre dos o más usuarios.

### ¿Por qué este proyecto?

Los sockets desempeñan un papel fundamental en la comunicación de red y la interacción entre procesos en un sistema informático. Este proyecto utiliza sockets para implementar la comunicación, ya que proporcionan una solución simple y efectiva para el problema. Además, los sockets ofrecen una baja latencia en la entrega de mensajes, esencial para una experiencia de chat en tiempo real.

## Funcionalidades Específicas

- Servidor de chat: Se desarrolla un script de servidor que actúa como el punto central de la sala de chat, administrando la comunicación entre clientes.
- Clientes de chat: Se crea un script de cliente que permite a los usuarios unirse al chat y participar en la conversación.
- Comunicación en tiempo real: Los usuarios pueden escribir mensajes y presionar "Enter" para enviarlos, permitiendo una comunicación en tiempo real.
- Interfaz de usuario: La interfaz de usuario se realiza a través de la terminal.
- Mensajes con emisor: Cada mensaje enviado muestra al emisor junto con el contenido.
- Manejo de conexiones múltiples: El servidor es capaz de manejar múltiples conexiones de clientes simultáneamente.
- Utilización de sockets: El proyecto utiliza sockets TCP para la comunicación.

## Recursos/Tecnologías Utilizadas

- Python 3.10.12: Lenguaje de programación de alto nivel con sintaxis sencilla y legible.
- TCP Sockets: Mecanismo de comunicación que permite la comunicación entre procesos a través de la red.
- Módulo Socket y Módulo Thread: Utilizados para crear y gestionar conexiones de red y trabajar con subprocesos.
- Diccionario de Clientes: Estructura de datos utilizada para almacenar y gestionar clientes conectados al servidor.

## Instrucciones de Uso

### Crear entorno virtual
Para la instalación se necesita Python > 3.10.12 . Primeramente se crea un entorno virtual dentro del directorio raíz del proyecto.

GNU/Linux o MacOS:
```
$ python3 -m venv venv
$ source ./venv/bin/activate
```

Luego, se instalan las dependencias usando pip.

GNU/Linux o MacOS:
```
$ (venv) python3 -m pip install -r requirements.txt
```
```
### Desactivar el entorno virtual

Para desactivar el entorno virtual, ejecuta el siguiente comando:

GNU/Linux o MacOS:
```
$ (venv) deactivate
```
## Ejecutar Cliente


## Ejecutar Servidor


## Contribuciones

Si deseas contribuir a este proyecto, ¡estamos abiertos a colaboraciones! Puedes enviar pull requests o informar sobre problemas (issues) que encuentres.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.


