import boto3
import json

def lambda_handler(event, context):

	print('Invoking pretraffic tests.')

	deployment_id = event['DeploymentId']
	execution_id = event['LifecycleEventHookExecutionId']

	deploy_client = boto3.client('codedeploy')

	print("Context:")
	print(context)
	print("Event:")
	print(event)

	response = deploy_client.put_lifecycle_event_hook_execution_status(
    	deploymentId = deployment_id,
    	lifecycleEventHookExecutionId = execution_id,
    	status = 'Succeeded'
	)

	return 'Pretraffic hook completed'
