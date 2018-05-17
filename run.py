#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socketeer import Socketeer
import argparse

"""
Replicates the following functionality

printUsage()
{
    echo
    echo "Usage:"
    echo
    echo "run.sh -h|--help"
    echo "run.sh -m <client|server> -p <80> - s localhost"
    exit 1
}
"""
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", help="Client or Server")
parser.add_argument("-p", "--port", help="Change the default port", default=80)
parser.add_argument("-s", "--server_name", help="Server name", default="localhost")

args = parser.parse_args()
SOCK = Socketeer(args)