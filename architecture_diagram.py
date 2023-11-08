from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Service

with Diagram("3-Tier Web App in Kubernetes on AWS", show=False):
    with Cluster("AWS Services"):
        elb = ELB("Load Balancer")
        rds = RDS("Database")
        ec2 = EC2("EC2 Instances")

    with Cluster("Kubernetes Cluster"):
        web_frontend = Pod("Web Frontends")
        app_servers = Pod("App Servers")
        service = Service("K8s Service")

    elb >> ec2 >> web_frontend
    web_frontend >> service
    app_servers >> rds
