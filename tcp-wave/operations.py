"""
Copyright (C) 2024 Fortinet Inc.
All rights reserved.
FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
"""

import requests
from connectors.core.connector import get_logger, ConnectorError
import json
from .constants import Url, Method
logger = get_logger('tcp-wave')


class TCPWave(object):
    def __init__(self, config):
        """
            Initialize the TCPWave instance with configuration settings.

            Parameters:
                config (dict): Configuration dictionary containing the following keys:
                    - 'host' (str): The hostname or IP address of the TCPWave server.
                    - 'port' (int): The port number to connect to the TCPWave server.
                    - 'tims_session_token' (str): The API session token for authentication.
                    - 'protocol' (str): The protocol to use (e.g., 'http' or 'https').

            Sets:
                self.base_url (str): The base URL for connecting to the TCPWave server.
                self.headers (dict): The headers to include in HTTP requests, including the session token for authentication.
        """
        try:
            self.get_config_data(config)
            if self.host.startswith('http://') or self.host.startswith('https://'):
                self.base_url = '{host}:{port}'.format(
                    host=self.host.rstrip('/'),
                    port=self.port
                )
            else:
                self.base_url = '{protocol}://{host}:{port}'.format(
                    protocol=self.protocol,
                    host=self.host.rstrip('/'),
                    port=self.port
                )
            self.headers = {
                'TIMS-Session-Token': self.api_key
            }
            logger.info("base_url: {0}".format(self.base_url))
        except Exception as err:
            logger.exception('Initialization failed: %s', err)
            raise ConnectorError(f"Initialization failed: {str(err)}")

    def get_config_data(self, config):
        """
            Initialize configuration settings for the TCPWave instance from the provided config dictionary.

            Parameters:
                config (dict): Configuration dictionary containing the following keys:
                    - 'host' (str): The hostname or IP address of the TCPWave server.
                    - 'port' (int): The port number to connect to the TCPWave server.
                    - 'tims_session_token' (str): The API session token for authentication.
                    - 'protocol' (str): The protocol to use (e.g., 'http' or 'https').
                    - 'verify_ssl' (bool, optional): Whether to verify SSL certificates (default is False).

            Sets:
                self.host (str): The hostname or IP address of the TCPWave server.
                self.port (int): The port number to connect to the TCPWave server.
                self.api_key (str): The API session token for authentication.
                self.protocol (str): The protocol to use.
                self.verify_ssl (bool): Whether to verify SSL certificates.
        """
        try:
            self.host = config.get('host')
            self.port = config.get('port')
            self.api_key = config.get('tims_session_token')
            self.protocol = config.get('protocol')
            self.verify_ssl = config.get('verify_ssl', False)
        except ValueError as ve:
            logger.error(f"Configuration error: {ve}")
            raise ConnectorError(f"Configuration error: {str(ve)}")
        except Exception as err:
            logger.exception(f"Failed to initialize configuration: {err}")
            raise ConnectorError(f"Failed to initialize configuration: {str(err)}")

    def make_rest_call(self, endpoint=None, method='GET', headers=None, health_check=False, data=None):
        """
            Makes an HTTP request to the specified endpoint and returns the response.

            Parameters:
                endpoint (str): The API endpoint to which the request will be made.
                method (str): The HTTP method to use for the request (e.g., 'GET', 'POST'). Defaults to 'GET'.
                headers (dict, optional): Additional headers to include in the request. Defaults to None.
                health_check (bool, optional): If True, performs a health check and returns the raw response. Defaults to False.
                data (dict, optional): The data to send with the request (used with methods like 'POST'). Defaults to None.

            Returns:
                dict: A dictionary with the status and data of the response. The status is 'Success' or 'Failure'.
                      The data contains the response details, which may include:
                            - For a successful response: {'status': 'Success', 'data': response_data}
                            - For a failure or non-200 status code response: {'status': 'Failure',
                                                                          'status_code': str(response.status_code),
                                                                          'response': response.content}

            Raises:
                ConnectorError: If an error occurs during the request or response handling.

            Notes:
                - If `health_check` is True, the raw response is returned, and the response is not converted to JSON format.
                - If the response cannot be converted to JSON, the raw content is returned with a failure status.
                - If the request fails with a non-200 status code, an error is logged, and a `ConnectorError` is raised with details.
        """
        url = self.base_url + endpoint
        logger.debug('Final URL to make REST call is: {0}'.format(url))

        if headers:
            self.headers.update(headers)

        try:
            logger.debug('Making a request with {0} method and {1} headers.'.format(method, headers))
            response = requests.request(method, url, headers=self.headers, data=data, verify=self.verify_ssl)

            # Handle the response if it's successful
            if response.status_code in [200]:
                if health_check:
                    return response

                content_type = response.headers.get('Content-Type', '')

                # Handle JSON response
                if 'application/json' in content_type:
                    response_data = response.json()
                    logger.debug(
                        'Converting the response into JSON format after returning with status code: {0}'.format(
                            response.status_code))
                    return {'status': response_data['status'] if 'status' in response_data else 'Success',
                            'data': response_data}
                # Handle plain text response
                elif 'text/plain' in content_type:
                    logger.debug('Plain text response received.')
                    return {'status': 'Success', 'data': response.text}

                # Handle other content types
                else:
                    logger.error('Unknown content type: {0}. Returning raw content.'.format(content_type))
                    return {'status': 'Failure', 'data': response.content}

            else:
                logger.error('Failed with response {0}'.format(response))
                return {
                    'status': 'Failure',
                    'status_code': str(response.status_code),
                    'response': response.text
                }

        except Exception as e:
            logger.exception(str(e))
            raise ConnectorError(str(e))


def _check_health(config):
    """
       Perform a health check on the TCPWave instance to ensure it is operational.

       Parameters:
           config (dict): Configuration settings required for the TCPWave instance.

       Returns:
           bool: True if the health check passes, indicating that the TCPWave instance is operational.

       Raises:
           ConnectorError: If the health check fails or an error occurs during the API call.
       """
    try:
        obj = TCPWave(config)
        return obj.make_rest_call(endpoint=Url.LOGCAT_LIST, method=Method.GET, health_check=True)

    except Exception as err:
        logger.exception('Health check failed: {0}'.format(err))
        raise ConnectorError(str(err))


def get_object_details_by_ipaddress(config, params):
    """
    Retrieve details of an object based on its IP address.

    Parameters:
        config (dict): Configuration settings required for the TCPWave instance.
        params (dict): Dictionary containing parameters for the API call. Must include:
            - 'ip_address' (str): The IP address of the object for which details are to be retrieved.

    Returns:
        dict: The response from the API call, typically in JSON format, containing the details of the TIMS object array.

    Raises:
        ConnectorError: If an error occurs during the API call.
    """
    try:
        obj = TCPWave(config)
        endpoint = Url.OBJECT_DETAILS_IP_ADDRESS.format(ip_address=params.get('ip_address'))
        logger.debug('Requesting object details from endpoint: {0}'.format(endpoint))
        return obj.make_rest_call(endpoint=endpoint, method=Method.GET)
    except Exception as err:
        raise ConnectorError(str(err))


def check_object_exists(config, params):
    """
        Check if an object exists based on its IP address and organization name.

        Parameters:
            config (dict): Configuration settings required for the TCPWave instance.
            params (dict): Dictionary containing parameters for the API call. Must include:
                - 'ip_address' (str): The IP address of the object to check.
                - 'organization_name' (str): The name of the organization associated with the object.

        Returns:
            str: The response from the API call, typically in JSON format, indicating whether the object exists.

        Raises:
            ConnectorError: If an error occurs during the API call.
        """
    try:
        obj = TCPWave(config)
        endpoint = Url.CHECK_OBJECT_EXISTS.format(ip_address=params.get('ip_address'), organization_name=params.get('organization_name'))
        logger.debug('Requesting object existence check from endpoint: {0}'.format(endpoint))
        return obj.make_rest_call(endpoint=endpoint, method=Method.GET)
    except Exception as err:
        raise ConnectorError(str(err))


def get_network_details_by_ipaddress(config, params):
    """
        Retrieve network details based on the IP address.

        Parameters:
            config (dict): Configuration settings required for the TCPWave instance.
            params (dict): Dictionary containing parameters for the API call. Must include:
                - 'ip_address' (str): The IP address of the network for which details are to be retrieved.

        Returns:
            object: The response from the API call, typically in JSON format, containing the details of the network information array.

        Raises:
            ConnectorError: If an error occurs during the API call.
        """
    try:
        obj = TCPWave(config)
        endpoint = Url.NETWORK_DETAILS_IP_ADDRESS.format(ip_address=params.get('ip_address'))
        logger.debug('Requesting network details from endpoint: {0}'.format(endpoint))
        return obj.make_rest_call(endpoint=endpoint, method=Method.GET)
    except Exception as err:
        logger.exception('TIMS-2024: This subnet does not correspond to any of the existing networks.')
        raise ConnectorError(str(err))


operations = {
    'get_object_details_by_ipaddress': get_object_details_by_ipaddress,
    'check_object_exists': check_object_exists,
    'get_network_details_by_ipaddress': get_network_details_by_ipaddress
}
