import subprocess
import re
import os
import time
import sh
import time
from docker_digitalocean_db import *
from docker_digitalocean_scraper import *
from docker_digitalocean_api import *
from docker_digitalocean_nginx import *

def deploy_dev_api(ssh, ssh_con_str):
	kill_and_remove_containers(ssh, 'airpolution-dev-api')
	kill_and_remove_containers(ssh, 'airpollution-dev-api')
	copy_api_src_to_remote_host(ssh_con_str)
	build_api_continer_in_remote_host(ssh)

def deploy_prod1_api(ssh, ssh_con_str):
	kill_and_remove_containers(ssh, 'airpollution-prod1-api')
	copy_api_src_to_remote_host(ssh_con_str, 'prod1')
	build_api_continer_in_remote_host(ssh, 'prod1')

def deploy_prod2_api(ssh, ssh_con_str):
	kill_and_remove_containers(ssh, 'airpollution-prod2-api')
	copy_api_src_to_remote_host(ssh_con_str, 'prod2')
	build_api_continer_in_remote_host(ssh, 'prod2')

ssh_con_str = "root@207.154.255.70"
#ssh_con_str = "root@46.101.148.70"

print "NOTICE: this script has to be run as a user with access to SSH keys."
print "Deployment to remote server (" + ssh_con_str + ") started."

ssh = sh.ssh.bake(ssh_con_str)

print "Successfully connected to remote server."

#kill_and_remove_containers(ssh, 'airpolution-dev-db')
#copy_db_src_to_remote_host(ssh_con_str)
#build_db_continer_in_remote_host(ssh)

#kill_and_remove_containers(ssh, 'airpolution-dev-scraper')
#copy_scraper_src_to_remote_host(ssh_con_str)
#build_scraper_continer_in_remote_host(ssh)

deploy_prod1_api(ssh, ssh_con_str)
deploy_prod2_api(ssh, ssh_con_str)

#run_db_container(ssh)
#run_scraper_container(ssh)
run_api_container(ssh, 'prod1')
run_api_container(ssh, 'prod2')

#kill_and_remove_containers(ssh, 'nginx')
#copy_nginx_src_to_remote_host(ssh_con_str)
#build_nginx_continer_in_remote_host(ssh)
#run_nginx_container(ssh)





#kill_and_remove_containers(ssh, 'gardenmate-dev-identity')
#copy_identity_src_to_remote_host(ssh_con_str)
#build_identity_continer_in_remote_host(ssh)


#kill_and_remove_containers(ssh, 'gardenmate-dev-designer')
#copy_designer_src_to_remote_host(ssh_con_str)
#build_designer_continer_in_remote_host(ssh)


#kill_and_remove_containers(ssh, 'gardenmate-dev-db')
#copy_db_src_to_remote_host(ssh_con_str)
#build_db_continer_in_remote_host(ssh)
#build_db_seed_continer_in_remote_host(ssh)


#kill_and_remove_containers(ssh, 'gardenmate-dev-api')
##copy_api_src_to_remote_host(ssh_con_str)
#build_api_continer_in_remote_host(ssh)

#run_designer_container(ssh)
#run_db_container(ssh)
#run_db_seed_container(ssh)
#run_api_container(ssh)
#run_identity_container(ssh)
#run_www_container(ssh)

#copy_assets_to_remote_host(ssh_con_str)

#kill_and_remove_containers(ssh, 'nginx')
#copy_nginx_src_to_remote_host(ssh_con_str)
#build_nginx_continer_in_remote_host(ssh)
#run_nginx_container(ssh)




