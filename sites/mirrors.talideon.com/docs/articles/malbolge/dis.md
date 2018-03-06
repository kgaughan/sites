Ben’s original interpreter is available for download here too as a
[ZIP file](dis.zip "Dis interpreter") and as a
[tarball](dis.tar.gz "Dis interpreter").
If you’re interested in Dis, you’d probably be interested in
[Malbolge](spec.html) too.
{: .host-note }

Dis ’98
=======

Ben Olmstead

I hereby relenquish any and all copyright on this language,
documentation, and interpreter; Dis is officially public domain.

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

Hence the author created [Malbolge](spec.html). It was meant to be a
nightmare to write in, and it was.

But the author soon discovered that, try as he had, the only program he
had successfully written in Malbolge was one which printed ’666‘ and
aborted. He had succeeded in his quest far too well.

This was a problem.

He thought upon this for many hours, slept a bit, had some dinner,
freaked out a Principles of Programming Languages professor, and came
back to the problem at hand.

He examined Malbolge, and came to a decision: he would split the
evolution in twain. Malbolge proper would become even more of a
nightmare (for, though he had not consciously realized it, he had used a
certain, albeit tiny, amount of restraint when creating Malbolge), while
he would create another language which was—just barely—humanly possible
to use. After pulling out his copy of The Divine Comedy again, he
decided to call this ‘lesser’ branch **Dis**, after the capital city of
Hell, at the heart of which lies Malbolge. Dis, literally, means
‘Satan’.

Environment
-----------

In many languages, the environment is easy to understand. In Dis, it is
best to understand the runtime environment before you ever see a
command.

The environment is, roughly, that of a primitive trinary CPU. Both code
and data share the same space (the machine’s memory segment), and there
are three registers. Machine words are ten trits (trinary digits) wide,
giving a maximum possible value of *59048* (all numbers are unsigned).
Memory space is exactly *59049 words long*.

The three registers are the A, C, and D. A is the accumulator, used for
data manipulation. A is implicitly set to the value written by all write
operations on memory. (Standard I/O, a distinctly non-chip-level
feature, is done directly with the A register.)

C is the code pointer. It is automatically incremented after each
instruction, and points the instruction being executed.

D is the data pointer. It, too, is automatically incremented after each
instruction, but the location it points to is used for the data
manipulation commands.

All registers begin with the value 0.

When the interpreter loads the program, it ignores all whitespace
(including comments). If it encounters anything that is not one of
`!{}|^>_*` and is not whitespace, it will give an error, otherwise it
loads the file, one non-whitespace character per cell, into memory. All
uninitialized cells are set to 0.

Commands
--------

This mythical Dis CPU supports seven instructions; all are equivalent to
the ASCII codes of punctuation characters. Unsupported instructions are
treated as no-ops.

\*
: sets the data pointer to the value in the cell pointed to by the current
  data pointer.

^
: sets the code pointer to the value in the cell pointed to be the current
  data pointer.

>
: rotates the trinary value of the cell pointed to by D to the right 1.
  The least significant trit becomes the most significant trit, and all
  others move one position to the left.

|
: performs a tritwise ‘op’ on the value pointed to by D with the contents
  of A. The op is *Tritwise Subtract Without Borrow* and is:

```nohighlight
	 |   A
_____|_0_1_2_
   0 | 0 1 2
*D 1 | 2 0 1
   2 | 1 2 0
```

}
: reads an ASCII value from the stdin and converts it to Trinary, then
  stores it in A. 10 (line feed) is considered ‘newline’, and 2222222222t
  (59048 dec.) is EOF.

{
: converts the value in A to ASCII and writes it to stdout. Writing 10 is
  a newline. If the value 2222222222t (EOF) is written, program execution
  is instantly terminated.

!
: indicates a full stop for the machine.

\_
: Used to explicitly place a nop instruction (of value 95 decimal) in the
  source file. This is the only major difference between the original
  Malbolge and Dis.

Turing-Completeness
-------------------

Though I have not proven it, I believe Dis to be Turing-complete. To be
Turing-complete, there must be some data construct which can be used to
do any mathematical calculation. I believe that using `|>` in various
clever ways on the tritwords, while using `*_` to manipulate D, can
fulfill this requirement.

Turing-completeness also requires three code constructs: sequential
execution (which Malbolge obviously has), repetition (provided by the ^
and, indirectly, \* instructions), and conditional-execution (provided,
I believe, by self-modifying code and altering ^ destinations).

But, of course, I cannot be certain unless I prove it, and I fear that
Dis’ tortuous syntax is too much for me to overcome to create a proof.

Appendix: Trinary Conversion Table
----------------------------------

Trinary to ASCII to decimal to hex table, provided, strangely enough,
for the convenience of Dis programmers.

```nohighlight
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
01011 US  031 1f    02100 ? 063 3f    10112 _ 095 5f    11201 . 127 7f

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
```
