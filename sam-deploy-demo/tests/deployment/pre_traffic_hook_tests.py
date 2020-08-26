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

	param_1 = 1
	param_2 = 2

	function_parameters = b"""{
		"param1": %i,
		"param2": %i
	}""" % (param_1, param_2)

	lambda_response = lambda_client.invoke(
		FunctionName = test_function,
		InvocationType = 'RequestResponse',
		Payload = function_parameters
	)

	function_response = json.load(lambda_response['Payload'])
	function_response_body = json.loads(function_response['body'])

	function_status_code = lambda_response['StatusCode']
	functoion_result = function_response_body['result']
	expected_result = param_1 + param_2

	deployment_status = 'Succeeded' if function_status_code == 200 and functoion_result == expected_result else 'Failed'

	response = deploy_client.put_lifecycle_event_hook_execution_status(
    	deploymentId = deployment_id,
    	lifecycleEventHookExecutionId = execution_id,
    	status = deployment_status
	)

	return 'Pretraffic hook completed'
