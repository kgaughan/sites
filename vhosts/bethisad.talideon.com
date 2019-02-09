server {
	include common_params;
	include ssl_params;
	include letsencrypt_params;

	server_name bethisad.talideon.com;
	root /home/freebsd/sites/bethisad.talideon.com/web;
	index index.html index.htm;

	ssl_certificate /usr/local/etc/ssl/acme/talideon.com/fullchain.pem;
	ssl_certificate_key /usr/local/etc/ssl/acme/private/talideon.com.pem;

	access_log /var/log/www/other/bethisad.talideon.com.access.log combined;
	error_log /var/log/www/other/bethisad.talideon.com.error.log;
}
