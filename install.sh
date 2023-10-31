#!/bin/bash

SHELL_PROFILE=""

if [ "$SHELL" == "/bin/bash" ]; then
    SHELL_PROFILE="$HOME/.bashrc"
elif [ "$SHELL" == "/bin/zsh" ]; then
    SHELL_PROFILE="$HOME/.zshrc"
else
    echo "Unsupported shell. Please manually set the TRACKER_PROJECT_DIR variable in your shell profile."
    exit 1
fi

if ! grep -q "export TRACKER_PROJECT_DIR=" $SHELL_PROFILE; then
    echo "export TRACKER_PROJECT_DIR=\"$(pwd)\"" >> $SHELL_PROFILE
fi
source $SHELL_PROFILE
echo $SHELL_PROFILE

docker compose build
chmod +x track.sh

if [[ ":$PATH:" != *":/usr/local/bin:"* ]]; then
    echo "export PATH=$PATH:/usr/local/bin" >> $SHELL_PROFILE
    source $SHELL_PROFILE
fi
ln -s $(pwd)/track.sh /usr/local/bin/track

docker compose up -d
