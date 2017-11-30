Current use is something like:

`cat tr.final| lt-proc ~/Dev/Apertium/apertium-tur/tur.automorf.bin | python intersect.py -c config | lt-proc -g ~/Dev/Apertium/apertium-tur/tur.autogen.bin | sort | uniq > tr.fut`
