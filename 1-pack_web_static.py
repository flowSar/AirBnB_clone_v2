#!/usr/bin/python3
"""pack web static"""

from fabric import Connection
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    local_conn = Connection('localhost')
    local_conn.local('mkdir versions')
    today = datetime.today().strftime('%Y%m%d%H%M%S')
    arc_name = f"versions/web_static_{today}.tgz"
    command = f"tar -cvzf {arc_name} versions/"
    result = local_conn.local(command)
    if result.failed:
        return None
    return arc_name
