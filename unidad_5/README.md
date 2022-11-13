# Unidad 5
DAG que realiza una consulta a
una URL y descarga un dataset de medallas olímpicas. Luego
contabiliza el top ten de países con más medallas y guarda los
resultados en un archivo en formato Excel.

Para utilizar este DAG, se deberá poner en la carpeta
DAGs de Airflow.
## Consigna
agregar un logger que realice las siguientes tareas:

1. Indicarnos si la descarga del dataset se y procesamiento se realizó
correctamente
2. Indicarnos si la tarea anterior fue fallida.
3. Mostrar el logging por consola y también guardarlo en un archivo.
