import boto3
import time

client = boto3.client('ec2')

def stop_instances(my_instance):
    client.stop_instances(InstanceIds=[my_instance])
    waiter=client.get_waiter('instance_stopped')
    waiter.wait(InstanceIds=[my_instance])

def change_size(my_instance,targetsize):
    client.modify_instance_attribute(InstanceId=my_instance, Attribute='instanceType', Value=targetsize)

def start_instances(my_instance):
    client.start_instances(InstanceIds=[my_instance])

def main ():
    webservers = {'server1' : 'i-xxxxxxxxxxx','server2' : 'i-xxxxxxxxxx','server3' : 'i-xxxxxxxxx'}
    for k, v in webservers.iteritems():
        my_instance = (v)
        instance_name = (k)
        targetsize = 'c4.2xlarge'
        print (instance_name + " is stopping")
        stop_instances(my_instance)
        print (instance_name + " resizing to " + targetsize)
        change_size(my_instance,targetsize)
        print (instance_name + " is starting")
        start_instances(my_instance)
        time.sleep(60) 

main()
