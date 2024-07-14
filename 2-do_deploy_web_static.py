#!/usr/bin/python3
"""pack web static"""

from fabric.api import env, run, put, cd
from datetime import datetime
from os.path import exists

env.hosts = ['35.175.64.12', '18.234.192.156']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Generates a .tgz archive from the contents of the web_static"""
    if not exists(archive_path):
        return False

    file_name = archive_path.split('/')[-1].split('.')[0]
    try:
        put(archive_path, '/tmp/')
        # cd('/tmp/')
        run(f'sudo mkdir -p /data/web_static/releases/')
        destination = "/data/web_static/releases/"
        run(f"sudo tar -xvzf /tmp/{file_name}.tgz -C {destination}")
        # we extract the file and move then from web_static to file_name
        origin = f"/data/web_static/releases/{file_name}/web_static/*"
        destination = f"/data/web_static/releases/{file_name}/"
        run(f"mv {origin} {destination}")

        run(f'sudo rm -r /tmp/{file_name}.tgz')
        # cd('/data/web_static/')
        run('sudo rm /data/web_static/current')
        destination = "/data/web_static/current"
        run(f'sudo ln -s /data/web_static/releases/{file_name} {destination}')

        return True
    except Exception as e:
        return False
