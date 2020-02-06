# Cisco-AMP4EP-PoC
Cisco AMP for Endpoint sample code

## POC code to setup AMQP listener for AMP4EP

Sample code to set up a AMQP listener for Cisco AMP for Endpoint event
Stream.

This requires to set up an EventStream

Refer to Cisco
[Security AMP 01 Basics](https://github.com/CiscoSecurity/amp-01-basics)
for examples on how to interact with Cisco AMP for Endpoint API.

## References
Create EventStream:
[amp-04-create-event-stream](https://github.com/CiscoSecurity/amp-04-create-event-stream)

Delete EventStream
[amp-04-delete-event-stream](https://github.com/CiscoSecurity/amp-04-delete-event-stream)

Cisco [API-Docs](https://api-docs.amp.cisco.com)



# Example output
`````
[*] Waiting for messages. To exit press CTRL+C

[x] Received b'{"id":xxx097yyy19730xxxxx,"timestamp":1580974451"timestamp_nanoseconds":973027000,"date":"2020-02-06T07:34:11+00:00""event_type":"Threat Detected","event_type_id":1090519054"detection":"Win.Ransomware.Eicar::95.sbx.tg""detection_id":"13257897837238329""connector_guid":"f7addabd-yyy-xxx-zzz-d89a311e59d0","group_guids"["254e2ae0-xxx-yyyy-92bb-36e0c2da41b1"],"severity":"Medium","computer{"connector_guid":"f7addabd-xxxx-yyyyy-zzz-d89a311e59d0""hostname":"Computer","external_ip":"xx.yy.zz.67","user":"u""active":true"network_addresses":[{"ip":"192.168.1.131""mac":"xx:xx:xx:xx:xx:be"}{"ip":"","mac":"xx:xx:xx:xx:xx:01"},{"ip":"""mac":"xx:xx:xx:xx:11:22"}],"links":{"computer":"https:/api.eu.amp.cisco.com/v1/computers/f7addabd-yyyy-4968-xxxx-d89a311e59d0""trajectory":"https://api.eu.amp.cisco.com/v1/computersf7addabd-yyyy-4968-xxxx-d89a311e59d0/trajectory","group":"https:/api.eu.amp.cisco.com/v1/groups/254e2ae0-yyyy-xxxx-zzzz-36e0c2da41b1"}}"file":{"disposition":"Blacklisted","file_name":"eicar_com.zip""file_path":"/Users/MacUser/Downloads/eicar_com.zip","identity"{"sha256":"2546DCFFC5AD854D4DDC64FBF056871CD5A00F2471CB7A5BFD4AC23B6E9EEDA"},"archived_file":{"disposition":"Malicious","identity"{"sha256":"275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0"}},"parent":{"process_id":577,"disposition":"Unknown""file_name":"Safari","identity"{"sha256":"08DA6F595A2B79988CA9ACABE40ABB9F8EA12F4A26627D379077A97A2129D5A"}}}}'


`````

