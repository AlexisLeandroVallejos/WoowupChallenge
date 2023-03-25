select 
	c.id, c.nombre, c.apellido
from 
	cliente as c inner join venta as v on c.id = v.id_cliente
where
	date_sub(curdate(), interval 1 year)
group by
	v.id_cliente
having
	sum(v.importe) > 100000;