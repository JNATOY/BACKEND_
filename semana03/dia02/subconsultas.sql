-- mostrar todos los alumnos de peru cuya nota sea mayor
-- al promedio de notas de todo el pais
select avg(nota) from tbl_alumno where pais ='Peru';
select *from tbl_alumno
where pais = 'Peru'
and nota > (select avg(nota) from tbl_alumno where pais ='Peru');