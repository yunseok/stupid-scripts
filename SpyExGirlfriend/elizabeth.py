import subprocess
import time

stupidEx = '[REDACTED]'		# Username of my ex-girlfriend, REDACTED
username = 'anant.sisou'	# My Instagram username, give me a follow!

while True:
	subprocess.run(['instaloader', stupidEx, '--login', username, '--stories'])
	time.sleep(18000)