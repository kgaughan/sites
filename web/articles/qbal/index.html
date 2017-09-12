<!DOCTYPE html>

<html lang="en">
	<head>
		<title>Q-BAL Programming Language</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<link rel="stylesheet" type="text/css" href="/assets/stylesheet.css" media="all">
	</head>
	<body>

<h1>Q-BAL Programming Language</h1>

<p>Q-BAL is a programming language that Ben Yackley and Michael Shulman
invented on a whim, based on the question &ldquo;What would it be like if a
language were based on queues rather than stacks?&rdquo; The acronym stands for
Queue-BAsed Lanugage. This language is not designed to be useful, just fun.</p>

<h2 class="screen-only">How to Program in Q-BAL</h2>

<ol class="screen-only">
	<li><a href="#intro">Introduction</a>
		<ul>
			<li><a href="#queues">Introduction to Queues</a>
				<ul>
					<li><a href="#declqs">Declaring Queues of Numbers</a></li>
					<li><a href="#init">Initialization</a></li>
				</ul></li>
			<li><a href="#attach">Attachment</a>
				<ul>
					<li><a href="#attops">The Attachment Operators</a></li>
					<li><a href="#attwhat">What they do</a></li>
					<li><a href="#arith">Arithmetic</a></li>
					<li><a href="#logic">Logic</a></li>
				</ul></li>
			<li><a href="#assign">Assignment</a></li>
			<li><a href="#bscprfx">The Basic Prefix Operators</a>
				<ul>
					<li><a href="#preserve">The Preservation Operator (<code>*</code>)</a></li>
					<li><a href="#number">The Number Operator (<code>#</code>)</a></li>
				</ul></li>
			<li><a href="#null">The Use of the Null</a></li>
			<li><a href="#comments">Comments</a></li>
			<li><a href="#direct">Compiler/Interpreter Directives</a></li>
		</ul></li>
	<li><a href="#io">Input and Output</a>
	
		<ul>
			<li><a href="#stdinout">Stdin and Stdout</a>
				<ul>
					<li><a href="#inout">The Predefined Queues <code>in</code> and <code>out</code></a></li>
					<li><a href="#chrio">ASCII Character input and output</a></li>
					<li><a href="#longio">String and multiple number input and output</a></li>
				</ul></li>
			<li><a href="#vario">Variable Input and Output</a>
				 <ul>
					<li><a href="#ioq">The Predefined Variable I/O Queues</a></li>
					<li><a href="#ioinc">I/O include files</a></li>
				</ul></li>
		</ul></li>
	<li><a href="#progctrl">Program Control</a>
		<ul>
			<li><a href="#progcounter">The Program Counter</a></li>
			<li><a href="#execution">Program Execution</a></li>
			<li><a href="#relbranch">Relative Branching</a></li>
			<li><a href="#multithread">Multithreading</a></li>
			<li><a href="#endexec">Ending Execution</a></li>
			<li><a href="#linelabels">Line Labels</a></li>
		</ul></li>
	<li><a href="#introfunc">Introduction to Functions</a>
		<ul>
			<li><a href="#declfs">Declaring Functions</a></li>
			<li><a href="#initf">Initializing Functions</a></li>
			<li><a href="#fcode">The Code of a Function</a></li>
			<li><a href="#lvlop">The Higher-Level Prefix Operator</a></li>
			<li><a href="#fcall">Calling a Function</a></li>
		</ul></li>
	<li><a href="#advfunc">Advanced Functions</a>
		<ul>
			<li><a href="#io_ops">The Input/Output Override Prefix Operators</a></li>
			<li><a href="#static">Static Local Variables</a></li>
			<li><a href="#instq">The Instruction Queue</a>
				<ul>
					<li><a href="#codeprdf">The <code>code</code> Predefined Queue</a></li>
			   </ul></li>
			<li><a href="#oop">Object Oriented Programming in Q-BAL</a></li>
			<li><a href="#vario_func">Variable I/O and Functions</a>
				<ul>
					<li><a href="#files">File Handling</a></li>
				</ul></li>
			<li><a href="#static">Static Local Variables</a>
				<ul>
					<li><a href="#static_q">The <code>?</code> is Static</a></li>
					<li><a href="#dynalloc">Dynamic Allocation</a></li>
				</ul></li>
		</ul></li>
	<li><a href="#datatypes">Compound Data Types</a>
		<ul>
			<li><a href="#datawhat">What are compound data types?</a></li>
			<li><a href="#gcd">The &ldquo;Greatest Common Denominator&rdquo;</a></li>
			<li><a href="#dataioops">The Input/Output Override Prefix Operators Revisited</a></li>
			<li><a href="#vardata">Variable Data Types</a></li>
			<li><a href="#string">The String Prefix Operator</a></li>
			<li><a href="#diminish">The Diminish Prefix Operator</a></li>
		</ul></li>
</ol>

<h2 class="screen-only">Revisions since then</h2>

<ul class="screen-only">
<li><a href="revision.txt">Revision</a></li>
<li><a href="comment.txt">Comment by Andy</a></li>
</ul>

<h2 class="screen-only">Other versions</h2>

<ul class="screen-only">
<li><a href="specification.pdf" title="Q-BAL Specification in PDF format">PDF</a></li>
</ul>

<h1 id="intro">Introduction</h1>

<h2 id="queues">Introduction to Queues</h2>

<p>A Queue is a FIFO (First-In, First-Out) data structure, as opposed to a
LIFO (Last-In, First-Out) structure such as a stack. A queue is like a list,
or a line. The first one to get in line is the first to get out of line. The
items get removed from the top of the queue and entered at the bottom. As in
a stack, when something is taken off the top of a queue it is removed from
the queue (except when the preservation prefix operator is used&mdash;see
below).</p>

<p>All objects in Q-BAL are queues or functions. For now, we will just deal
with queues of numbers (see below for functions and compound data types). A
queue of numbers is a simple FIFO structure of integers (Q-BAL has no
floating point capacity as yet).</p>

<h3 id="declqs">Declaring Queues of Numbers</h3>

<p>An object is declared by a declaration statement, as follows:</p>

<pre>
Q <var>queue_name</var>
</pre>

<p>This declares a queue of numbers named <var>queue_name</var>. The name is
an alphanumeric sequence which can include letters, numbers, and underscores,
but cannot begin with a number. There is another part to the declaration: the
type. For now, the only type we'll be using is <code>Q</code>, meaning a queue of
numbers.</p>

<h3 id="init">Initialization</h3>

<p>A queue may be initialized to a certain list of numbers. This is done
using the <code>=</code> initialization operator and the <code>{ , }</code>
literal queue operators. An example follows:</p>

<pre>
Q squares = {1,4,9,16,25}
</pre>

<p>The first number inside the <code>{ , }</code> comes at the top of the
queue and the last comes at the bottom. Literal queues can also be used in
expressions and assignments (see below).</p>

<h2 id="attach">Attachment</h2>

<h3 id="attops">The attachment operators</h3>

<p>All non-declarations in Q-BAL are assignments or attachments. That is, all
statements that do not create a queue or function are classed as assignments
or attachments and are thus built around the assignment operator,
<code>=</code>, or one of the two attachment operators, <code>-&gt;</code>
and <code>&lt;-</code>. We will discuss attachment first.</p>

<p class="note"><strong>Note</strong>: Unicode character /u2192 (and /u2090
the other way) is a nice arrow. Unfortunately most computers are still
running on ASCII or ANSI so we are unable to type unicode characters in our
programs. :( Hence we use the two characters <code>-&gt;</code>.</p>

<p>Of the two attachment operators, the second is identical to the first
except with reversed arguments. That is to say, <code>x -&gt; y</code> is
equivalent to <code>y &lt;- x</code>.</p>

<p>It is a good idea to be consistent in which you use, unless for some
reason the clarity is improved by switching, or you are trying to confuse
people. The queue from which the arrow points is known as the source, and the
one to which it points is known as the destination. Attachment is also known
as appending, or &ldquo;sticking on the bottom.&rdquo;</p>

<h3 id="attwhat">What they do</h3>

<p>What the first attachment does is to pop the top of <var>x</var> and
append it to the bottom of <var>y</var>. That is, this code:</p>

<pre>
Q x = {1,2,3}
Q y = {4,5,6}
x -&gt; y
y -&gt; x
</pre>

<p>will end up with <code>x = {2,3,4}</code> and <code>y =
{5,6,1}</code>.</p>

<h3 id="arith">Arithmetic</h3>

<p>Arithmetic may be performed on the number after it is popped and before it
is attached. More than one number may be popped off the same or different
queues and arithmetic may be performed on them. Reading from left to right in
an expression, numbers are popped off queues in the order they appear. This
is important if more than one number is to be popped off one queue in an
expression. One queue can appear on both the source and destination sides,
such as in the attachment <code>x + 1 -&gt; x</code>, which serves as an
increment if <var>x</var> is a one-element queue.</p>

<p>The arithmetic operators are <code>+</code>, <code>-</code>,
<code>/</code>, <code>\</code>, <code>|</code>, and <code>^</code>. Of these,
<code>+</code> adds, <code>-</code> subtracts, <code>/</code> finds the
quotient, <code>|</code> finds the remainder, <code>\</code> multiplies (the
opposite of division, naturally), and <code>^</code> exponentiates. Remember,
these are all integer operators. The parenthesis operators, <code>(</code>
and <code>)</code>, are used to separate operations and override the natural
order of operations (which is <code>^</code> <code>\</code> <code>/</code>
<code>|</code> <code>+</code> <code>-</code>). They are also often used for
clarity.</p>

<h3 id="logic">Logic</h3>

<p>The traditional logical operators may also be applied. They return 1 if
true and 0 if not true. They are used in program control (see program
counter, below). They are <code>==</code>, <code>&lt;</code>,
<code>&gt;</code>, <code>&lt;=</code> or <code>=&lt;</code>,
<code>&gt;=</code> or <code>=&gt;</code>, <code>!=</code>, and <code>!</code>
(logical NOT turns nonzero into zero and zero into one).</p>

<h2 id="assign">Assignment</h2>

<P>The assignment sets one queue <em>equal</em> to another. It does
not modify the source queue (the one on the right), but the destination queue
is completely overwritten by the source queue. An example will
illustrate:</p>

<pre>
Q x = {1,2,3}
Q y = {4,6}
y = x
</pre>

<p>This example produces <code>x = {1,2,3}</code> and <code>y =
{1,2,3}</code>. As it shows, the assignment operator does not care about how
many elements are in the destination queue. There is no &ldquo;flipped&rdquo; form of the
assignment operator as there is with the attachment operators; the left is
always the destination and the right is always the source.</p>

<h2 id="bscprfx">The Basic Prefix Operators</h2>

<p>Prefix operators are an important part of Q-BAL. For the most part they
control access to a queue or force different types of access to a queue. They
have higher precedence than any other operators and are evaluated from inside
to outside.</p>

<h3 id="preserve">The Preservation Operator (<code>*</code>)</h3>

<p>The preservation operator returns the top element of a queue without that
element being removed from the queue.</p>

<h3 id="number">The Number Operator (<code>#</code>)</h3>

<p>The number operator returns the number of elements in the queue it is
applied to. It is often used by functions to determine if they have enough
arguments to execute (see functions, below).</p>

<h3 id="otherprefix">Other Prefix Operators</h3>

<p>The <code>&amp;</code>, <code>@</code>, <code>~</code>, and <code>:</code>
operators really only have meaning when used with functions and will be
discussed in that section. The <code>$</code> and <code>%</code> operators
only have meaning when used with different data types and will be discussed
in that section.</p>

<h2 id="null">The Use of the Null</h2>

<p>In either an attachment or assignment, either the source or the
destination (or theoretically both, but this would be useless) may be left
blank. This is called the &ldquo;null queue.&rdquo; The null queue is never modified and
is considered to have no elements. Here are the possible combinations:</p>

<pre>
x -&gt;
-&gt; x
x =
= x
</pre>

<p>Of these, the fourth is the only one with no use whatever. The first pops
an element from <var>x</var> and discards it, and the third erases
<var>x</var> completely (i.e. makes it a null queue.). The second does
nothing to <var>x</var> if it is a queue, but if <var>x</var> is a function
it makes the function&rsquo;s code execute without storing anything in the input
queue (see functions, below).</p>

<h2 id="comments">Comments</h2>

<p>A comment is, as in any programming language, a statement ignored by the
compiler/interpreter. The sole function of comments is to make the program
more readable to the programmer and anyone else. In Q-BAL all characters
between a backquote (<code>`</code>) and carriage return/linefeed are
considered comments and ignored by the compiler or interpreter.</p>

<h2 id="direct">Compiler/Interpreter Directives</h2>

<p>As in other languages (especially C) the programmer in Q-BAL can instruct
the compiler or interpreter in certain ways. In Q-BAL any line
<em>beginning</em> in a period (<code>.</code>) is considered a directive.
There must be one letter after the period designating what type of directive
it is, then a space and any parameters required by the directives. At the
time this is being written there are only three directives:</p>

<pre>
.I "included.qbl"
.P ;-1 -&gt; ;
.M print 'out?
</pre>

<p>The first tells the compiler/interpreter to include a specified file at
that point. The pathname can be relative or absolute. The second changes the
end-of-line statment from the default <code>;+1 -&gt; ;</code> to anything
the programmer specifies. (We'll find out about <code>;</code> and program
control later.) The third creates a macro, like C's <code>#define</code>
statement. Macros and other predefined objects are generally made with ALL
CAPS.</p>

<h1 id="io">Input and Output</h1>

<h2 id="stdinout">Stdin and Stdout</h2>

<h3 id="inout">The Predefined Queues <code>in</code> and
<code>out</code></h3>

<p>Input and output to stdin and stdout&mdash;that is, from the keyboard or to
the screen&mdash;are handled by a group of predefined queues. The simplest of
the group are <code>in</code> and <code>out</code>. <code>in</code> can only
be a source and <code>out</code> can only be a destination. Numerical input
and output is handled with attachments, as follows:</p>

<pre>
Q x
in -&gt; x
x + 1 -&gt; x
x -&gt; out
</pre>

<p>This will input a number, add one to it, and output it in numerical
format. Note that at the end of this code snippet <var>x</var> is a null queue again
(has no elements).</p>

<h3 id="chrio">ASCII Character input and output</h3>

<p>Character ASCII values can be input and output with the <code>'in</code>
and  <code>'out</code> predefined queues. <code>'in</code> reads a character
from stdin, and <code>'out</code> outputs a character to stdout, in much the
same way as before. They both convert to or from ASCII values, because queues
only store numbers.</p>

<h3 id="longio">String and multiple number input and output</h3>

<p>So far we have only read one number or character at a time. But input and
output would be tedious indeed if this were the only way. (Not that that
would have stopped us from leaving it at that if it were in any way difficult
to engineer longer input and output, however.) However, we can use the
assignment operator rather than the attachment operators. Therefore, this
code:</p>

<pre>
Q x
x = 'in
'out = x
</pre>

<p>will read a string from stdin until return is pressed and output it to
stdout. Note that at the end of this code snippet <var>x</var> still contains the
string, as the assignment operator does not modify the source.
<code>in</code> and <code>out</code> are most often used with attachment,
while <code>'in</code> and <code>'out</code> are most often used with
assignment, but either can be used with either.</p>

<h3 id="litstr">Literal Strings</h3>

<p>The double quotes <code>&quot;</code> are the literal string operator. A literal string
such as <code>&quot;This is a string&quot;</code> is equivalent to the queue
of the ASCII values of the characters in the string (which, for the example,
is a 16-element queue).</p>

<h2 id="vario">Variable Input and Output</h2>

<p>The predefined queues <code>in</code>, <code>out</code>, <code>'in</code>, and
<code>'out</code> pretty much cover the
keyboard and the screen (stdin and stdout). However, those are not the only
sources of input and output that a program will want to utilize. Q-BAL
provides variable input and output for those who want to use other sources of
input and directions of output.</p>

<h3 id="ioq">The Predefined Variable I/O Queues</h3>

<p>The Variable I/O system introduces five new predefined queues. They are
<code>?</code>, <code>in?</code>, <code>out?</code>, <code>'in?</code>, and
<code>'out?</code>. The first, represented by a single question mark, is a
queue of all the sources and destinations the programmer may want to use. It
begins the program as a null queue, and while it is a null queue the use of
the other four will cause an error to be generated. Variable I/O is
initialized by putting a number (usually defined by the <code>.M</code> directive to be a
descriptive word) into the queue <code>?</code> as follows:</p>

<pre>
PRINTER -&gt; ?
</pre>

<p>Assuming that earlier in the program there was a <code>.M PRINTER x</code>
statement, where <var>x</var> is whatever number the compiler/interpreter decides
represents the printer, this statement initializes the variable I/O queues.
The other four variable I/O queues function exactly like their standard I/O
counterparts except that they input from and output to only whatever area is
listed at the top of the <code>?</code> queue.</p>

<h3 id="ioinc">I/O include files</h3>

<p>You may have noticed that the last section was rather vague on what
numbers represent which sources of input and destinations for output. This is
because the representation is dependent on the compiler/interpreter. Luckily,
the compiler/interpreter is required to provide include files (usually <kbd>.inc</kbd>
or <kbd>.qbi</kbd>) which include the neccessary <code>.M</code> statements for common devices such
as printers, mice, modems, etc. Also sure to be included are library
functions which handle these devices, so that it is generally unneccessary to
access them directly. (Don&rsquo;t worry, we&rsquo;ll get to functions in a bit.)</p>

<h1 id="progctrl">Program Control</h1>

<h2 id="progcounter">The Program Counter</h2>

<p>There are no if, then, while, for, etc. loops or even a goto statement in
Q-BAL. Program control is handled by explicitly manipulating the program
counter, a predefined queue represented by a semicolon (<code>;</code>). The
program counter normally has one element in it, representing a line number
(after all <code>.I</code> inclusions: see below), starting from 1 at the first line.
Blank lines and comments are not counted. So the following line:</p>

<pre>
0 -&gt; ;
</pre>

<p>Will reset program execution to the beginning of the program. But in
reality, it is never necessary to know the exact line number of any given
line. Labels and relative branching are usually sufficient, as we will
discover later.</p>

<h2 id="execution">Program Execution</h2>

<p>You may have been wondering why the code snippet in the previous section
was <code>0 -&gt; ;</code> and not <code>1 -&gt; ;</code>. Normally, program
execution follows this pattern: The compiler/interpreter compiles/interprets
the command at the line number at the top of the program counter, then
executes the statement <code>;+1 -&gt; ;</code> and repeats. If not
disturbed, therefore, execution will begin at line one (since <code>; =
{1}</code> at the start) and continue through the program one line at a time.
Therefore you must always set the program counter to the number one less than
the line number you want to branch to.</p>

<h2 id="relbranch">Relative Branching</h2>

<p>To imitate if, while, for, etc. statements, we only need to be able to say
&ldquo;go back <var>x</var> lines if such-and-such is true.&rdquo; This is done
by multiplying <var>x</var> by
the result of a logic operation, which is 0 if false and 1 if true. The code
snippet</p>

<pre>
Q x
in -&gt; x
; - 2 \ (x != 0) -&gt; ;
</pre>

<p>illustrates this concept, and will get input repeatedly until the number 0
is entered. Remember that after the line the statement <code>;+1 -&gt;
;</code> is executed, so you must set <code>;</code> to the line number one before the
line number of the line you want execution to jump to.</p>

<h2 id="multithread">Multithreading</h2>

<p>Very rarely, you may want to put two numbers into the program counter.
This will cause execution to jump back and forth between two areas of the
program, executing one statement, then another at a completely different
address, then the statement after the first, then the one after the second,
and so on.</p>

<h2 id="endexec">Ending Execution</h2>

<p>Program execution can be stopped by the statement <code>; -&gt;</code> if
there is only one number in the <code>;</code> queue or <code>; =</code> if there are more
(except from inside a function as noted below. From inside a function these
statements return from the function, and <code>:; -&gt;</code> is required to
end execution.). The compiler/interpreter will assume the program is over if
there is no more code, so this statement is not really necessary. (A function
will also return without it at the end of the code.)</p>

<h2 id="linelabels">Line Labels</h2>

<p>As anyone who has programmed in primitive BASIC will know, it can be
extremely cumbersome to have to know line numbers in order to control program
flow. Fortunately, it is possible to &ldquo;label&rdquo; a line in Q-BAL, although (like
so many other things in Q-BAL) it is not designed directly into the language.
Consider this code:</p>

<pre>
Q LABEL
...
LABEL = ;
...
; = LABEL
</pre>

<p>The first statement functions as the &ldquo;label,&rdquo; storing the program counter
value (i.e. line number) at that point. It does not modify the program
counter. The second statement reassigns that line number to the program
counter, causing execution to jump to the line just after the label. Voila!
And all without knowing what that line number is. Note that the second
statement does not modify the queue <code>LABEL</code>, allowing it to be used again and
again.</p>

<h1 id="introfunc">Introduction to Functions</h1>

<h2 id="whatis">What is a Function?</h2>

<p>A function is the only other object type in Q-BAL, besides the queue. We
will start with functions on numbers, as we did with queues of numbers. A
function is composed of three elements: an input queue, an output queue, and
an instruction queue.</p>

<p>A function is <em>called</em> (although that term is not usually used in Q-BAL)
whenever an object is placed on its input queue. This is normally done by
treating the function name as if it were a queue name and attaching something
to it. When this occurs, a <em>sub-program-counter</em> is invoked and the
instruction queue of the function activates.</p>

<h2 id="declfs">Declaring Functions</h2>

<p>A function on numbers is declared in the same way as a queue of numbers,
except with an <code>F</code> instead of a <code>Q</code> for the type, as
follows:</p>

<pre>
F <var>func_name</var>
</pre>

<p>The same restrictions on the name of a function apply as on the name of a
queue.</p>

<h2 id="initf">Initializing Functions</h2>

<p>The instruction queue of a function is the only part that can be
initialized. It is done as follows:</p>

<pre>
F square
 Q x
 *in -&gt; x
 x \ in -&gt; x
 x -&gt; out
F
</pre>

<p>Don&rsquo;t worry about what that function does; we&rsquo;ll get to that in the next
section.</p>

<h2 id="fcode">The Code of a Function</h2>

<p>Any statement valid outside a function is valid inside a function, and
some others as well, with a few modifications. When the program counter is
referred to inside a function, it refers to the function&rsquo;s
sub-program-counter. When the predefined queues <code>in</code> or
<code>out</code> are referred to, they refer to the input and output queues
of the function. For this reason, one can attach to <code>in</code> or read
from <code>out</code>, although it is considered bad form in most cases. A
function can declare its own local variables, but they are reinitialized
every time the function executes (see advanced functions for how to prevent
this).</p>

<h2 id="lvlop">The Higher-Level Prefix Operator
(<code>:</code>)</h2>

<p>The higher-level prefix operator, when used inside a function, forces the
name to refer to the object of the same name <em>outside</em> the function.
For example, <code>:;</code> inside a function will refer to the original
program counter, while <code>:in</code> will refer to stdin rather than the
function&rsquo;s input queue.</p>

<h2 id="fcall">Calling a Function</h2>

<p>Whenever the name of a function is used on the source side of an
expression it refers to the output queue, and is treated as if it were a
normal queue. Whenever it is used as the destination, it refers to the input
queue, and again is treated as a normal queue.</p>

<h1 id="advfunc">Advanced Functions</h1>

<h2 id="io_ops">The Input/Output Override Prefix Operators
(<code>&amp;</code> and <code>@</code>)</h2>

<p>From outside the function, it is possible to store to the output or read
from the input. It is generally considered bad form to do so, but is
sometimes neccessary. This is done with the Input/Output Override prefix
operators. The <code>&amp;</code> operator forces use of the input queue, and
the <code>@</code> operator forces use of the output queue. When the <code>&amp;</code>
operator is used to store to the input queue (even if it would not be
necessary) the function's code does <em>not</em> execute. Execution can then
be forced later by storing a null queue to the function.</p>

<h2 id="instq">The Instruction Queue</h2>

<p>Remember that a function consists of <em>three</em> queues? An input
queue, an output queue, and an instruction queue? Well, the instruction queue
isn&rsquo;t called a queue for nothing. You can manipulate it just like any other
queue, as long as you use the instruction queue override prefix
(<code>~</code>). Statments are enclosed in brackets <code>[]</code> to keep
them as one item, but otherwise can be treated just like numbers (except that
you can&rsquo;t do arithmetic with them, of course). The ability to manipulate the
instruction queue can create very interesting self-modifying code. See
Compound Data Types for examples of how this can be used.</p>

<h3 id="codeprdf">The <code>code</code> Predefined Queue</h3>

<p>There is another predefined queue, like <code>in</code> and
<code>out</code>. It is <code>code</code> and it refers to the instruction
queue of the current function, just as <code>in</code> and <code>out</code>
refer to the input and output queues of a given function. In the main
program, it refers to the main instruction queue.</p>

<h2 id="oop">Object Oriented Programming in Q-BAL</h2>

<p>OOP (Object Oriented Programming) can be done in Q-BAL, but it is
primitive compared to other languages such as C++. Then again, Q-BAL is not a
object-oriented language, so it&rsquo;s surprising that you can do it at all.
It&rsquo;s really a consequence of the capabilities of functions, and not a real
designed capability of the language.</p>

<p>A function can act as an object. If it needs to store &ldquo;member variables&rdquo;
it can do so in a static local variable (see above). The instruction queue
can be set to do different things depending on how many arguments are put in
the input queue at the same time (or even what type of argument: see variable
data types, below), thus acting as different functions. Data can also be
stored in the output queue. One function can be assigned to another of the
same data type, replacing the target&rsquo;s instruction queue, input queue, and
output queue.</p>

<h2 id="vario_func">Variable I/O and Functions</h2>

<p>Since each function has its own <code>in</code> and <code>out</code>
queues, it stands to reason that it would also have the corresponding
variable I/O queues, and this is in fact the case. Each function has its own
of all five variable I/O queues, and they function exactly the same as in the
main program. Furthermore, if a function&rsquo;s <code>?</code> queue is nonempty,
then input to the device it specifies is considered input to the function and
will cause execution of the instruction queue. In this way, Q-BAL can create
an event-driven program. For this purpose, there is a stdin handle that can
be stored to <code>?</code>, even though the main program does not require
it. Stdin can be accessed from a function through <code>:in</code> but this
will not cause function execution. Also note that in order for this to work,
the <code>?</code> queue is static; that is, unchanged between function
calls.</p>

<h3 id="files">File Handling</h3>

<p>File handling is done through variable I/O, but since the programmer needs
to tell the computer what file to open before I/O is possible, it is handled
through a function rather than a macro, and now that we know all about
functions, we can cover it. <code>FILE</code> is a predefined function which
takes as input a string which is the filename, with either a local or global
path. If the filename does not exist, <code>FILE</code> will create it. It
then returns a &ldquo;file handle&rdquo; which can be stored to <code>?</code>, allowing
I/O to that file. File I/O using <code>FILE</code> is sequential and
appending. That is, if <code>?={<var>filehandle</var>}</code>, then
attachments from <code>in?</code> read one character at a time from the top
of the file, sending an EOF when the file is over, and attachments to
<code>out?</code> append characters to the end of the file. Assignments from
<code>in?</code> read one line at a time, and assignments to
<code>out?</code> write one line at a time (as is standard with I/O queues).
There are also other miscellanous file-handling predefined functions such as
<code>FQ DELETE</code>, which takes a queue of files to delete.</p>

<h2 id="static">Static Local Variables</h2>

<p>Functions can declare local variables, in the normal manner of variable
declaration, but these variables do not keep their values when the function
is called multiple times. Many functions can get around this by keeping
values on the input or output queues, but sometimes this isn&rsquo;t sufficient,
especially for OOP-like functions. One way to get around this is by declaring
a queue outside the function that is only used from inside that function, but
this is cumbersome.</p>

<h3 id="static_q">The <code>?</code> is Static</h3>

<p>Each function has its own <code>?</code> queue which remains unchanged
from calling to calling, like a static variable. It is therefore possible to
store single values in the <code>?</code> queue between function callings, as
long as the function does not utilize variable I/O. This is dangerous,
however, because if the number stored happens to be the handle for some
device, then the function may be inadvertently called by input to that
device.</p>

<h3 id="dynalloc">Dynamic Allocation</h3>

<p>There is yet another area that variable I/O can handle: dynamic allocation
of memory. C or C++ programmers will be familiar with this concept. To
dynamically allocate memory for an object (of <em>any</em> data type), use
the function <code>F ALLOC</code>. This function takes as input a string
indicating the data type of the desired object (for example,
<code>"FQQ"</code>) and outputs a handle that can be stored to a
<code>?</code> queue. When this handle is on top of the <code>?</code> queue,
then the variable I/O queues access the dynamically created object.
<code>in?</code> functions exactly like <code>&amp;x</code> and <code>out?</code>
exactly like <code>@x</code>, for an object named <var>x</var>. The queues
<code>'in?</code> and <code>'out?</code> are not well defined when
<code>?</code> holds the handle of a dynamic variable. When a function
dynamically creates variables, they are static because their handle
(presumably in the <code>?</code> queue) is also static. This is the best way
for a function to create static variables.</p>

<h1 id="datatypes">Compound Data Types</h1>

<h2 id="datawhat">What are compound data types?</h2>

<p>There are other types of queues and functions in Q-BAL than queues of
numbers and functions on numbers. There are queues of queues, or functions on
queues, or queues of functions. These are declared with a variable number of
<code>Q</code>s and <code>F</code>s for the type section of a declaration.
For example, <code>FQ sort</code> would declare a function on queues. In
general, a &ldquo;queue&rdquo; or &ldquo;function&rdquo; refers to a queue of numbers or a function
on numbers. An example of a use of a queue of queues follows:</P>

<pre>
QQ x
Q y
y = 'in
*$y -&gt; x
; - 3\(#y != 0) -&gt; ;
$x -&gt; 'out
; - 2\(#x != 0) -&gt; ;
; -&gt;
</pre>

<p>This complete program will read strings until a null string is entered
(return with no other characters), and then print them all out in the same
order they were entered, followed by a blank line. (Don&rsquo;t worry about
understanding it now; we&rsquo;ll refer back to it as we go on.)</p>

<h2 id="gcd">The &ldquo;Greatest Common Denominator&rdquo;</h2>

<p>When an assignment or attachment includes different data types, the
&ldquo;Greatest Common Denominator Rule&rdquo; is used to determine how the data is
manipulated. The GCD of two types is the largest string of <code>Q</code>s
and <code>F</code>s that is common to both, on the right side. In the case of
attachment, the GCD must be shorter in length than the shorter of the two
types, while in assignment it can be equal to the shorter. The GCD is the
longest data type that is manipulated. For any data type, if the GCD is more
than one letter shorter than the type in question (if the operation is
attachment) or if it is at all shorter (if the operation is assignment), then
the excess is put onto the top of the queue (or the output queue for
functions.) An example will serve to make this clearer:</p>

<pre>
FQQ x
QQ y
FQ z
...
y -&gt; x
y = x
z = y
y -&gt; z
x -&gt; z
</pre>

<p>Admittedly, you aren&rsquo;t likely to run across anything nearly this complex.
But it serves a good illustration. Let&rsquo;s take this in order. The first three
statements declare <var>x</var> a function on queues of queues,
<var>y</var> a queue of queues, and <var>z</var> a function on queues.
The fourth line is an ellipsis, indicating that there is probably code in
between, but what it is doesn&rsquo;t matter. Now we&rsquo;re at the confusing part.</p>

<p>The first attachment has a GCD of <code>Q</code> (it would be
<code>QQ</code>, but an attachment GCD must be shorter than the shortest,
which in this case is <code>QQ</code>). Therefore it works on queues. It pops
the first queue off <var>y</var> (<var>y</var> is a queue of queues) and
appends it to&mdash;what? Well, excess is put onto the output queue, so it
appends it to the top queue of queues on the output queue of <var>x</var>,
which is a function on queues of queues.</p>

<p>The second statement is an assignment with a GCD of <code>QQ</code>. It
sets <var>y</var> (a queue of queues) equal to the top queue of queues in
the output queue of <var>x</var> (a function on queues of queues) without
popping it off <var>x</var>.</p>

<p>The third statement is an assignment with a GCD of <code>Q</code>. It sets
the top of the output queue of <var>z</var> (a function on queues) equal to
the top of <var>y</var> (a queue of queues) without popping it off
<var>y</var>.</p>

<p>The fourth statement is an attachment with a GCD of <code>Q</code> working
the same way between the same variables as the third statement. This one pops
the top queue off <var>y</var> (a queue of queues) and appends it to the
bottom of the input queue of <var>z</var> (a function on queues).</p>

<p>The fifth statement is an attachment with a GCD of <code>Q</code>. It pops
the top queue off the top queue of queues of the output queue of
<var>x</var> (a function on queues of queues) and appends it to the bottom
of the input queue of <var>z</var> (a function on queues).</p>

<p>Got it? Good!</p>

<h2 id="dataioops">The Input/Output Override Prefix Operators Revisited</h2>

<p>Remember the I/O override operators <code>&amp;</code> and <code>@</code> from
advanced functions? They can apply to multiple data types as well. Normally,
excess is put on the top, or the top of the output queue, but these can force
it to be put on the bottom, or on the input queue. To this end, they can be
applied to queues as well as functions. When used in this way to functions,
sometimes they must be applied twice. The default is <code>@</code> or
<code>@@</code>, the top of the output queue. <code>&amp;</code> or
<code>&amp;&amp;</code> will force it to the bottom of the input queue.
<code>&amp;@</code> will force the bottom of the output queue, and
<code>@&amp;</code> the top of the input queue. Needless to say, these are
generally considered bad form. But hey; who cares?</p>

<h2 id="vardata">Variable Data Types</h2>

<p>An object may be declared as a type ending in <code>X</code>, such as
<code>QX</code> or <code>FQX</code>. The <code>X</code> stands for
&ldquo;anything&rdquo;. <code>QX</code> means a queue of anything, and
<code>FQX</code> means a function on queues of anything. When used in an
expression, consider the <code>X</code> by default to be whatever will make
the GCD the longest. If two <code>X</code>-types are used in the same
expression, make both the <code>X</code>s equal to whatever is at the top of
the source.</p>

<h2 id="string">The String Prefix Operator (<code>$</code>)</h2>

<p>The String prefix operator <code>$</code> forces the GCD to a higher
level. One use of the string on the source will raise an attachment to the
level of the smaller, if possible. For example:</p>

<pre>
QQ x
Q y
...
$y -&gt; x
</pre>

<p>This code will leave <var>y</var> a null queue and append to
<var>x</var> (a queue of queues) what it used to be. The string operator
often leaves its operand a null queue. When used other than this, it causes
things to be strung together. For example:</p>

<pre>
Q x
Q y
...
$x -&gt; y
</pre>

<p>This code will string together all of <var>x</var> and append it to
<var>y</var>. If <code>x = {1,2,3}</code> and <code>y = {1,4,9}</code>,
then after this code executes <code>y = {1,4,9,1,2,3}</code> and
<var>x</var> is a null queue. In general, be logical: it&rsquo;s usually pretty
obvious what the string operator should do in any given situation.</p>

<h2 id="diminish">The Diminish Prefix Operator (<code>%</code>)</h2>

<p>The Diminish Prefix Operator <code>%</code> is the opposite of the string
operator. It lowers the GCD by one letter. It is even more intuitive than the
string operator and needs no example.</p>

</body></html>
