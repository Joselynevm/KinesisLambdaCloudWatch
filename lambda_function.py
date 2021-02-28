from __future__ import print_function
#import json
import base64
def lambda_handler(event, context):
    for record in event['Records']:
    #Kinesis data is base64 enconded so decode here
    payload=base64.b64decode(record["Kinesis"]["data"])
    print("Decoded payload: "+ str(pay))
