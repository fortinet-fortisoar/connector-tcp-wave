## About the connector
TCPWave offers automated DDI (DNS, DHCP, IPAM) workflow management, providing significant benefits to large-scale organizations. It reduces manual tasks, enhances IT productivity, and enables a focus on strategic initiatives that drive business growth. By standardizing network management processes, TCPWave enforces best practices and facilitates rapid, scalable service delivery.
<p>This document provides information about the TCP Wave Connector, which facilitates automated interactions, with a TCP Wave server using FortiSOAR&trade; playbooks. Add the TCP Wave Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with TCP Wave.</p>

### Version information

Connector Version: 1.0.0


Authored By: SpryIQ.Co

Certified: No

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-tcp-wave</pre>

## Prerequisites to configuring the connector
- You must have the credentials of TCP Wave server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the TCP Wave server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>TCP Wave</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the URL or IP address of the TCPWave server to which you will connect and perform automated operations.
</td>
</tr><tr><td>TIMS Session Token</td><td>Specify the TIMS Session Token to access the endpoint where you will perform the automated operations.
</td>
</tr><tr><td>Protocol</td><td>Specify the protocol to access the endpoint where you will perform the automated operations.
</td>
</tr><tr><td>Port</td><td>Specify the port to access the endpoint where you will perform the automated operations. The default is set to 7443.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Object Details By IP Address</td><td>Provides the details of Object defined in the TCPWave IPAM based on the IP Address of the object.</td><td>get_object_details_by_ipaddress <br/>Investigation</td></tr>
<tr><td>Check Object Exists</td><td>Checks if the object exists in the TCPWave IPAM with the specified address.</td><td>check_object_exists <br/>Investigation</td></tr>
<tr><td>Get Network Details by IP Address</td><td>Provides the details of a Network defined in the TCPWave IPAM based on the IP Address of the Network.</td><td>get_network_details_by_ipaddress <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Object Details By IP Address
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>IP Address</td><td>Specify the IP address of the object to retrieve its details from TCPWave IPAM.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "rrs": [],
    "name": "",
    "rrsXML": "",
    "address": "10.236.111.213",
    "addedRRs": [],
    "class_code": "",
    "deletedRRs": [],
    "update_ns_a": false,
    "addressArray": [],
    "routersArray": [],
    "update_ns_ptr": false,
    "update_ns_flag": false,
    "organization_id": "",
    "denyClassesArray": [],
    "dyn_update_rrs_a": false,
    "allowClassesArray": [],
    "dyn_update_rrs_mx": "",
    "organization_name": "",
    "dyn_update_rrs_ptr": false,
    "isDeleterrsChecked": 0,
    "dyn_update_rrs_cname": false
}</pre>

### operation: Check Object Exists
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>IP Address</td><td>Specify the IP address of the object to retrieve its details from TCPWave IPAM.
</td></tr><tr><td>Organization Name</td><td>Specify the name of the organization associated with the network in TCPWave IPAM.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": "",
    "status": ""
}</pre>

### operation: Get Network Details by IP Address
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>IP Address</td><td>Specify the IP address of the network to retrieve its details from TCPWave IPAM.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "name": "",
    "addr1": "",
    "addr2": "",
    "addr3": "",
    "addr4": "",
    "address": "",
    "has_subnets": "",
    "mask_length": "",
    "end_addr_val": "",
    "object_count": "",
    "percent_full": "",
    "server_count": "",
    "subnet_count": "",
    "templateList": [],
    "customTemplate": "",
    "nw_mask_length": "",
    "percentageFull": "",
    "start_addr_val": "",
    "autoCreateBlock": "",
    "organization_id": "",
    "organization_name": "",
    "reverse_zone_serial": "",
    "selectedSlaveServer": [],
    "selectedMasterServer": [],
    "networkSlaveServerXML": "",
    "networkMasterServerXML": ""
}</pre>
## Included playbooks
The `Sample - TCP Wave - 1.0.0` playbook collection comes bundled with the TCP Wave connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the TCP Wave connector.

- Check Object Exists
- Get Network Details by IP Address
- Get Object Details By IP Address

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
