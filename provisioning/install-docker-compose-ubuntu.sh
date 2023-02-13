#!/bin/bash

wget https://github.com/docker/compose/releases/download/v2.15.1/docker-compose-linux-x86_64
mv docker-compose-linux-x86_64 docker-compose
chmod +x docker-compose
mv docker-compose /usr/libexec/docker/cli-plugins
