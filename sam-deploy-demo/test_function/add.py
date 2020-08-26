import boto3
import json

def lambda_handler(event, context):

	param_1 = event['param1']
	param_2 = event['param2']

	return {
		'statusCode': 200,
		'body': json.dumps({
			'result': param_1 + param_2 + 1 # Should result in the pretraffic test failing
		}) 
	}