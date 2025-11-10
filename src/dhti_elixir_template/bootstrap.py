# Define default variables here
# Can be overridden by the user in the server

from kink import di


def bootstrap():
    di["fhir_access_token"] = "YWRtaW46QWRtaW4xMjM="  # admin:Admin123 in base64
    di["fhir_base_url"] = "http://localhost/openmrs/ws/fhir2/R4"
