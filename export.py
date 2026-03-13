from music21 import converter

score = converter.parse("output.mid")
score.write('musicxml', 'output.xml')