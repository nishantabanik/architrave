1. The Ansible playbooks and roles you would create for each component

Here's a summary of the Ansible playbooks and roles created for each component of your 3-tier web application deployment:

Playbooks:
-------------
deploy_app.yml: Deploys the entire 3-tier web application by including the following roles:
-- load_balancer
-- web_frontend
-- app_servers
-- database

create_load_balancer.yml: Creates the Kubernetes Service for the load balancer using the load_balancer role.

create_web_frontend.yml: Creates the Kubernetes Deployment for web frontends using the web_frontend role.

create_app_servers.yml: Creates the Kubernetes Deployment for application servers using the app_servers role.

create_database.yml: Creates the Kubernetes Deployment for the database using the database role.

update_app.yml: Performs a rolling update of the application servers using the app_servers role to update the Docker image version.

Roles:
-----------

-- common (Shared Configuration): 
Contains common tasks and configurations shared across all components.

-- load_balancer (Load Balancer Configuration): 
Defines tasks for creating a Kubernetes Service for the load balancer.
Utilizes templates for load balancer service YAML.

-- web_frontend (Web Frontend Configuration):
Defines tasks for creating a Kubernetes Deployment for web frontends.
Utilizes templates for frontend deployment YAML.

-- app_servers (Application Servers Configuration):
Defines tasks for creating a Kubernetes Deployment for application servers.
Utilizes templates for app servers deployment YAML.

-- database (Database Configuration):
Defines tasks for creating a Kubernetes Deployment for the database.
Utilizes templates for database deployment YAML.


2. How would you organize the code for reusability across environments

To organize the Ansible code for reusability across different environments (e.g., dev, prod, stage), we've set up a directory structure and configuration approach that allows us to manage environment-specific variables and inventory files. Here's how we've organized the code:







Your approach to configuring other Kubernetes objects like services
How you would manage app configuration
Your strategy for rolling updates and minimizing downtime