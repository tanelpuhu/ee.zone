#!/usr/bin/env python3
import os
import sys


def main(input_file, output_file):
    if not os.path.exists(input_file):
        return
    hosts = set()
    with open(input_file) as fp:
        for line in fp.readlines():
            sp = line.strip().split()
            if len(sp) != 5:
                continue
            domain = sp[0].strip('.')
            if domain not in hosts:
                hosts.add(domain)
    with open(output_file, 'w') as fp:
        for host in sorted(hosts):
            fp.write('%s\n' % host)


if __name__ == '__main__':
    main(*sys.argv[1:])
