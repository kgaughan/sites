July 10th, 2011: the original site has been gone since 2003, and this
mirror is a duplicate of sorts of
[the most recent archive.org mirror](http://web.archive.org/web/20031202211441/http://www.mines.edu/students/b/bolmstea/malbolge/).
This content is also
[mirrored by Lou Scheffer](http://www.lscheffer.com/malbolge.shtml), who has
some interesting stuff on the langauge too.

I’ve added additional links to the text.

Ben’s original interpreter is available for download here too as a
[ZIP file](malbolge.zip "Malbolge interpreter") and as a
[tarball](malbolge.tar.gz "Malbolge interpreter").

If you’re interested in Malbolge, you’d probably be interested in
[Dis](dis.html) too.

Malbolge ’98
============

[Ben Olmstead]{.author}

I hereby relenquish any and all copyright on this language,
documentation, and interpreter; Malbolge is officially public domain.

Introduction
------------

It was noticed that, in the field of esoteric programming languages,
there was a particular and surprising void: no programming language
known to the author was specifically designed to be difficult to program
in.

Certainly, there were languages which were difficult to write in, and
far more were difficult to read (see:
[Befunge](http://catseye.tc/projects/befunge93/),
[False](http://strlen.com/false-language), TWDL,
[RUBE](http://catseye.tc/projects/rube/)...). But even
[INTERCAL](http://www.catb.org/~esr/intercal/) and
[BrainF\*\*\*](http://www.muppetlabs.com/~breadbox/bf/), the two kings
of mental torment, were designed with other goals: INTERCAL to have
nothing in common with any major programming language, and BrainF\*\*\*
to be a very tiny, yet still Turing-complete, language.

INTERCAL’s constructs are certainly tortuous, but they are all too
flexible; you can, for instance, quite easily assign any number to a
variable with a single statement.

BrainF\*\*\* is lacking the flexibility which is INTERCAL’s major
weakness, but it fails in that its constructs are far, far too
intuitive. Certainly, there are only 8 instructions, none of which take
any arguments—but it is quite easy to determine how to use those
instructions. Subtract 8 from the current number? With a simple
`--------` you are done! This kind of simple answer was unacceptable to
the author.

Hence the author created Malbolge. It borrows from machine,
BrainF\*\*\*, and
[tri-INTERCAL](http://www.muppetlabs.com/~breadbox/intercal-man/s06.html),
but put together in a unique way. It was designed to be difficult to
use, and so it is. It is designed to be incomprehensible, and so it is.

So far, no Malbolge programs have been written. Thus, we cannot give an
example.

**Malbolge** is the name of Dante’s Eighth Circle of Hell, in which
practitioners of deception (seducers, flatterers, simonists, thieves,
hypocrites, and so on) spend eternity.

Environment
-----------

In many languages, the environment is easy to understand. In Malbolge,
it is best to understand the runtime environment before you ever see a
command.

The environment is, roughly, that of a primitive trinary CPU. Both code
and data share the same space (the machine’s memory segment), and there
are three registers. Machine words are ten trits (trinary digits) wide,
giving a maximum possible value of *59048* (all numbers are unsigned).
Memory space is exactly *59049 words long*.

The three registers are A, C, and D. A is the accumulator, used for data
manipulation. A is implicitly set to the value written by all write
operations on memory. (Standard I/O, a distinctly non-chip-level
feature, is done directly with the A register.)

C is the code pointer. It is automatically incremented after each
instruction, and points the instruction being executed.

D is the data pointer. It, too, is automatically incremented after each
instruction, but the location it points to is used for the data
manipulation commands.

All registers begin with the value 0.

When the interpreter loads the program, it ignores all whitespace. If it
encounters anything that is not one of an instruction and is not
whitespace, it will give an error, otherwise it loads the file, one non-
whitespace character per cell, into memory. Cells which are not
initialized are set by performing op on the previous two cells
repetitively.

Commands
--------

When the interpreter tries to execute a program, it first checks to see
if the current instruction is a graphical ASCII character (33 through
126). If it is, it subtracts 33 from it, adds C to it, mods it by 94,
then uses the result as an index into the following table of 94
characters:

    +b(29e*j1VMEKLyC})8&m#~W>qxdRp0wkrUo[D7,XTcA"lI
    v%{gJh4G\-=O@5`_3i<?Z';FNQuY]szf$!BS/|t:Pn6^Ha

It then checks it against the characters listed below, and performs an
appropriate action.

If the result is not one of the characters listed below, it is treated
as a nop. If the original character is not graphic ASCII, the program is
immediately ended.

When the interpreter parses the input file, it checks each
non-whitespace character with the process above. If any result is not
one of the eight characters below, the file will be rejected.

After the instruction is executed, 33 is subtracted from the instruction
at C, and the result is used as an index in the table below. The new
character is then placed at C, and then C is incremented.

    5z]&gqtyfr$(we4{WP)H-Zn,[%\3dL+Q;>U!pJS72FhOA1C
    B6v^=I_0/8|jsb9m<.TVac`uY*MK'X~xDl}REokN:#?G"i@

j
:   sets the data pointer to the value in the cell pointed to by the
    current data pointer.

i
:   sets the code pointer to the value in the cell pointed to be the
    current data pointer.

\*
:   rotates the trinary value of the cell pointed to by D to the
    right 1. The least significant trit becomes the most significant
    trit, and all others move one position to the left.

p

:   performs a tritwise ‘op‘ on the value pointed to by D with the
    contents of A. The op (don’t look for pattern, it’s not there) is:

               | A trit:
        _______|_0__1__2_
             0 | 1  0  0
         *D  1 | 1  0  2
        trit 2 | 2  2  1

        Di-trits:
            00 01 02 10 11 12 20 21 22

        00  04 03 03 01 00 00 01 00 00
        01  04 03 05 01 00 02 01 00 02
        02  05 05 04 02 02 01 02 02 01
        10  04 03 03 01 00 00 07 06 06
        11  04 03 05 01 00 02 07 06 08
        12  05 05 04 02 02 01 08 08 07
        20  07 06 06 07 06 06 04 03 03
        21  07 06 08 07 06 08 04 03 05
        22  08 08 07 08 08 07 05 05 04

&lt;
:   reads an ASCII value from the stdin and converts it to trinary, then
    stores it in A. 10 (line feed) is considered ‘newline’, and
    2222222222t (59048 dec.) is EOF.

/
:   converts the value in A to ASCII and writes it to stdout. Writing 10
    is a newline.

v
:   indicates a full stop for the machine.

o
:   does nothing, except increment C and D, as all other instructions
    do.

Turing-Completeness
-------------------

Though I have not proven it, I *think* Malbolge to be Turing-complete.
To be Turing-complete, there must be some data construct which can be
used to do any mathematical calculation. I believe that using \*p in
various clever ways on the tritwords can fulfill this requirement.

Turing-completeness also requires three code constructs: *sequential
execution* (which Malbolge obviously has), *repetition* (provided by the
i and, indirectly, j instructions), and *conditional-execution*
(provided, I believe, by self-modifying code and altering i
destinations).

I do have my doubts, particularly about data constructs, but I *think*
this works...

Appendix: Trinary Conversion Table
----------------------------------

Trinary to ASCII to decimal to hex table, provided, strangely enough,
for the convenience of Malbolge programmers.

    00000 NUL 000 00    01012   032 20    02101 @ 064 40    10120 ` 096 60
    00001 SOH 001 01    01020 ! 033 21    02102 A 065 41    10121 a 097 61
    00002 STX 002 02    01021 " 034 22    02110 B 066 42    10122 b 098 62
    00010 ETX 003 03    01022 # 035 23    02111 C 067 43    10200 c 099 63
    00011 EOT 004 04    01100 $ 036 24    02112 D 068 44    10201 d 100 64
    00012 ENQ 005 05    01101 % 037 25    02120 E 069 45    10202 e 101 65
    00020 ACK 006 06    01102 & 038 26    02121 F 070 46    10210 f 102 66
    00021 BEL 007 07    01110 ' 039 27    02122 G 071 47    10211 g 103 67
    00022 BS  008 08    01111 ( 040 28    02200 H 072 48    10212 h 104 68
    00100 HT  009 09    01112 ) 041 29    02201 I 073 49    10220 i 105 69
    00101 LF  010 0a    01120 * 042 2a    02202 J 074 4a    10221 j 106 6a
    00102 VT  011 0b    01121 + 043 2b    02210 K 075 4b    10222 k 107 6b
    00110 FF  012 0c    01122 , 044 2c    02211 L 076 4c    11000 l 108 6c
    00111 CR  013 0d    01200 - 045 2d    02212 M 077 4d    11001 m 109 6d
    00112 SO  014 0e    01201 . 046 2e    02220 N 078 4e    11002 n 110 6e
    00120 SI  015 0f    01202 / 047 2f    02221 O 079 4f    11010 o 111 6f
    00121 DLE 016 10    01210 0 048 30    02222 P 080 50    11011 p 112 70
    00122 DC1 017 11    01211 1 049 31    10000 Q 081 51    11012 q 113 71
    00200 DC2 018 12    01212 2 050 32    10001 R 082 52    11020 r 114 72
    00201 DC3 019 13    01220 3 051 33    10002 S 083 53    11021 s 115 73
    00202 DC4 020 14    01221 4 052 34    10010 T 084 54    11022 t 116 74
    00210 NAK 021 15    01222 5 053 35    10011 U 085 55    11100 u 117 75
    00211 SYN 022 16    02000 6 054 36    10012 V 086 56    11101 v 118 76
    00212 ETB 023 17    02001 7 055 37    10020 W 087 57    11102 w 119 77
    00220 CAN 024 18    02002 8 056 38    10021 X 088 58    11110 x 120 78
    00221 EM  025 19    02010 9 057 39    10022 Y 089 59    11111 y 121 79
    00222 SUB 026 1a    02011 : 058 3a    10100 Z 090 5a    11112 z 122 7a
    01000 ESC 027 1b    02012 ; 059 3b    10101 [ 091 5b    11120 { 123 7b
    01001 FS  028 1c    02020 < 060 3c    10102 \ 092 5c    11121 | 124 7c
    01002 GS  029 1d    02021 = 061 3d    10110 ] 093 5d    11122 } 125 7d
    01010 RS  030 1e    02022 > 062 3e    10111 ^ 094 5e    11200 ~ 126 7e
    01011 US  031 1f    02100 ? 063 3f    10112 _ 095 5f

    11202 128 80    12221 160 a0    21010 192 c0    22022 224 e0
    11210 129 81    12222 161 a1    21011 193 c1    22100 225 e1
    11211 130 82    20000 162 a2    21012 194 c2    22101 226 e2
    11212 131 83    20001 163 a3    21020 195 c3    22102 227 e3
    11220 132 84    20002 164 a4    21021 196 c4    22110 228 e4
    11221 133 85    20010 165 a5    21022 197 c5    22111 229 e5
    11222 134 86    20011 166 a6    21100 198 c6    22112 230 e6
    12000 135 87    20012 167 a7    21101 199 c7    22120 231 e7
    12001 136 88    20020 168 a8    21102 200 c8    22121 232 e8
    12002 137 89    20021 169 a9    21110 201 c9    22122 233 e9
    12010 138 8a    20022 170 aa    21111 202 ca    22200 234 ea
    12011 139 8b    20100 171 ab    21112 203 cb    22201 235 eb
    12012 140 8c    20101 172 ac    21120 204 cc    22202 236 ec
    12020 141 8d    20102 173 ad    21121 205 cd    22210 237 ed
    12021 142 8e    20110 174 ae    21122 206 ce    22211 238 ee
    12022 143 8f    20111 175 af    21200 207 cf    22212 239 ef
    12100 144 90    20112 176 b0    21201 208 d0    22220 240 f0
    12101 145 91    20120 177 b1    21202 209 d1    22221 241 f1
    12102 146 92    20121 178 b2    21210 210 d2    22222 242 f2
    12110 147 93    20122 179 b3    21211 211 d3
    12111 148 94    20200 180 b4    21212 212 d4
    12112 149 95    20201 181 b5    21220 213 d5
    12120 150 96    20202 182 b6    21221 214 d6
    12121 151 97    20210 183 b7    21222 215 d7
    12122 152 98    20211 184 b8    22000 216 d8
    12200 153 99    20212 185 b9    22001 217 d9
    12201 154 9a    20220 186 ba    22002 218 da
    12202 155 9b    20221 187 bb    22010 219 db
    12210 156 9c    20222 188 bc    22011 220 dc
    12211 157 9d    21000 189 bd    22012 221 dd
    12212 158 9e    21001 190 be    22020 222 de
    12220 159 9f    21002 191 bf    22021 223 df
