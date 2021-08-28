<!--
# tet-lab1
First laboratory in "Tópicos Especiales en Telemática" course. EAFIT 2021-2.
-->

# Laboratorio #2 (Aplicación Distribuida en HTTP)

## Condiciones del reto 📈

**1.** Reutilice la misma aplicación desarrollada en el Lab1y rediséñela e impleméntela utilizando el protocolo de aplicación HTTP(ej: calculadora distribuida, chat, crud, etc)

**2.** Utilizar una librería HTTP encualquier lenguaje de programación de su preferencia (recomendado Python)

**3.** Defina, diseñe e implemente el mecanismo de comunicación (mensajes y codificación) que requiera para implementar dicha aplicació

**4.** Realice inicialmente todos los supuestos que requiera respecto a tipo de sistema: C/S o P2P, tipo de arquitectura, y aplique algunos de los conceptos fundamentales de los sistemas distribuidos que se verán en esta Lectura: Introducción a Sistemas Distribuidos

**5.** Impleméntela en AWS Educate, para probar el sistema al menos instancie 3 máquinas EC2

## Solución 👨‍🔬

Para este reto decidimos diseñar una **calculadora de tasas de interés** de acuerdo con nuestros conocimientos adquiridos en el curso de *Ingeniería Económica* y que queríamos darle un valor agregado a este laboratorio.

Por facilidad y conocimientos previos de todos los participantes, decidimos usar **Python** como lenguaje general de la práctica aún conociendo la heterogeneidad de los sistemas distribuidos. Con este se verán las implementaciones de las máquinas y los sockets utilizados.

La arquitectura de esta aplicación es **orientada a servicios (SOA)**, donde tenemos un servicio de conversión de tasas de interés manejado por un servidor y otro servicio de generación de tabla de pagos manejado por otro servidor. En este tipo de arquitectura llamamos a esos servicios los *proveedores* y al cliente al que nos conectaremos para usarlos el *consumidor*.

<!--[DIAGRAMA DE ARQUITECTURA EN AWS]-->


### Guía de uso

Para conectarnos al cliente o consumidor de servicios necesitaremos acceder a la máquina EC2 correspondiente y ejecutar:

```bash
python3 client.py
```

Se podrá ver la siguiente interfaz:

![image](https://user-images.githubusercontent.com/52968530/129671118-07755708-ff60-4019-862f-1f4fbcc26a0e.png)


### Cómo convertir tasas de interés

Se escoge la opción 1 del menú y se empiezan a agregar los datos interactivamente.

![image](https://user-images.githubusercontent.com/52968530/129674277-8c46cf55-792e-4950-a480-efdc4e342990.png)

**Datos necesarios.** Tipo de tasa inicial y valor, tipo de tasa final y valor.

Los tipos válidos de momento son:
- Tasa efectiva mensual o mes vencido (E.M)
- Tasa efectiva anual (E.A)
- Tasa nominal mes vencido (N.M.V)
- Tasa nominal año vencido (N.A.V)

Al final se obtendrá una respuesta y con cualquier tecla podremos regresar al menú principal.

### Cómo generar tabla de pagos

Se escoge la opción 2 del menú y se empiean a agregar los datos interactivamente.

![image](https://user-images.githubusercontent.com/52968530/129674444-a7b22455-0911-42ee-8cfa-51840e407b95.png)

**Datos necesarios.** Capital inicial, tasa de interés efectiva mensual (E.M), cantidad de cuotas.

Al final se obtendrá una respuesta y con cualquier tecla podremos regresar al menú principal.

## Participantes

- David Calle González <a href="https://github.com/dcalleg707"><img src="https://image.flaticon.com/icons/png/512/25/25231.png" width=20></a>
- Juan Sebastián Díaz Osorio <a href="https://github.com/juansedo"><img src="https://image.flaticon.com/icons/png/512/25/25231.png" width=20></a>
- Santiago Hidalgo Ocampo <a href="https://github.com/sanhidalgoo"><img src="https://image.flaticon.com/icons/png/512/25/25231.png" width=20></a>

## Referencias
[1] Python Software Foundation (2021, Aug 16). Socket Programming HOW TO. [Online] Disponible en [este enlace](https://docs.python.org/3/howto/sockets.html).
