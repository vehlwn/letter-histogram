# letter-histogram

Caclulate relative frequencies of letters in an UTF-8 text file and draw bar chart with matplotlib.

## Help

```bash
$ python main.py -h
usage: main.py [-h] -i INPUT [-j]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        file name to be processed (default: None)
  -j, --dump-json       print json object with frequencies (default: False)
```

## Build

```bash
$ python main.py -j -i the-godfather.txt
{"t": 0.08894916744577983, "h": 0.06787850991045513, "e": 0.12339252784113962, "g": 0.021608008152531586, "o": 0.0806731537731919, "d": 0.045529609240259505, "f": 0.020807410010733444, "a": 0.0804058354105915, "r": 0.05169421493210521, "m": 0.02572498232577831, "i": 0.06734387318525434, "p": 0.015169299368070247, "u": 0.0283276047596238, "z": 0.002107337142733079, "b": 0.015064814525835574, "n": 0.06972938425861219, "v": 0.008985696432181875, "y": 0.021678569344690066, "s": 0.05874762025594715, "c": 0.02482668407176073, "l": 0.043627170943986625, "k": 0.010240871485000998, "w": 0.023897176059673057, "j": 0.0018847979982332564, "x": 0.0010679165043985404, "q": 0.0005943423493348929, "\u00e9": 3.799448808533562e-05, "\u00ff": 1.3569460030477007e-06, "\u00ec": 1.3569460030477007e-06, "\u00f0": 1.3569460030477007e-06, "\u00f9": 1.3569460030477007e-06}

$ python main.py -j -i Достоевский\ Федор.\ Униженные\ и\ оскорбленные.txt
{"\u0444": 0.000755836082784796, "\u0435": 0.09173216344098435, "\u0434": 0.03189303566500046, "\u043e": 0.11080124036489385, "\u0440": 0.03816701632353392, "\u043c": 0.033709567730309024, "\u0438": 0.0591265854067715, "\u0445": 0.007444714829720413, "\u0430": 0.08778882769643169, "\u0439": 0.010139748499602239, "\u043b": 0.048111943112060365, "\u0432": 0.043149401193824155, "\u0447": 0.017992145798796075, "\u0441": 0.050621174594527314, "\u0442": 0.06388167828080664, "\u043a": 0.0321906799458107, "\u0443": 0.02790460230214322, "\u043d": 0.06711788337034344, "\u0436": 0.011263581147752425, "\u044b": 0.0164137291581357, "\u0431": 0.018912137212209548, "\u044c": 0.02187956049665105, "\u043f": 0.024507849691442096, "\u044f": 0.02530697948779929, "\u0433": 0.01741850409396179, "i": 0.0001569397116999457, "\u0448": 0.010154179737459705, "\u0446": 0.002774405478097891, "\u044d": 0.0035410649892757863, "\u0449": 0.002485780720948565, "\u044e": 0.006299235324784027, "\u0437": 0.015517188506240608, "\u044a": 0.00022007637732636065, "d": 1.4431237857466272e-05, "o": 4.50976183045821e-05, "r": 4.148980884021553e-05, "f": 5.411714196549852e-06, "b": 2.5254666250565974e-05, "a": 5.952885616204837e-05, "e": 9.199914134134748e-05, "v": 4.6901523036765385e-05, "x": 2.5254666250565974e-05, "t": 3.6078094643665676e-05, "s": 2.3450761518382692e-05, "c": 1.6235142589649557e-05, "l": 2.3450761518382692e-05, "n": 5.231323723331523e-05, "u": 1.8039047321832838e-05, "p": 1.4431237857466272e-05, "h": 1.4431237857466272e-05, "m": 5.952885616204837e-05, "q": 3.607809464366568e-06, "j": 3.607809464366568e-06}
```
