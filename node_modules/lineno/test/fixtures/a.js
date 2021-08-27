const path = require('path');

const Lineno = require(path.resolve(__dirname, '../../'));
const lineno = new Lineno(__filename);

var lno = lineno.get();

module.exports = { lineno:lno  };
