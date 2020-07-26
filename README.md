# DYNDNS

Aplicación en Python 3 que implementa un DNS dinámico, utlizando AWS Route53.

## Instalación

1. Clonar repositorio

   ```bash
   git clone https://github.com/thermosilla/dynamicdns.git
   ```

2. Crear virtualenv

   ```bash
   python3 -m venv dyndnsenv
   source dyndnsenv/bin/activate
   ```

3. Instalar dependencias

   ```bash
   pip install -r dynamicdns/requirements.txt
   ```

4. Configurar variables de entorno

   ```bash
   export DYNDNS_FQDN=fqdn.example.com
   export DYNDNS_HOSTED_ZONE=aws_hosted_zone_id
   ```

5. Ejecutar aplicación

   ```bash
   python dynamicdns
   ```

## Siguentes pasos

Para ejecutar la aplicación periodicamente, se puede agregar al cron o configurar como un servicio systemd

