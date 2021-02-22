# KinesisLambdaCloudWatch
Se crea una función de Lambda para consumir eventos de un flujo de Kinesis. 
1.	Creación de la función.
2.	2.	Crear un flujo de Kinesi
Un shard es una unidad de capacidad de rendimiento. Cada shard ingiere hasta 1 Mb/seg y 10000 registros/seg, y emite hasta 2Mb/seg. Para adaptarse a un rendimiento más alto o más bajo, la cantidad de shard se puede modificar después de crear la secuencia de Kinesis utilizando la API.
3.	Adición de un origen de evento en AWS Lambda.
4.	4.	Prueba de la configuración.
Lambda utiliza el rol de ejecución para leer los registros desde el flujo. A continuación, se invoca la función de Lambda y se pasan lotes de registros. La función descodifica los datos de cada registro y los registra, enviando la salida a CloudWatch Logs.
