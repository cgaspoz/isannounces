# Introduction #

In order to improve the retrieval of the location information in the body of messages, add the location of the message's sender.


# Details #

We could also add a small flag in the messages listing, based on the sender IP (which should match the sender location in most of the cases).

It seems that, by manually inspecting a sample of messages, the last IP of the header that is not private or local should give a good approximation of the sender's location.

# Sources #

  * http://code.google.com/p/geo-ip-location/wiki/GoogleAppEngine
  * http://geo.xjs.pl/
  * http://www.maxmind.com/app/web_services_omni
  * http://www.famfamfam.com/lab/icons/flags/