#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mongobeer import Mongobeer
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--connection_string", help="Mongodb Connection String")
parser.add_argument("-c", "--collection", help="Select the database/collection name",
                    default='SuspiciousActivity')

args = parser.parse_args()
MONG = Mongobeer(args)