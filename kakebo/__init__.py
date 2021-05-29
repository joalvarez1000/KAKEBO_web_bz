#para que pueda ser importado por cualquier otro usuario

from flask import Flask

app = Flask (__name__, instance_relative_config= True) #Con esto creamos la aplicacion 
app.config.from_object('config') #instanciamos el secret_key de config.py

from kakebo import views #instanciamos las rutas de views