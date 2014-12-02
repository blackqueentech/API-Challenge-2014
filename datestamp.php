<?php
/*
This uses the array I got from convertFromSeconds in my timestamp.py file. There I converted
the value of seconds (252583761) to an array of days, hours, minutes, and seconds which was
[2923, 10, 9, 21]. With those values, I added them to the base time stamp we recieved:
"datestamp": "2038-09-04T21:20:00.000Z"

I think I'm close, but I don't have the formatting correct. 
*/
echo date(DATE_ATOM, mktime(21+10, 20+9, 0+12, 9, 4+2923 , 2038));
?>
