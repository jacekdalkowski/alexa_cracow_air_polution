from docker_digitalocean_common import *

def copy_scraper_src_to_remote_host(ssh_con_str):
	pwd = run_local_command("pwd").rstrip()
	local_dir = pwd + "/scraper"
	print "Copying scraper src (" + local_dir + ") to remote host."
	os.system("scp -r " + local_dir + "/* " + ssh_con_str + ":/root/apps/airpolution/dev/scraper")
	print "Copying scraper src to remote host finished."



def build_scraper_continer_in_remote_host(ssh):
	print "Building scraper image in remote host."
	result = ssh("docker build -t airpolution-dev-scraper -f /root/apps/airpolution/dev/scraper/Dockerfile_dev /root/apps/airpolution/dev/scraper")
	print "Building scraper image in remote host result: "
	print result



def run_scraper_container(ssh):
	print "Starting scraper container in remote host."
	result = ssh("docker run -d --name airpolution-dev-scraper --link airpolution-dev-db:airpolution-db airpolution-dev-scraper")
	print "Starting scraper container in remote host result: "
	print result


