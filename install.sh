#!/bin/bash

docker compose build
chmod +x track.sh
ln -s $(pwd)/track.sh /usr/local/bin/track
docker compose up -d
