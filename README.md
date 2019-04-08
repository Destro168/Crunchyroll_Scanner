# Program Description:

This program reloads Crunchyrolls Official Guest Pass Thread while searching for changes. Once a change is found, a beep goes off, a log is written to the command line and two file logs containing the differences are written to the system.

The program works well. But, Crunchyroll forum's have a rate limiter for requests it seems. So, it isn't the best method to be alerted to new posts. However, it works! And, that's all that matters I suppose!

#  Program Notes:

This can be used to write data to a file pretty easily:

fo = open("lib/log" + str(count) + "-m.txt", "a")
fo.write(str(post_list))
fo.close()

# Main tutorials used in creating this program:

Using tutorial (Actually worked!):
https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3

Pythong tutorials:
https://docs.python.org/3/installing/index.html