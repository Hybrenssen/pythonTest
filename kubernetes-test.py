from flask import Flask
from redis import Redis, RedisError
import os
import socket

redis=Redis(host="192.168.1.5", port=6379, password='Huawei2020', db=0, socket_connect_timeout=2, socket_timeout=2)
app = Flask(__name__)
@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError as e:
        print(str(e))
        visits = "cannot connect to Redis, counter disabled"
    html = 	"<body style=\"background-color: #ceeff3bd;\">"\
			"<h1><span style=\"color: #993300;\"><strong>Bienvenido a Huawei Cloud!</strong></span></h1>"\
			"<p><img src=\"https://ricardo-rojas-web.obs.myhuaweicloud.com/imgs/huawei-cloud.jfif\" alt=\"Huawei Cloud\" width=\"582\" height=\"291\" /></p>"\
			"<h2><strong>Despu&eacute;s de este taller estas listo para experimentar y comenzar a crear valor usando la nube p&uacute;blica de Huawei.</strong></h2>"\
			"<p>&nbsp;</p>"\
			"<h1 style=\"color: #5e9ca0;\">HELLO {name}!</h1>"\
            "<h2 style=\"color: #2e6c80;\">Hostname: {hostname}</h2>"\
            "<p>&nbsp;</p>"\
            "<p>VISITS: <span style=\"background-color: #2b2301; color: #fff; display: inline-block; padding: 3px 10px; font-weight: bold; border-radius: 5px;\">{visits}</span>&nbsp;</p>"\
			"</body>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)
	
if __name__ =="__main__":
    app.run(host='0.0.0.0',port=80)	