#!/usr/local/bin/python3
"""module"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """ create version directory"""
    local("mkdir -p versions")
