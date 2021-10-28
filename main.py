#   Para acceder a la API, se necesita hacer esto primero:
#   https://stackoverflow.com/questions/54135206/requests-caused-by-sslerrorcant-connect-to-https-url-because-the-ssl-module

import meraki
import os           #   Para acceder a la variable de entorno

#   Accede a la API de Meraki
dashboard = meraki.DashboardAPI(os.getenv('MERAKI_DASHBOARD_API_KEY'))

#   Datos del profe
organization_id = '578350'
network_id = 'L_770115536280355073'

#   Regresa una lista de diccionarios sobre las redes en una organización
networks = dashboard.organizations.getOrganizationNetworks(
    organization_id, total_pages = 'all'
)
print(networks)
print()

#   Regresa un diccionario sobre una red
response = dashboard.networks.getNetwork(network_id)
print(response)
print()


#   Regresa un diccionario sobre un dispositivo en una red
serial = 'Q2BV-25WV-M9DA'
responseDevice = dashboard.devices.getDevice(serial)
print(responseDevice)
print()

#   Acceder a elemento de diccionario
print(responseDevice['lat'])
print()

#   Acceder a elemento de una lista de diccionarios
print(networks[0]['organizationId'])