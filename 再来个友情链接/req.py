#!/usr/bin/env python2
# coding: utf-8

import requests
import thread
import sys

url = 'http://127.0.0.1:8899/xxx'
threads = 2
locks = []
done = False

def get(url):
	try:
		r = requests.get(url, timeout=1)
	except:
		r = False
	if r:
		return r.status_code
	else:
		return 500

def job(t, url, lock):
	while (not done):
		c = get(url)
		if c == 200:
			print '200'
	lock.release()

def main():
	for i in xrange(threads):
		try:
			lock = thread.allocate_lock()
			lock.acquire()
			locks.append(lock)
			thread.start_new_thread(job, (i, url, lock))
		except:
			print 'Fail to start new thread'
	for lock in locks:
		while lock.locked():
			pass;
	print 'Done'

main()
