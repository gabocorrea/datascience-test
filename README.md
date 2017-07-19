# Caso Machine Learning

Cornershop trabaja actualmente en 6 ciudades completando miles de órdenes por día. Un elemento fundamental para determinar cuántas órdenes podemos aceptar, cuando debemos comenzar a trabajar en una orden y que horario le podemos prometer a los clientes es la **estimación de tiempo**.

En este caso te pedimos que entrenes el mejor estimador posible utilizando técnicas de Machine Learning y los datos disponibles en la carpeta *data* (cada tabla en un archivo formato csv). Puedes utilizar el lenguaje y librería que más te acomode. *Nosotros trabajamos con Python, Scikit Learn y Keras, pero si prefieres trabajar en R u otra librería, no tenemos problemas*.

A continuación el detalle de la información que te facilitaremos:

***Tabla Orders***:
- order_id: Identificador de la orden.
- lat y lng: Latitud y Longitud de la dirección de entrega.
- dow: Día de la semana en que se prometió la orden. 0: Domingo 6: Sabado.
- promised_time: Hora de entrega prometida al cliente.
- actual_time: Hora en que se entregó el pedido al cliente.
- on_demand: Si el pedido fue solicitado en “Menos de 90 minutos” o en una ventana horario en el futuro.
- picker_id: Identificador del shopper que hizo de picker en el pedido.
- driver_id: Identificador del shopper que hizo de driver en el pedido.
- store_branch_id: Identificador del local en que se realizó la compra.
- total_minutes: Tiempo total que demoró completar la orden (desde la compra hasta la entrega).

***Tabla Order_Product***:
- order_id: Identificador de la orden.
- product_id: Identificador del producto.
- quantity: Cantidad solicitada del producto por el cliente.
- quantity_found: Cantidad encontrada del producto por el shopper.
- buy_unit: Formato en que se vendió el producto (Unidades o KG).

***Tabla Shoppers***:
- shopper_id: Identificador del Shopper.
- seniority: Clasificación de experiencia del Shopper.
- found_rate: Porcentaje histórico de productos que el shopper encontró.
- picking_speed: Velocidad histórica de recogida de productos.
- accepted_rate: Porcentaje histórico de pedidos aceptado por el shopper.
- rating: Evaluación histórica del shopper.

***Tabla Storebranch***:
- store_branch_id: Identificador del local.
- store: Identificador de la tienda a la cual pertenece el local.
- lat y lng: Latitud y Longitud de la ubicación del local.

Todos los IDs y nombres han sido encriptados para mantener la anonimidad. Además, esto corresponde a un pequeño sampling de la operación de Cornershop.

El objetivo de este caso es que realices una estimación de cuánto tiempo tomará completar los pedidos que tienen el campo **total_minutes** vacío. También te solicitaremos el script con el que entrenaste el modelo y un pequeño informe (**en 1 plana**) explicando cómo enfrentaste este problema en términos de:

- Generación de tu dataset.
- Transformaciones que hayas realizados a los datos.
- En qué entorno entrenaste los modelos.
- Que modelos utilizaste y con qué métricas evaluar el desempeño de tu modelo.

Puedes escribir un correo a matias.sanchez@cornershopapp.com para cualquier consulta adicional.
