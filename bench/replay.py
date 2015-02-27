#!/usr/bin/env python

import argparse
import redis
import


def replay_command(server, line):
    parts = line.split()
    cmd = parts[0].lower()
    if cmd == 'setex':
        server.setex(parts[1], parts[3], parts[2])
    elif cmd == 'del':
        server.delete(parts[1])


def main():

    parser = argparse.ArgumentParser(description = "Replay output from redis-sa")
    parser.add_argument('-o', '--host', default = 'localhost', help='The hostname/IP of the Redis server. Default: localhost')
    parser.add_argument('-p', '--port', type = int, default = 6379, help='The port Redis is running on. Default: 6379')
    parser.add_argument('parsefile', help="The file to replay", metavar="FILE", nargs=1)
    args = parser.parse_args()

    commands = open(args.parsefile[0], 'r')
    server = redis.Redis(host=args.host, port=args.port)
    counter = 1
    for line in commands:
        counter += 1
        replay_command(server, line)
    print counter


if __name__ == '__main__':
    main()