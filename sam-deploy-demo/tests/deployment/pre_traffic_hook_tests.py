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

	function_response = json.load(lambda_response['Payload'])
	function_response_body = json.loads(function_response['body'])

	function_status_code = lambda_response['StatusCode']
	functoion_result = function_response_body['result']

	deployment_status = 'Succeeded' if function_status_code == 200 && functoion_result == 3 else 'Failed'

	response = deploy_client.put_lifecycle_event_hook_execution_status(
    	deploymentId = deployment_id,
    	lifecycleEventHookExecutionId = execution_id,
    	status = deployment_status
	)

	return 'Pretraffic hook completed'
