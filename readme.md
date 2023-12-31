Using BeautifulSoup allows us to scrape websites, enabling data extraction for our purposes.
In this case, I'm interested in the short throw 4K projector 'Formovie Theater' by 'Formovie'.
It's an amazing product for a 100" TV at almost 3k instead of 25k.

In this scenario, I want an SMS alert when the product hits or falls below my target price.
Using the `requests` module, I retrieve HTML, parse with BeautifulSoup, look for product 
title and price, verifying if it's within target range.
Then, using 'Twilio' as a client, I write the `send_sms()` function to send an SMS with 
retrieved data and a link for a purchase.
