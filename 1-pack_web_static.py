#!/usr/bin/python3
""" pack web static"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ generates a .tgz archive from the contents of the web_static """
    local("mkdir -p versions")

    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    arc_name = "versions/web_static_{}.tgz".format(date_time)

    command = "tar -cvzf {} web_static".format(arc_name)
    result = local(command)
    if result.failed:
        return None
    return arc_name
