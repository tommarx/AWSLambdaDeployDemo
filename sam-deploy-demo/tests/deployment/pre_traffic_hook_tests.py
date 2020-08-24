import boto3
import json

def lambda_handler(event, context):

	deployment_id = event['DeploymentId']
	execution_id = event['LifecycleEventHookExecutionId']

	deploy_client = boto3.client('codedeploy')

	response = deploy_client.put_lifecycle_event_hook_execution_status(
    	deploymentId = event['DeploymentId'],
    	lifecycleEventHookExecutionId = ['LifecycleEventHookExecutionId'],
    	status = 'Succeeded'
	)

	return 'Pretraffic hook hanlder completed.'
