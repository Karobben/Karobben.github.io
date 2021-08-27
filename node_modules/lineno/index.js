const path = require('path');

var Lineno = function(filename) {
  Constructor.prototype = Lineno.prototype;
  return new Constructor(filename);

  function Constructor(filename) {
    this.filename = filename;
    this.get = _constructorOpt;
  }

  function _constructorOpt() {
    var original = Error.prepareStackTrace;
    Error.prepareStackTrace = _prepareStackTrace;
    var error = {};
    Error.captureStackTrace(error, _constructorOpt);
    var lno = error.stack;
    Error.prepareStackTrace = original;
    return lno;
  }

  function _prepareStackTrace(error, structuredStackTrace) {
    var lno = -1;
    for (var i=0, n=structuredStackTrace.length; i<n; i++) {
      var st = structuredStackTrace[i];
      if (st.isEval()) {
        if (lno < 0) { lno = st.getLineNumber(); }
        if (st.getEvalOrigin().indexOf('(' + filename + ':') >= 0) {
          break;
        }
      } else if (st.getFileName() === filename) {
        lno = st.getLineNumber();
        break;
      } else if ( // for 'load'
          (st.getFunctionName() == null) &&
          (st.getMethodName() == null) &&
          (path.basename(filename) === st.getFileName())) {
        lno = st.getLineNumber();
        break;
      }
    }
    return lno;
  }
};

module.exports = Lineno;
