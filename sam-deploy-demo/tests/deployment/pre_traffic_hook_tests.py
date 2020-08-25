import boto3
import json

def lambda_handler(event, context):

	print('Invoking pretraffic tests.')

	deployment_id = event['DeploymentId']
	execution_id = event['LifecycleEventHookExecutionId']

	print('Deployment id:')
	print(deployment_id)
	print('Execution id:')
	print(execution_id)

	deploy_client = boto3.client('codedeploy')

	response = deploy_client.put_lifecycle_event_hook_execution_status(
    	deploymentId = event['DeploymentId'],
    	lifecycleEventHookExecutionId = ['LifecycleEventHookExecutionId'],
    	status = 'Failed'
	)

	return 'Pretraffic hook completed'
