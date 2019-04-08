#import all the goodies.
import requests
from bs4 import BeautifulSoup
import time
import datetime
import winsound

# Initialize variables
url = 'https://www.crunchyroll.com/forumtopic-803801/the-official-guest-pass-thread-read-opening-post-first?pg=last'
saved_post_list = []
firstRun = True
count = 0
frequency = 1500  # 2500 Hertz
duration = 1000  # 1000 ms

print("Running Scanner!") # Alert the user that the program has begun.

while (True):
	page = requests.get(url) # Get the page's contents.
	soup = BeautifulSoup(page.text, 'html.parser') # Parse the contents.
	
	# Parse some more.
	post_list = soup.findAll('div', class_='showforumtopic-message-contents-text')
	
	# If we loaded some real data (non-empty), then attempt to save it and potentially
	# alert the user of the script if the data is interesting.
	if post_list != saved_post_list and post_list != [] and post_list != None:
		# We don't want alerts on the first time that data is loaded, so we use a simple boolean flag to hnadle program flow.
		if firstRun == False:
			print(datetime.datetime.now(), ': ', "Post detected!!!")
			
			#perform a beep.
			winsound.Beep(frequency, duration)

			#Open file and write data.
			fo = open("lib/log-" + str(count) + "-a.txt", "a")
			fo.write(str(post_list))
			fo.close()
			
			#Open file and write data.
			fo = open("lib/log" + str(count) + "-b.txt", "a")
			fo.write(str(saved_post_list))
			fo.close()
		else:
			firstRun = False
		
		# Always update the svaed post list with the latest non-empty data.
		saved_post_list = post_list
	
	# Always output every 10 seconds whether any changes occured.
	if count % 10 == 0:
		print(datetime.datetime.now(), ': ', "No changes.")
	
	count = count + 1 # Increment second counter for log file name purposes.
	time.sleep(1) # wait a second
