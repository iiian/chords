import random
import sys
import time

CHORDS = ["Ab", "A", "A#", "Bb", "B", "C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#" ]
VARIANT = [
  "",
  "Maj9", 
  "Maj7", 
  "min", 
  "min9", 
  "min7",
  "min7b5",
  "dim", 
  "dim7",
  "dim Maj7",
  "aug",
  "7",
  "9",
]

PART = [CHORDS, VARIANT]

def get_root(current):
  while (nxt := random.choice(PART[0])) == current[0]: pass
  current[0] = nxt
  current[1] = random.choice(PART[1])
  return current

def run():
  slp = float(sys.argv[1]) if 1 < len(sys.argv) else 5
  csrc = [None, None]
  cdest = [None, None]
  max_len = 0
  while True:
    csrc = get_root(csrc)
    cdest = get_root(cdest)
    tim = slp
    while 0 < tim:
      outstr = "\r%s :: %s to %s" % (str(round(tim, 2)).rjust(4), " ".join(csrc), " ".join(cdest))
      outstr_len = len(outstr)
      if outstr_len < max_len:
        outstr += " " * (max_len - outstr_len)
      else:
        max_len = outstr_len
      sys.stdout.write(outstr)
      sys.stdout.flush()
      time.sleep(.1)
      tim -= .1

run()