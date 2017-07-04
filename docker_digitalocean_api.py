from docker_digitalocean_common import *

def copy_api_src_to_remote_host(ssh_con_str, env):
	pwd = run_local_command("pwd").rstrip()
	local_dir = pwd + "/api"
	print "Copying api src (" + local_dir + ") to remote host."
	#os.system("scp -r " + local_dir + "/* " + ssh_con_str + ":/root/apps/airpollution/" + env + "/api")
	rsync_cmd = "rsync -azP --delete --exclude '*/node_modules' " + local_dir + "/ " + ssh_con_str + ":/root/apps/airpollution/" + env + "/api"
	print "rsync command: " + rsync_cmd
	os.system(rsync_cmd)
	print "Copying api src to remote host finished."



def build_api_continer_in_remote_host(ssh, env):
	print "Building api image in remote host."
	result = ssh("docker build -t airpollution-" + env + "-api -f /root/apps/airpollution/" + env + "/api/Dockerfile_" + env + " /root/apps/airpollution/" + env + "/api")
	print "Building api image in remote host result: "
	print result



def run_api_container(ssh, env):
	print "Starting api container in remote host."
	result = ssh("docker run -d --name airpollution-" + env + "-api --link airpolution-dev-db:airpolution-db airpollution-" + env + "-api")
	print "Starting api container in remote host result: "
	print result

