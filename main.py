
import boto3
#from os.path import dirname

#script_dir = dirname(__file__)
#print(script_dir)
sess = boto3.Session(region_name='ap-south-1')

cfnclient = sess.client('cloudformation')

stack = ''
with open('nestedstack.yaml','r')as fd:
    stack = fd.read()

print(stack)

cfnclient.create_stack(StackName='mythirdtask',TemplateBody=stack)




