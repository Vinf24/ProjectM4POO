""" ERRORES PERSONALIZADOS client_exceptions.py """

class ClientError(Exception):
    """ BASE DE ERROR PERSONALIZADO """

class ClientTypeError(ClientError):
    """ ERROR TIPO CLIENTE """

class InvalidAgeError(ClientError):
    """ ERROR EDAD INVALIDA """

class InvalidEmailError(ClientError):
    """ ERROR EMAIL INVALIDO """
