# Weblogs.Com XML-RPC interface

NOTE: This mirror exists because weblogs.com is no more.

## What is Weblogs.Com? 

Weblogs.Com is a Web application that tracks changes to news-oriented websites. It was launched in late 1999, when XML-RPC was quite young and there weren't many weblogs. Today XML-RPC is widely deployed, and the weblog community has grown from a few hundred sites to many thousands.

To meet the growth, we've designed and are deploying a new mechanism for tracking updates to weblogs. This page explains the XML-RPC mechanism for updates.

```
weblogUpdates.ping(weblogname, weblogurl, changesurl=weblogurl, categoryname="none") returns struct
```

To tell Weblogs.Com that a weblog has changed, call `weblogUpdates.ping` on `rpc.weblogs.com`, port 80, path `/RPC2`.

It takes two required parameters, both strings, and two optional parameters, also strings. The first is the name of the weblog, the second is its URL. The third, `changesurl`, is the url of a page to be checked for changes. The fourth, `categoryname`, is the name of a category of pings, allowing the weblogs.com interface to be used to track RSS feeds, European weblogs, or whatever.

We read the weblog to determine if it has changed, therefore the weblog must already be updated when you call `weblogUpdates.ping`.

It returns a struct that indicates success or failure. It has two elements, `flerror` and `message`. If `flerror` is `false`, it worked. If it's `true`, message contains an English-language description of the reason for the failure.

If the call succeeds, the weblog will appear in `changes.xml`.

## Request and Response 

Here's an example of a call and a response. 

```
POST /RPC2 HTTP/1.0
User-Agent: Radio UserLand/7.1b7 (WinNT)
Host: rpc.weblogs.com
Content-Type: text/xml
Content-length: 250
	
<?xml version="1.0"?>
<methodCall>
  <methodName>weblogUpdates.ping</methodName>
  <params>
    <param>
      <value>Scripting News</value>
    </param>
    <param>
      <value>http://www.scripting.com/</value>
    </param>
  </params>
</methodCall>
	
HTTP/1.1 200 OK
Connection: close
Content-Length: 333
Content-Type: text/xml
Date: Sun, 30 Sep 2001 20:02:30 GMT
Server: UserLand Frontier/7.0.1-WinNT
	
<?xml version="1.0"?>
<methodResponse>
  <params>
    <param>
      <value>
        <struct>
          <member>
            <name>flerror</name>
            <value>
              <boolean>0</boolean>
            </value>
          </member>
          <member>
            <name>message</name>
            <value>Thanks for the ping.</value>
          </member>
        </struct>
      </value>
    </param>
  </params>
</methodResponse>
```
