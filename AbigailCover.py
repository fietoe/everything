
#Setup
from earsketch import *
init()
setTempo(120)
def chorus(startmeasure, endmeasure):
  fitMedia(DUBSTEP_BASS_WOBBLE_025, 2, startmeasure, endmeasure)
  fitMedia(DUBSTEP_BASS_WOBBLE_015, 3, startmeasure, endmeasure)
drum = DUBSTEP_DRUMLOOP_MAIN_009
drum2 = DUBSTEP_DRUMLOOP_MAIN_008
#Music
fitMedia(FIETOE_MOTIONLESS_IN_WHITE_ABIGAIL_OFFICIAL_MUSIC_VIDEO, 1, 1, 88)
for measure in range (2, 81):
  fitMedia(drum, 4, measure, measure + 0.5)
  fitMedia(drum2, 4, measure + 0.5 , measure + 1)
  
fitMedia(DUBSTEP_BASS_WOBBLE_017, 2, 2, 5)
fitMedia(DUBSTEP_BASS_WOBBLE_020, 2, 6, 12)

chorus(14, 24)

fitMedia(DUBSTEP_BASS_WOBBLE_038, 2, 24, 29)
fitMedia(DUBSTEP_BASS_WOBBLE_039, 2, 30, 40)
fitMedia(DUBSTEP_DRUMLOOP_MAIN_006, 3, 30, 40)
fitMedia(DUBSTEP_BASS_WOBBLE_041, 2, 41, 51)

chorus(52, 63)

#don't put anything between 63 and 72

fitMedia(DUBSTEP_BASS_WOBBLE_038, 2, 72, 76)
#Effects
setEffect(2, VOLUME, GAIN, 4, 2, 5)

#Finish
finish()
