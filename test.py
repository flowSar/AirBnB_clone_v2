#!/usr/bin/python3




value = '"value"'

if "\"" in value[:1] and "\"" in value[1:]:
    print('found')
else:
    print('not found')
