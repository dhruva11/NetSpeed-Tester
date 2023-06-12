"""
GoTo Command Prompt and install speedtest package using command 'pip install speedtest-cli'
"""
import os
os.system('cmd /c "speedtest-cli"')

'''
The output will be like-

Retrieving speedtest.net configuration...
Testing from Airtel (122.171.234.218)...
Retrieving speedtest.net server list...
Selecting best server based on ping...
Hosted by ACT Fiber-net (Hyderabad) [499.30 km]: 32.973 ms
Testing download speed................................................................................
Download: 113.45 Mbit/s
Testing upload speed......................................................................................................
Upload: 109.73 Mbit/s

Process finished with exit code 0
'''