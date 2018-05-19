#!/bin/bash

STRING="$(textToGithubEmoji $1)"
git commit -m $STRING
