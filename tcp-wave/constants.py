"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

class Url:
    """
        Defines API endpoint URLs for the TCPWave service.

        Attributes:
            API (str): The base API path.
            LOGCAT_LIST (str): Endpoint for retrieving the logcat list.
            NETWORK_DETAILS_IP_ADDRESS (str): Endpoint for retrieving network details by IP address.
            OBJECT_DETAILS_IP_ADDRESS (str): Endpoint for retrieving object details by IP address.
            CHECK_OBJECT_EXISTS (str): Endpoint for checking if an object exists by IP address and organization name.
    """
    API = "/tims/rest"
    LOGCAT_LIST = API + '/logcat/list'
    NETWORK_DETAILS_IP_ADDRESS = API + '/home/getNetworkDetails/{ip_address}'
    OBJECT_DETAILS_IP_ADDRESS = API + '/home/getObjectDetails?ipAddress={ip_address}'
    CHECK_OBJECT_EXISTS = API + '/object/checkObjectExists?address={ip_address}&organization_name={organization_name}'


class Method:
    """
       Defines HTTP methods for making API requests.

       Attributes:
           GET (str): HTTP method for GET requests.
           POST (str): HTTP method for POST requests.
    """
    GET = 'GET'
    POST = 'POST'