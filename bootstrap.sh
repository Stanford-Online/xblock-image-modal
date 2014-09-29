#!/bin/sh

TEMPLATE=./skel

echo 'OK GO' && \
    npm install -g grunt-cli && \
    npm install && \
    ./node_modules/grunt-init/bin/grunt-init "${TEMPLATE}" && \
    npm install && \
    grunt && \
    echo >> ./package.json && \
    git rm ./bootstrap.sh && \
    git rm -rf "${TEMPLATE}" && \
    git add --all . && \
    git commit -m "Fork XBlock from template" && \
echo 'ALL DONE'
