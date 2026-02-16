""" ERRORES PERSONALIZADOS client_exceptions.py """

class ClientError(Exception):
    """ BASE DE ERROR PERSONALIZADO """

class ClientTypeError(ClientError):
    """ ERROR TIPO CLIENTE """

class InvalidAgeError(ClientError):
    """ ERROR EDAD INVALIDA """

class InvalidEmailError(ClientError):
    """ ERROR EMAIL INVALIDO """

class InvalidPhoneError(ClientError):
    """ ERROR TELEFONO INVALIDO """

class InvalidNameError(ClientError):
    """ ERROR NOMBRE INVALIDO """

class InvalidCompanyError(ClientError):
    """ ERROR EMPRESA INVALIDA """

class InvalidAddressError(ClientError):
    """ ERROR DIRECCION INVALIDA """

class InvalidAmountError(ClientError):
    """ ERROR MONTO INVALIDO """

class RepositoryError(Exception):
    """ ERROR BASE DE PERSISTENCIA """

class DatabaseConnectionError(RepositoryError):
    """ NO SE PUDO CONECTAR A LA BASE DE DATOS """

class DatabaseSchemaError(RepositoryError):
    """ ERROR CREANDO TABLAS O ESTRUCTURA """

class DatabaseWriteError(RepositoryError):
    """ ERROR AL GUARDAR DATOS """

class DatabaseReadError(RepositoryError):
    """ ERROR AL LEER DATOS """

class DatabaseDeleteError(RepositoryError):
    """ ERROR AL ELIMINAR DATOS """
