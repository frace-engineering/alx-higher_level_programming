#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request(process.argv[2]).pip(fs.createWriteStream(process.argv[3]));
