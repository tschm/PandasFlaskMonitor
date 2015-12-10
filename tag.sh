#!/bin/bash
VERSION=v6.0
git tag -a ${VERSION} -m 'version ${VERSION}'
git push --tags
