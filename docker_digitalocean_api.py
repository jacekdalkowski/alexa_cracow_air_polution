from docker_digitalocean_common import *

def copy_api_src_to_remote_host(ssh_con_str):
	pwd = run_local_command("pwd").rstrip()
	local_dir = pwd + "/api"
	print "Copying api src (" + local_dir + ") to remote host."
	os.system("scp -r " + local_dir + "/* " + ssh_con_str + ":/root/apps/airpolution/dev/api")
	print "Copying api src to remote host finished."



def build_api_continer_in_remote_host(ssh):
	print "Building api image in remote host."
	result = ssh("docker build -t airpolution-dev-api -f /root/apps/airpolution/dev/api/Dockerfile_dev /root/apps/airpolution/dev/api")
	print "Building api image in remote host result: "
	print result



def run_api_container(ssh):
	print "Starting api container in remote host."
	result = ssh("docker run -d --name airpolution-dev-api --link airpolution-dev-db:airpolution-db airpolution-dev-api")
	print "Starting api container in remote host result: "
	print result

