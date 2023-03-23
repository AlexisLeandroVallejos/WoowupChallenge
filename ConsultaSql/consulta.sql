/* 
Ejercicio SQL
Escribir una consulta SQL que traiga todos los clientes que han comprado en total más de 100,000$ en los últimos 12 meses usando las siguientes tablas: 

Clientes: ID, Nombre, Apellido

Ventas: Fecha, Sucursal, Numero_factura, Importe, Id_cliente 
*/

SELECT C.ID, C.NOMBRE, C.APELLIDO
FROM CLIENTES AS C, VENTAS AS V
WHERE C.ID = V.ID_CLIENTE AND SUM(V.IMPORTE) > 100000 AND V.FECHA BETWEEN DATE_SUB(CUR_DATE(), INTERVAL 1 YEAR)