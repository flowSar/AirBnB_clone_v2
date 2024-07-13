#!/usr/bin/python3
"""pack web static"""

from fabric import Connection
from datetime import datetime

env.hosts = ['35.175.64.12', '18.234.192.156']
env.user = 'ubuntu' 
env.key_filename = ['~/.ssh/id_rsa']


def do_deploy(archive_path):
    """generates a .tgz archive from the contents of the web_static"""
    with Connection(env.hosts[0]) as server_conn1, Connection(env.hosts[1]) as server_conn2:
        deply_by_server(server_conn1, archive_path)
        deply_by_server(server_conn2, archive_path)


def deply_by_server(server_conn, archive_path):
    server_conn.put(archive_path, '/tmp/')
    file_name = archive_path.split('/')[-1].split('.')[0]
    result = None
    with server_conn.run('cd /tmp/'):
        command = f"tar -xvzf {file_name}.tgz -C /data/web_static/releases/{file_name}"
        result = server_conn.run(command)
        result = server_conn.run(f'rm -r {file_name}.tgz')
    
    with server_conn.run('cd /data/web_static/'):
        server_conn.run('rm current')
        result = command_sys_link = f'ln -s /data/web_static/releases/{file_name} /data/web_static/current'
        result = server_conn.run(command_sys_link)
    
    if result.failed:
        return False
    return True
