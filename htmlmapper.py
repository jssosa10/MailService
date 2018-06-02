import codecs
import configparser, json
from Exceptions import *
class HtmlMapper():
    def __init__(self):
        self.config = configparser.ConfigParser()
    """
        Funión encargada de mapear un html si no esta todos los valores requeridos lanza excepción
    """
    def map(self,template,values):
        f=codecs.open(template+'.html', 'r')
        self.config.read(template+'cfg.cfg')
        message = str(f.read())
        required=self.config.get('Values', 'Required').split(',')  
        optional=self.config.get('Values', 'Optional').split(',')
        for x in values.keys():
            message = message.replace(x,values[x])
        #print(message)
        #print(required[0])
        for x in required:
            if x in message:
                #print(required[x],message)
                raise IncompleteValuesException('Faltan valores requeridos')
        for x in optional:
            message = message.replace(x,'')
        #print(message)
        return message
#hm = HtmlMapper()
#print(hm.map('test',{'Name':'Juan','cc':'1000'}))
