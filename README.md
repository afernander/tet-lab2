<!--
# tet-lab1
First laboratory in "Tópicos Especiales en Telemática" course. EAFIT 2021-2.
-->

# Laboratorio #1 (Aplicación Distribuida en Sockets TCP/UDP)

## Condiciones del reto 📈

**1.** Defina cualquier tipo de aplicación sencilla distribuida que desee diseñar e implementar (ej. calculadora distribuida, chat, CRUD, etc).
**2.** Utilizar Sockets TCP o UDP en cualquier lenguaje de programación de su preferencia.
**3.** Defina, diseñe e implemente el protocolo de aplicación que requiera para implementar dicha aplicación.
**4.** Realice inicialmente todos los supuestos que requiera respecto a tipo de sistema: C/S o P2P, tipo de arquitectura, y aplique algunos de los conceptos fundamentales de los sistemas distribuidos que se verán en esta Lectura: Introducción a Sistemas Distribuidos.
**5.** Impleméntela en AWS Educate. Con el fin de probar la funcionalidad del sistema, se requiere que al menos instancie 3 máquinas EC2.

## Solución 👨‍🔬

Para este reto decidimos diseñar una **calculadora de tasas de interés** de acuerdo con nuestros conocimientos adquiridos en el curso de *Ingeniería Económica* y que queríamos darle un valor agregado a este laboratorio.

Por facilidad y conocimientos previos de todos los participantes, decidimos usar **Python** como lenguaje general de la práctica aún conociendo la heterogeneidad de los sistemas distribuidos. Con este se verán las implementaciones de las máquinas y los sockets utilizados.

La arquitectura de esta aplicación es **orientada a servicios (SOA)**, donde tenemos un servicio de conversión de tasas de interés manejado por un servidor y otro servicio de generación de tabla de pagos manejado por otro servidor. En este tipo de arquitectura llamamos a esos servicios los *proveedores* y al cliente al que nos conectaremos para usarlos el *consumidor*.

[DIAGRAMA DE ARQUITECTURA EN AWS]

### Explicación de los sockets


### Guía de uso

Para conectarnos al cliente o consumidor de servicios...

### Cómo convertir tasas de interés

**Datos necesarios.** Tipo de tasa inicial y valor, tipo de tasa final y valor.

Los tipos válidos de momento son:
- Tasa efectiva mensual o mes vencido (E.M)
- Tasa efectiva anual (E.A)
- Tasa nominal mes vencido (N.M.V)
- Tasa nominal año vencido (N.A.V)

### Cómo generar tabla de pagos

**Datos necesarios.** Capital inicial, tasa de interés efectiva mensual (E.M), cantidad de cuotas.

## Participantes

- David Calle González <a href="https://github.com/dcalleg707"><img src="https://image.flaticon.com/icons/png/512/25/25231.png" width=20></a>
- Juan Sebastián Díaz Osorio <a href="https://github.com/juansedo"><img src="https://image.flaticon.com/icons/png/512/25/25231.png" width=20></a>
- Santiago Hidalgo Ocampo <a href="https://github.com/sanhidalgoo"><img src="https://image.flaticon.com/icons/png/512/25/25231.png" width=20></a>