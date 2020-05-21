---
url: download2
---

# Download Software

<a name="QK6Hj"></a>
# wget

```bash
wget -c ulr
```

支持断点续传


<a name="DowT6"></a>
# aria2c
website: [https://aria2.github.io/](https://aria2.github.io/)<br />install:
```bash
sudo apt-get install aria2
```
aria2 is a **lightweight** multi-protocol & multi-source command-line **download utility**. It supports **HTTP/HTTPS**, **FTP**, **SFTP**, **BitTorrent** and **Metalink**. aria2 can be manipulated via built-in **JSON-RPC** and **XML-RPC** interfaces.

<a name="JJbwG"></a>
## Examples

```bash
#Usage Examples
#Command-line scares you off? No, aria2 is really easy to use!!

#Download from WEB:
aria2c http://example.org/mylinux.iso

#Download from 2 sources:
aria2c http://a/f.iso ftp://b/f.iso

#Download using 2 connections per host:
aria2c -x2 http://a/f.iso

#BitTorrent:
aria2c http://example.org/mylinux.torrent

#BitTorrent Magnet URI:
aria2c 'magnet:?xt=urn:btih:248D0A1CD08284299DE78D5C1ED359BB46717D8C'

#Metalink:
aria2c http://example.org/mylinux.metalink

#Download URIs found in text file:
aria2c -i uris.txt
```

<a name="48Jvx"></a>
# curl
reference: [https://curl.haxx.se/docs/manpage.html](https://curl.haxx.se/docs/manpage.html)

curl is a tool to transfer data from or to a server, using one of the supported protocols (DICT, FILE, FTP, FTPS, GOPHER, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS, TELNET and TFTP). The command is designed to work without user interaction.

```bash
curl ftps://files.are.secure.com/secrets.txt
```

more tutorial: [https://curl.haxx.se/docs/manual.html](https://curl.haxx.se/docs/manual.html)
