# tilde.club hosts

## What is this?

Just a hosts file. @reppep is [rightfully suspicious of it](https://github.com/tildeclub/tilde.hosts/issues/1).

The vague idea I (@ftrain) have going on is that if
you want to be a tilde.club peer you tell us the name of your server
and the IP address. Every server in the network would mirror this
file. This is how early Unix machines wired up to each other in the
days before DNS.

## What now?

I dunno. If you want to be a peer of tilde.club then you could add
your IP here? Nothing is implemented. I'm just putting it here as a
kind of placeholder for some things to figure out later.

## host-gen.py
The host-gen.py script can be used to dynamically recreate the hosts file. It will create a new file called host-data in the current directory, which should be manually verified prior to overwriting the existing /etc/hosts file.
