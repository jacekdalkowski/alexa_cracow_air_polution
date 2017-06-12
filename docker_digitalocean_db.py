from docker_digitalocean_common import *

def copy_db_src_to_remote_host(ssh_con_str):
	pwd = run_local_command("pwd").rstrip()
	local_dir = pwd + "/db"
	print "Copying db src (" + local_dir + ") to remote host."
	os.system("scp -r " + local_dir + "/* " + ssh_con_str + ":/root/apps/airpolution/dev/db")
	print "Copying db src to remote host finished."



def build_db_continer_in_remote_host(ssh):
	print "Building db image in remote host."
	result = ssh("docker build -t airpolution-dev-db -f /root/apps/airpolution/dev/db/Dockerfile_dev /root/apps/airpolution/dev/db")
	print "Building db image in remote host result: "
	print result

'''
def build_db_seed_continer_in_remote_host(ssh):
	print "Building db seed image in remote host."
	result = ssh("docker build -t gardenmate-dev-db-seed -f /root/apps/gardenmate/dev/gardenmate_db/Dockerfile_dev_seed /root/apps/gardenmate/dev/gardenmate_db")
	print "Building db seed image in remote host result: "
	print result
'''


def run_db_container(ssh):
	print "Starting db container in remote host."
	result = ssh("docker run -d --name airpolution-dev-db airpolution-dev-db")
	print "Starting db container in remote host result: "
	print result

'''
def run_db_seed_container(ssh):
	print "Starting db seed container in remote host."
	result = ssh("docker run -d --name gardenmate-dev-db-seed --link gardenmate-dev-db:garden_mongo gardenmate-dev-db-seed")
	print "Starting db seed container in remote host result: "
	print result
'''
