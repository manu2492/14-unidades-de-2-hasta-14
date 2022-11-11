--exercise 1
SELECT Nombre FROM dbo.Proveedor
WHERE Ciudad LIKE '%Ramos%';

--exercise 2
--Listar los códigos de los materiales que provea el proveedor 4
--y no los provea el proveedor 5. Se debe resolver de 3 formas.
SELECT CodMat from Provisto_Por
WHERE CodProv = 4 and 
CodMat not in (SELECT CodMat FROM Provisto_Por WHERE CodProv = 5);

--EXERCISE 3
--Listar los materiales, código y descripción, provistos por
--proveedores de la ciudad de Ramos Mejía.
--Material, Proveedor, Provisto_Por
SELECT Material.CodMat, Descripcion
from Material 
JOIN Provisto_Por ON (Material.CodMat=Provisto_Por.CodMat)
JOIN Proveedor ON (Provisto_Por.CodProv=Proveedor.CodProv)
WHERE Ciudad = 'Ramos Mejia';

--exercise 4
--Listar los proveedores y materiales que provee. La lista
--resultante debe incluir a aquellos proveedores que no proveen
--ningún material.
SELECT Proveedor.CodProv, Nombre, CodMat FROM Proveedor
FULL OUTER JOIN Provisto_Por ON Proveedor.CodProv = Provisto_Por.CodProv
ORDER BY Proveedor.CodProv;

--exercise 5
--Listar los artículos que cuesten más de $30 o que estén
--compuestos por el material 2.
SELECT DISTINCT Articulo.CodArt, Descripcion, Precio FROM Articulo
JOIN Compuesto_Por ON Articulo.CodArt= Compuesto_Por.CodArt
WHERE Precio > 30 OR CodMat = 2;
--select * from Compuesto_Por;

--exercise 6
--Listar los artículos de Mayor precio.
SELECT CodArt, Descripcion FROM Articulo
WHERE Precio IN (SELECT MAX(Precio) FROM Articulo);

SELECT * FROM Articulo
ORDER BY Precio;

--exercise 7
--Listar los proveedores que proveen más de 3 materiales
SELECT CodProv, COUNT(*) as count
FROM Provisto_Por GROUP BY CodProv
HAVING COUNT(*) > 3;

--SELECT CodProv, COUNT(*)
--FROM Provisto_Por GROUP BY CodProv;

--select * from Provisto_Por
--where CodProv = 6

--exercise 8
--Listar los proveedores que proveen más de 4 materiales y crear una view
CREATE VIEW Providers2 AS 
SELECT CodProv, COUNT(*) as count
FROM Provisto_Por GROUP BY CodProv
HAVING COUNT(*) > 4

-- la forma de listar la view es
SELECT * FROM Providers2;



