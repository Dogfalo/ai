#!/usr/bin/env python
#
# Sample dropblox_ai exectuable.
#

import json
import time
import sys

if __name__ == '__main__':
   if len(sys.argv) == 3:
      game_state = json.loads(sys.argv[1]) # The game state is passed in as a json blob.
      seconds_remaining = sys.argv[2]	   # How many seconds until the game is over.
      print str(seconds_remaining)
      print 'left'                         # Print your moves to standard out and they'll be sent up to our game server.
      sys.stdout.flush()                   # We flush standard out to make sure moves are communicated to the game server immediately.
      time.sleep(11)                       # Do a bunch of fancy AI computation!
      print 'right'
      sys.stdout.flush()