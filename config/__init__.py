import os
from decouple import config

fqdn = config("DYNDNS_FQDN")
hostedzone = config("DYNDNS_HOSTED_ZONE")
