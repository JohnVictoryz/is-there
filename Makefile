install: src/isthere-exec-linux
	cp src/isthere-exec-linux /usr/bin/
	mv /usr/bin/isthere-exec-linux /usr/bin/isthere
	chmod +x /usr/bin/isthere
	echo "Done!"
