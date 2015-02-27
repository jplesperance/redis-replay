#!/usr/bin/env python

import argparse
import random
import redis


def addkey(server, keyIndex, length):
    global keyName

    valuechars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    keyName = "key_" + str(keyIndex)
    print keyIndex, '\n'
    value = ""
    for i in range(length):
        value += random.choice(valuechars)
    server.setex(keyName, value, 86400)
    return keyIndex


def main():

    parser = argparse.ArgumentParser(description="Create keys on redis server")
    parser.add_argument('--scale', '-s', type=int, default=1)
    parser.add_argument('--host', '-o', default='localhost')
    parser.add_argument('--port', '-p', type=int, default=6379)
    args = parser.parse_args()

    keyIndex = 10000

    server = redis.Redis(host = args.host, port = args.port)
    
    print "Deleting keys..."
    for key in server.keys('*'):
        server.delete(key)

    print "Adding", args.scale * 2000, "keys of length 128..."
    for i in range(args.scale * 2000):

        keyIndex += 1
        addkey(server, keyIndex, 128)

    print "Adding", args.scale * 1000, "keys of length 512..."
    for i in range(args.scale * 1000):
        keyIndex += 1
        addkey(server, keyIndex, 512)

    print "Adding", args.scale * 300, "keys of length 1024..."
    for i in range(args.scale * 300):
        keyIndex += 1
        addkey(server, keyIndex, 1024)

    print "Adding", args.scale * 100, "keys of length 2048..."
    for i in range(args.scale * 100):
        keyIndex += 1
        addkey(server, keyIndex, 2048)

if __name__ == '__main__':
    main()



