<!DOCTYPE html>

<html lang="en"><head>

<title>RFC: system.multicall (XML-RPC)</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="keywords" content="xml-rpc, multicall, system.multicall">
<link rel="stylesheet" type="text/css" href="../assets/stylesheet.css" media="all">

</head><body>

<div class="host-note">
<p>January 2nd, 2010: I pulled this article from <a href="http://web.archive.org/web/20060824100531/http://www.xmlrpc.com/discuss/msgReader$1208">its archive.org cache</a>. <a href="http://www.xmlrpc.com/discuss/msgReader$1208">Its original location</a> appears to be permanently broken, so I&rsquo;ve mirrored it for posterity. &mdash;K.</p>
</div>

<h1>RFC: system.multicall</h1>

<p class="source">Originally posted by <a href="http://www.xmlrpc.com/profiles/$11" class="author">Eric Kidd</a> on <span class="published">2001-01-25 31:34:52</span></p>

<p>After speaking with Adrian Likins at RedHat, I&rsquo;ve been thinking about ways to boxcar XML-RPC calls without changing the official specification.</p>

<h2>What&rsquo;s &lsquo;boxcarring&rsquo;?</h2>

<p>Basically, it involves packing multiple, asynchronous function calls into one big request, and shipping them all off to the server at once.</p>

<h2>Why would anybody want to do this?</h2>

<p>HTTP round-trip latency ranges from bad to awful. So it can be much faster to make one big request than ten little ones.</p>

<p>Also, some people want to use XML-RPC to script local applications. They need to perform one context-swap per request, which can really kill throughput. Again, it would be much better to make one big request than ten little ones.</p>

<h2>Can&rsquo;t you do this with HTTP pipelining?</h2>

<p>In theory, who knows? In practice, no. I spent this afternoon watching pipelined HTTP requests on the wire, and they appear to require at least one round-trip TCP packet per XML-RPC function call. If you&rsquo;ve got a 250 millisecond ping between your sites, that means a half-second per XML-RPC call. Period.</p>

<p>(And if the W3C&rsquo;s own reference code can&rsquo;t do any better than this, then you can safely assume that none of us mere mortals will ever figure it out.)</p>

<h2>But you can&rsquo;t change the XML-RPC specification!</h2>

<p>I know. I don&rsquo;t want to patch all the clients, either. So let&rsquo;s look for a different solution.</p>

<h2>The Proposal</h2>

<pre>
array system.multicall(array)
</pre>

Takes an array of XML-RPC calls encoded as structs of the form (in a Pythonish notation here):<p>

<pre>
{ 'methodName': string, 'params': array }
</pre>

<p>The array of structs may be of any length. In particular, empty lists are supported, so clients can test for the presence of the function without performing any actions.</p>

<p>Returns an array of responses. There will be one response for each call in the original array. The result will either be a one-item array containing the result value (this mirrors the use of <code>&lt;params&gt;</code> in <code>&lt;methodResponse&gt;</code>), or a struct of the form found <em>inside</em> the standard <code>&lt;fault&gt;</code> element.  (Please see the <a href="#example">example</a> below.)</p>

<p>If some items in the original call array are not valid call structs (as described above), the implementation must return a struct-with-fault-information in the corresponding response position. Under no circumstances may the implementation return a list of the wrong length.</p>

<p>To prevent stack overflow attacks against compiled XML-RPC servers, <code>system.multicall</code> <em>may</em> refuse to process recursive calls to itself.</p>

<p>Of course, <code>system.multicall</code> may return a fault of its own, using the normal XML-RPC fault mechanism. This probably means it that <code>system.multicall</code> isn&rsquo;t implemented, and you&rsquo;ll have to send all your requests in the normal fashion.</p>

<h2>Virtues</h2>

<ul>
<li>We haven&rsquo;t changed the XML-RPC specification.</li>
<li>We haven&rsquo;t required any heavy HTTP wizardry.</li>
<li>If a given XML-RPC library doesn&rsquo;t support this automatically, developers can provide it themselves. I&rsquo;m betting this is less than twenty lines of Python.</li>
<li>Clients can test for the presence of <code>system.multicall</code> either by using <code><a href="http://xmlrpc-c.sourceforge.net/introspection.html">system.listMethods</a></code> or by calling <code>system.multicall</code> with an empty list.</li>
<li>Smart XML-RPC libraries can do all the work behind the scenes.</li>
</ul><p>

<h2><a id="example">An Example</a></h2>

<p>This example uses a Python-like notation to represent XML-RPC values. If you have any questions about what the corresponding XML looks like, please ask.</p>

<p>A sample argument to <code>system.multicall</code>:</p>

<pre>
[{ 'methodName': 'system.add', 'params': [2, 2] },
 { 'methodName': 'test.nonexistant', 'params': [1] },
 { 'methodName': 'system.multicall', 'params': [] },
 { 'methodName': 'system.multicall' },
 'this is not a struct',
 { 'methodName': 'system.add', 'params': [4, 4] }]
</pre>

<p>The return value:</p>

<pre>
[[4],
 { 'faultCode': 123, 'faultString': 'No such method test.nonexistant' },
 { 'faultCode': 456, 'faultString': 'Recursive system.multicall forbidden' },
 { 'faultCode': 789, 'faultString': 'Missing params' },
 { 'faultCode': 987, 'faultString': 'system.multicall expected struct' },
 [8]]
</pre>

<p>Notice that regular return values are always nested inside a one-element array.  This allows you to return structs from functions without confusing them with faults.</p>

<p>The fault codes and fault strings used in the above example are arbitrary.</p>

<h2>Implementations</h2>

<p>A transparent, server-side implementation of <code>system.multicall</code> is available in the CVS version of <a href="http://xmlrpc-c.sourceforge.net/">xmlrpc-c</a>.</p>

<p>Thank you for any feedback on this proposal!</p>

<p>Cheers,<br>
Eric</p>

  </body>
</html>
