## About the connector
TCPWave offers automated DDI (DNS, DHCP, IPAM) workflow management, providing significant benefits to large-scale organizations. It reduces manual tasks, enhances IT productivity, and enables a focus on strategic initiatives that drive business growth. By standardizing network management processes, TCPWave enforces best practices and facilitates rapid, scalable service delivery.
<p>This document provides information about the TCP Wave Connector, which facilitates automated interactions, with a TCP Wave server using FortiSOAR&trade; playbooks. Add the TCP Wave Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with TCP Wave.</p>

### Version information

Connector Version: 1.0.0


Authored By: SpryIQ.Co

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-tcp-wave`

## Prerequisites to configuring the connector
- You must have the URL of TCP Wave server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the TCP Wave server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>TCP Wave</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Specify the URL or IP address of the TCPWave server to which you will connect and perform automated operations.<br>
<tr><td>TIMS Session Token<br></td><td>Specify the TIMS Session Token to access the endpoint where you will perform the automated operations.<br>
<tr><td>Protocol<br></td><td>Specify the protocol to access the endpoint where you will perform the automated operations.<br>
<tr><td>Port<br></td><td>Specify the port to access the endpoint where you will perform the automated operations. The default is set to 7443.<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get Object Details By IP Address<br></td><td>Provides the details of Object defined in the TCPWave IPAM based on the IP Address of the object.<br></td><td>get_object_details_by_ipaddress <br/>Investigation<br></td></tr>
<tr><td>Check Object Exists<br></td><td>Checks if the object exists in the TCPWave IPAM with the specified address.<br></td><td>check_object_exists <br/>Investigation<br></td></tr>
<tr><td>Get Network Details by IP Address<br></td><td>Provides the details of a Network defined in the TCPWave IPAM based on the IP Address of the Network.<br></td><td>get_network_details_by_ipaddress <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Get Object Details By IP Address
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>IP Address<br></td><td>Specify the IP address of the object to retrieve its details from TCPWave IPAM.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "rrs": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "rrsXML": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "address": "10.236.111.213",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "addedRRs": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "class_code": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "deletedRRs": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "update_ns_a": false,
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "addressArray": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "routersArray": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "update_ns_ptr": false,
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "update_ns_flag": false,
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "organization_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "denyClassesArray": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "dyn_update_rrs_a": false,
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "allowClassesArray": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "dyn_update_rrs_mx": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "organization_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "dyn_update_rrs_ptr": false,
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "isDeleterrsChecked": 0,
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "dyn_update_rrs_cname": false
</code><code><br>}</code>

### operation: Check Object Exists
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>IP Address<br></td><td>Specify the IP address of the object to retrieve its details from TCPWave IPAM.<br>
</td></tr><tr><td>Organization Name<br></td><td>Specify the name of the organization associated with the network in TCPWave IPAM.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "data": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "status": ""
</code><code><br>}</code>

### operation: Get Network Details by IP Address
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>IP Address<br></td><td>Specify the IP address of the network to retrieve its details from TCPWave IPAM.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "addr1": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "addr2": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "addr3": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "addr4": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "address": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "has_subnets": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "mask_length": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "end_addr_val": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "object_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "percent_full": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "server_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "subnet_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "templateList": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "customTemplate": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "nw_mask_length": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "percentageFull": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "start_addr_val": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "autoCreateBlock": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "organization_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "organization_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "reverse_zone_serial": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "selectedSlaveServer": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "selectedMasterServer": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "networkSlaveServerXML": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "networkMasterServerXML": ""
</code><code><br>}</code>
## Included playbooks
The `Sample - tcp-wave - 1.0.0` playbook collection comes bundled with the TCP Wave connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the TCP Wave connector.

- Check Object Exists
- Get Network Details by IP Address
- Get Object Details By IP Address

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
