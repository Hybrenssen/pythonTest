from flask import Flask
from redis import Redis, RedisError
import os
import socket

redis=Redis(host="192.168.1.47", port=6379, password='Huawei2020', db=0, socket_connect_timeout=2, socket_timeout=2)
app = Flask(__name__)
@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError as e:
        print(str(e))
        visits = "cannot connect to Redis, counter disabled"
    html = 	"<body style=\"background-color: #17C9FF; text-align: center;\">"\
			"<h1><span style=\"color: #0F1BBD;\"><strong>Bienvenido al CoE Data de Pacifico!</strong></span></h1>"\
			"<p><img src=\"https://www.t-aseguro.com/cotizadorweb/images/imagenes/pacifico-seguros-logo.png\" alt=\"Pacfico\" width=\"582\" height=\"291\" /></p>"\
			"<h2><strong>Despu&eacute;s de este taller estas listo para experimentar y comenzar a crear valor usando los datos.</strong></h2>"\
			"<p>&nbsp;</p>"\
			"<h1 style=\"color: #CE4257;\">HELLO WORLD, from application APP-DEMO in {envName} environment!</h1>"\
            "<h2 style=\"color: #4F000B;\">Hostname: [{hostname}]</h2>"\
            "<p>&nbsp;</p>"\
            "<p style=\"color: #720026;\"\><strong>VISITS: </strong><span style=\"background-color: #720026; color: #fff; display: inline-block; padding: 3px 10px; font-weight: bold; border-radius: 5px;\">{visits}</span>&nbsp;</p>"\
	    "<p>&nbsp;</p>"\
	    "<h2><span style=\"color: #993300;\"><strong>Unete a la comunidad Pacifico (click en la imagen)</strong></span></h2>"\
	    "<p><a title=\"Pacifico Workplace;\" href=\"https://pacifico.workplace.com/\"><img src=\"https://www.skalamkt.com/wp-content/uploads/2020/06/facebook-workplace-que-es.jpg\" alt=\"Huawei Cloud Peru Community\" width=\"600\" height=\"338\" /></a></p>"\
			"</body>"
    return html.format(envName=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)
	
if __name__ =="__main__":
    app.run(host='0.0.0.0',port=80)	
