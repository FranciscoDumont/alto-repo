from random import randint

mensajes = [
"jajaja es verdad",
"yo tambien te quiero <3",
"diculpame flacx podes hablar en un lenguajx mas inclusivx",
"mira vos che",
"JAJAJAJA"
]

class MensajeRandom(object):

    @staticmethod
    def fraseRandom():
        return mensajes[randint(0, len(mensajes)-1)]
