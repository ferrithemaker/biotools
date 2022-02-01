import biotools
import sys

cadena = biotools.Sequence()
cadena.readstring(sys.argv[1])
cadena.writestring(sys.argv[1])