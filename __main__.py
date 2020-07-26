import urllib3
from jinja2 import Template
import boto3
import json
import socket
import os

import config as conf

def get_ip():
	http = urllib3.PoolManager()
	public_ip = http.request('GET', 'http://icanhazip.com').data.decode('utf-8').replace("\n","")

	if public_ip != socket.gethostbyname(conf.fqdn):
		return public_ip
	else:
		return False

def set_payload(public_ip):
	dir = os.getcwd()+"/"+os.path.dirname(__file__)+"/"
	template = Template(open(dir+'templates/payload.j2').read())
	return json.loads(template.render(fqdn = conf.fqdn, public_ip = public_ip))

def send_changes(hostedzone, public_ip, payload):
	if public_ip:
		client = boto3.client('route53')
		response = client.change_resource_record_sets(HostedZoneId = conf.hostedzone, ChangeBatch = data )

		if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
			return("El cambio se procesó exitosamente [" + response["ChangeInfo"]['Status'] + "]")
		else:
			return("El cambio no se pudo ejecutar")
	else:
		return("La ip pública no requiere modificación")	


def main():
	
	print(send_changes(hostedzone=conf.hostedzone, 
						public_ip=get_ip(), 
						payload=set_payload(get_ip())),
	       flush=True)


if __name__ == '__main__':
	main()