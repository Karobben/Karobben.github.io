'use strict';
/**
 * @file filename main
 * @module filename
 * @subpackage main
 * @version 0.4.0
 * @author hex7c0 <hex7c0@gmail.com>
 * @copyright hex7c0 2014
 * @license GPLv3
 */

/*
 * initialize module
 */
var basename = require('path').basename;
var extname = require('path').extname;

/*
 * functions
 */
/**
 * options setting
 * 
 * @exports filename
 * @function filename
 * @param {String} path - path
 * @return {String}
 */
function filename(path) {

  var p = path || module.parent.filename;
  return basename(p, extname(p));
}
module.exports = filename;
