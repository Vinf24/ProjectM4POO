Proyecto Módulo 4 Paradigma Orientado a Objetos (POO)

Inicialmente el proyecto utilizaba JSOn para la persistencia 
la base de datos migró a sqlite, por lo tanto file_manager.py
en utils ya no es efectivo, funciones como client_from_dict o
to_dict también son vestigios de ello, aunque aún tienen uso.

El diagrama de clases inicial y final se encuentran en la carpeta UML
la versión inicial no contemplaba el utilizar SQL, ni todas las clases que
terminan participando.