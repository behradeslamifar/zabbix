#!/bin/sh

domain=$1
port=$2

if [ -z "$port" ]
then
	port=443
fi

expire=$(openssl s_client -connect "$domain:$port" -servername "$domain" </dev/null 2>/dev/null| openssl x509 -in /dev/stdin -noout -text | grep "Not After" |sed -n 's/ *Not After : *//p' | xargs -I{} date '+%s' --date "{}")

now=$(date +"%s")

expiry=$(( "$expire - $now" ))

echo $expiry

exit 0
