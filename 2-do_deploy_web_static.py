#!/usr/bin/python3
"""pack web static"""

from fabric.api import env, run, put, cd
from datetime import datetime
from os.path import exists

env.hosts = ['35.175.64.12', '18.234.192.156']
env.user = 'ubuntu'
env.key_filename = ['~/.ssh/id_rsa']


def do_deploy(archive_path):
    """Generates a .tgz archive from the contents of the web_static"""
    if not exists(archive_path):
        return False
    
    file_name = archive_path.split('/')[-1].split('.')[0]
    try :
        put(archive_path, '/tmp/')
        cd('/tmp/')
        run(f"tar -xvzf {file_name}.tgz -C /data/web_static/releases/{file_name}")
        run(f'rm -r {file_name}.tgz')
        cd('/data/web_static/')
        run('rm current')
        run(f'ln -s /data/web_static/releases/{file_name} /data/web_static/current')
        
        return True
    except Exception as e:
        return False
