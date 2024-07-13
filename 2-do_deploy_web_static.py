#!/usr/bin/python3
"""pack web static"""

from fabric.api import env, run, put, cd
from fabric.decorators import task
from fabric.context_managers import settings
from datetime import datetime
from os.path import exists

env.hosts = ['35.175.64.12', '18.234.192.156']
env.user = 'ubuntu'
env.key_filename = ['~/.ssh/id_rsa']

@task
def do_deploy(archive_path):
    """Generates a .tgz archive from the contents of the web_static"""
    if not exists(archive_path):
        return False
    
    file_name = archive_path.split('/')[-1].split('.')[0]

    with settings(host_string=env.hosts[0]):
        deploy_by_server(archive_path, file_name)

    with settings(host_string=env.hosts[1]):
        deploy_by_server(archive_path, file_name)

def deploy_by_server(archive_path, file_name):
    put(archive_path, '/tmp/')
    with cd('/tmp/'):
        run(f"tar -xvzf {file_name}.tgz -C /data/web_static/releases/{file_name}")
        run(f'rm -r {file_name}.tgz')

    with cd('/data/web_static/'):
        run('rm current')
        run(f'ln -s /data/web_static/releases/{file_name} /data/web_static/current')

    return True
