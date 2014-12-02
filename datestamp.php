<?php
/*
This uses the array I got from convertFromSeconds in my timestamp.py file. There I converted
the value of seconds (252583761) to an array of days, hours, minutes, and seconds which was
[2923, 10, 9, 21]. With those values, I added them to the base time stamp we recieved:
"datestamp": "2038-09-04T21:20:00.000Z"

I think I'm close, but I don't have the formatting correct. 

Got a new example for the challenge:
"datestamp": "1992-02-02T07:28:00.000Z",
"interval": 443206960
convertFromSeconds(443206960) >> [5129, 17, 2, 40]
*/
echo date(DATE_ATOM, mktime(7+17, 28+2, 0+40, 2, 2+5129, 1992)); 
// returns 2006-02-18T00:30:40-05:00
// when posting this, I deleted the -05.00 and replaced it with .000Z! I hope that's not cheating... 
?>
