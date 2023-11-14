

# Sala de Chat - Proyecto de Comunicación entre Procesos

![Proyecto en acción](https://benisnous.com/wp-content/uploads/2021/07/Python-Socket-Programming-Tutorial.jpg) <!-- Puedes agregar una imagen o un GIF de tu proyecto aquí -->

## Contenido
- [Instrucciones de Uso](#Instalación)
- [Ejecutar Cliente](#Cliente)
- [Ejecutar Servidor]( #Servidor)
- [Licencia](#Licencia)

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
- Módulo Socket y Módulo Threading: Utilizados para crear y gestionar conexiones de red y trabajar con subprocesos.
- Diccionario de Clientes: Estructura de datos utilizada para almacenar y gestionar clientes conectados al servidor.

## Instalación

### Crear entorno virtual

#### Instalar venv
```
sudo apt install python3-venv
```

Para la instalación se necesita Python > 3.10.12 . Primeramente se crea un entorno virtual dentro del directorio raíz del proyecto.

GNU/Linux o MacOS:
```
$ python3 -m venv venv
$ source ./venv/bin/activate
```

Luego, se instalan las dependencias usando pip desde (venv).

GNU/Linux o MacOS:
```
$ python3 -m pip install -r requirements.txt
```

#### Desactivar el entorno virtual

Para desactivar el entorno virtual, ejecuta el siguiente comando:

GNU/Linux o MacOS:
```
$ deactivate
```

### Servidor
```
$ python3 -m server.py 127.0.0.2 80881

```


### Cliente
```
$ python3 -m client.py 127.0.0.2 80881

```



## Contribuciones

Si deseas contribuir a este proyecto, ¡estamos abiertos a colaboraciones! Puedes enviar pull requests o informar sobre problemas (issues) que encuentres.

## Licencia

Este proyecto está bajo la Licencia MIT, lo que significa que es de código abierto y puedes utilizarlo, modificarlo y distribuirlo libremente. A continuación, se proporciona un resumen de los términos de la Licencia MIT:




