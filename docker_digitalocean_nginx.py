from docker_digitalocean_common import *

def copy_nginx_src_to_remote_host(ssh_con_str):
	pwd = run_local_command("pwd").rstrip()
	local_dir = pwd + "/../../_nginx"
	print "Copying nginx src (" + local_dir + ") to remote host."
	os.system("scp -rp " + local_dir + "/* " + ssh_con_str + ":/root/nginx")
	os.system("scp -rp " + local_dir + "/.htpasswd " + ssh_con_str + ":/root/nginx")
	print "Copying nginx src to remote host finished."

def build_nginx_continer_in_remote_host(ssh):
	print "Renaming nginx-homepage.conf file to nginx.conf in remote host."
	result = ssh("mv /root/nginx/nginx-homepage.conf /root/nginx/nginx.conf")
	print "Renaming result: "
	print result

	print "Building nginx image in remote host."
	result = ssh("docker build -t nginx -f /root/nginx/Dockerfile /root/nginx")
	print "Building nginx image in remote host result: "
	print result

def run_nginx_container(ssh):
	print "Starting nginx container in remote host."
	result = ssh("docker run -d -p 80:80 -p 443:443 --link homepage:homepage --link airpolution-dev-api:airpolution-dev-api --name nginx nginx")
	print "Starting nginx container in remote host result: "
	print result
