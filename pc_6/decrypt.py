#!/usr/bin/env python

import zlib

zip_data = zlib.ZipFile('channel.zip', 'r')
print zip_data.namelist()
