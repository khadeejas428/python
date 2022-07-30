from asyncio import DatagramProtocol


def file_read(fname):
    with open(fname, "r") as f:
        data= f.readlines()
        print(data)

file_read('includedata.txt')
