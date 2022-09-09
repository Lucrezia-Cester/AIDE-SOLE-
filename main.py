import json

#connect to kibana
import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint

username = 'user'
password = 'p'

response = requests.get('http://', auth = HTTPBasicAuth(username, password))

pprint(response.content)

#Query EVENT messages by study uid
#cquery logs real time

HEADERS = {
    'Content-Type': 'application/json'
}

from os import environ

SERVER_IP = environ.get("SERVER_IP")

uri = "http://"+ SERVER_IP + "logstash*/_search"

query = json.dumps({
{
  "query": {
    "json.correlation_id": "1.2.826.0.1.2112370.55.1.12527038"
  }
})



r = requests.get(uri,auth = HTTPBasicAuth(username, password),headers=HEADERS, data=query).json()
print(r)




# print request object








#json file from kibana logs
json_file = '''

{

  "_index": "logstash-2022.09.01",

  "_type": "_doc",

  "_id": "Zezq-YIBUbb8egOZR9Ch",

  "_version": 1,

  "_score": null,

  "_source": {

    "kubernetes": {

      "node": {

        "name": "head1"

      },

      "labels": {

        "pod-template-hash": "688c698b68",

        "app": "engine"

      },

      "container": {

        "name": "engine",

        "image": "registry.gitlab.com"

      },

      "replicaset": {

        "name": "engine"

      },

      "pod": {

        "uid": "9b72c404-efc2-4e65-81b3-fc466d6a4d1e",

        "name": "engine"

      },

      "namespace": "aie"

    },

    "ecs": {

      "version": "1.6.0"

    },

    "tags": [

      "beats_input_raw_event"

    ],

    "@version": "1",

    "log": {

      "offset": 31388488,

      "file": {

        "path": "/var/log/containers/engine.log"

      }

    },

    "event": {

      "timezone": "+00:00"

    },

    "agent": {

      "id": "4b7996f9-f823-4536-a170-d080cc7d48f6",

      "type": "filebeat",

      "hostname": "head1",

      "version": "7.10.2",

      "name": "head1",

      "ephemeral_id": "62dc4285-9dff-49ca-b56a-077d13dc7384"

    },

    "host": {

      "os": {

        "codename": "Core",

        "platform": "centos",

        "family": "redhat",

        "version": "7 (Core)",

        "kernel": "5.4.0-122-generic",

        "name": "CentOS Linux"

      },

      "id": "3d458769eadb4ca1ac689c5da40af2bf",

      "mac": [

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "18:c0:4d:79:3d:fa",

        "ee:ee:ee:ee:ee:ee",

        "18:c0:4d:79:3d:fb",

        "ee:ee:ee:ee:ee:ee",

        "8e:cd:e7:ed:46:cc",

        "ee:ee:ee:ee:ee:ee",

        "8e:cd:e7:ed:46:cc",

        "ee:ee:ee:ee:ee:ee",

        "8e:cd:e7:ed:46:cc",

        "ee:ee:ee:ee:ee:ee",

        "02:42:60:4c:fa:6d",

        "ee:ee:ee:ee:ee:ee",

        "56:64:b9:71:15:79",

        "92:74:1f:b0:a2:b4",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee",

        "ee:ee:ee:ee:ee:ee"

      ],

      "hostname": "gstt-head1",

      "containerized": true,

      "name": "gstt-head1",

      "architecture": "x86_64",

      "ip": [

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "10.36.191.223",

        "fe80::1ac0:4dff:fe79:3dfa",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "10.0.0.5",

        "fe80::8ccd:e7ff:feed:46cc",

        "fe80::ecee:eeff:feee:eeee",

        "172.17.0.1",

        "fe80::ecee:eeff:feee:eeee",

        "10.233.0.1",

        "10.233.0.3",

        "10.233.4.111",

        "10.233.18.229",

        "10.233.22.154",

        "10.233.54.210",

        "10.233.49.203",

        "10.233.46.123",

        "10.233.20.160",

       "10.233.16.135",

        "10.233.62.209",

        "10.233.31.38",

        "10.233.42.97",

        "10.233.40.212",

        "10.233.45.215",

        "10.233.24.138",

        "10.233.31.134",

        "10.233.2.208",

        "10.233.44.136",

        "10.233.12.124",

        "10.233.3.10",

        "10.233.39.168",

        "10.233.0.79",

        "10.233.52.112",

        "10.233.53.55",

        "10.233.101.0",

        "169.254.25.10",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee",

        "fe80::ecee:eeff:feee:eeee"

      ]

    },

    "@timestamp": "2022-09-01T16:37:28.927Z",

    "stream": "stderr",

    "input": {

      "type": "container"

    },

    "container": {

      "id": "3d6291a3bce03ae6b5f1067adb63f6f16911aa2341b0881821c3bdd8d56b3da0",

      "runtime": "docker",

      "image": {

        "name": "engine:latest"

      }

    },

    "json": {

      "line_no": 65,

      "type": "log",

      "thread": "Thread-3438",

      "msg": "Event has arrived",

      "level": "INFO",

      "written_at": "2022-09-01T16:37:28.927Z",

      "written_ts": 1662050248927598000,

      "logger": "root",

      "correlation_id": "8df5fc30-9f8e-4950-a57b-bceabc7ac2e7",

      "module": "orchestrator"

    }

  },

  "fields": {

    "@timestamp": [

      "2022-09-01T16:37:28.927Z"

    ],

    "json.written_at": [

      "2022-09-01T16:37:28.927Z"

    ]

  },

  "highlight": {

    "container.image.name": [

      "highlighted-field@"

    ],

    "json.correlation_id": [

      "@highlighted-field@"

    ]

  },

  "sort": [

    1662050248927

  ]

}
'''

#find event message
data = json.loads(json_file)
#print((data['_source']['json']['msg']))

#send event message to https site
payload = {"message": data['_source']['json']['msg']}
r = requests.post(url="https://httpbin.org/post", data=json.dumps(payload))
#print(r.text)
