January 2nd, 2010: I pulled this article from
[its archive.org cache](http://web.archive.org/web/20060824100531/http://www.xmlrpc.com/discuss/msgReader$1208).
[Its original location](http://www.xmlrpc.com/discuss/msgReader$1208)
appears to be permanently broken, so I’ve mirrored it for posterity. —K.
{: .host-note }

RFC: system.multicall
=====================

Originally posted by
[Eric Kidd](http://www.xmlrpc.com/profiles/$11)
on 2001-01-25 13:34:52
{: .source }

After speaking with Adrian Likins at RedHat, I’ve been thinking about
ways to boxcar XML-RPC calls without changing the official
specification.

What’s ‘boxcarring’?
--------------------

Basically, it involves packing multiple, asynchronous function calls
into one big request, and shipping them all off to the server at once.

Why would anybody want to do this?
----------------------------------

HTTP round-trip latency ranges from bad to awful. So it can be much
faster to make one big request than ten little ones.

Also, some people want to use XML-RPC to script local applications. They
need to perform one context-swap per request, which can really kill
throughput. Again, it would be much better to make one big request than
ten little ones.

Can’t you do this with HTTP pipelining?
---------------------------------------

In theory, who knows? In practice, no. I spent this afternoon watching
pipelined HTTP requests on the wire, and they appear to require at least
one round-trip TCP packet per XML-RPC function call. If you’ve got a 250
millisecond ping between your sites, that means a half-second per
XML-RPC call. Period.

(And if the W3C’s own reference code can’t do any better than this, then
you can safely assume that none of us mere mortals will ever figure it
out.)

But you can’t change the XML-RPC specification!
-----------------------------------------------

I know. I don’t want to patch all the clients, either. So let’s look for
a different solution.

The Proposal
------------

```nohighlight
array system.multicall(array)
```

Takes an array of XML-RPC calls encoded as structs of the form (in a
Pythonish notation here):

```json
{ 'methodName': string, 'params': array }
```

The array of structs may be of any length. In particular, empty lists
are supported, so clients can test for the presence of the function
without performing any actions.

Returns an array of responses. There will be one response for each call
in the original array. The result will either be a one-item array
containing the result value (this mirrors the use of `<params>` in
`<methodResponse>`), or a struct of the form found *inside* the standard
`<fault>` element. (Please see the [example](#example) below.)

If some items in the original call array are not valid call structs (as
described above), the implementation must return a
struct-with-fault-information in the corresponding response position.
Under no circumstances may the implementation return a list of the wrong
length.

To prevent stack overflow attacks against compiled XML-RPC servers,
`system.multicall` *may* refuse to process recursive calls to itself.

Of course, `system.multicall` may return a fault of its own, using the
normal XML-RPC fault mechanism. This probably means it that
`system.multicall` isn’t implemented, and you’ll have to send all your
requests in the normal fashion.

Virtues
-------

-   We haven’t changed the XML-RPC specification.
-   We haven’t required any heavy HTTP wizardry.
-   If a given XML-RPC library doesn’t support this automatically,
    developers can provide it themselves. I’m betting this is less than
    twenty lines of Python.
-   Clients can test for the presence of `system.multicall` either by
    using `system.listMethods` or by calling `system.multicall` with an
    empty list.
-   Smart XML-RPC libraries can do all the work behind the scenes.

An Example {#example}
----------

This example uses a Python-like notation to represent XML-RPC values. If
you have any questions about what the corresponding XML looks like,
please ask.

A sample argument to `system.multicall`:

```json
[{ 'methodName': 'system.add', 'params': [2, 2] },
 { 'methodName': 'test.nonexistant', 'params': [1] },
 { 'methodName': 'system.multicall', 'params': [] },
 { 'methodName': 'system.multicall' },
 'this is not a struct',
 { 'methodName': 'system.add', 'params': [4, 4] }]
```

The return value:

```json
[[4],
 { 'faultCode': 123, 'faultString': 'No such method test.nonexistant' },
 { 'faultCode': 456, 'faultString': 'Recursive system.multicall forbidden' },
 { 'faultCode': 789, 'faultString': 'Missing params' },
 { 'faultCode': 987, 'faultString': 'system.multicall expected struct' },
 [8]]
```

Notice that regular return values are always nested inside a one-element
array. This allows you to return structs from functions without
confusing them with faults.

The fault codes and fault strings used in the above example are
arbitrary.

Implementations
---------------

A transparent, server-side implementation of `system.multicall` is
available in the CVS version of
[xmlrpc-c](http://xmlrpc-c.sourceforge.net/).

Thank you for any feedback on this proposal!

Cheers, Eric
