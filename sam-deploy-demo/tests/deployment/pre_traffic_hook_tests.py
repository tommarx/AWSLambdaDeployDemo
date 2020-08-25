import boto3
import json
import os

def lambda_handler(event, context):

	print('Invoking pretraffic tests.')

	deployment_id = event['DeploymentId']
	execution_id = event['LifecycleEventHookExecutionId']

	deploy_client = boto3.client('codedeploy')
	lambda_client = boto3.client('lambda')

	test_function = os.environ['TestFunction']

	function_parameters = b"""{
		"param1": 1,
		"param2": 2
	}"""

	lambda_response = lambda_client.invoke(
		FunctionName = test_function,
		InvocationType = 'RequestResponse',
		Payload = function_parameters
	)

	print('Function response:')
	print(lambda_response)
	print(lambda_response['StatusCode'])

	print('Function response payload:')
	function_response = json.load(lambda_response['Payload'])
	print(function_response['statusCode'])

	function_response_body = json.loads(function_response['body'])
	print(function_response_body['result'])

	response = deploy_client.put_lifecycle_event_hook_execution_status(
    	deploymentId = deployment_id,
    	lifecycleEventHookExecutionId = execution_id,
    	status = 'Failed'
	)

	return 'Pretraffic hook completed'
