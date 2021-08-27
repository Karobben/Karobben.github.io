var reg = /(\s*)(```) *(graphviz) *\n?([\s\S]+?)\s*(\2)(\n+|$)/g;

function ignore(data) {
  var source = data.source;
  var ext = source.substring(source.lastIndexOf('.')).toLowerCase();
  return ['.js', '.css', '.html', '.htm'].indexOf(ext) > -1;
}

function getId(index) {
  return 'graphviz-' + index;
}

exports.render = function(data) {
  if (!ignore(data)) {

    var graphviz = [];

    data.content = data.content
      .replace(reg, function(raw, start, startQuote, lang, content, endQuote, end) {
        var graphvizId = getId(graphviz.length);
        graphviz.push(content);
        return start + '<div id="' + graphvizId + '"></div>' + end;
      });

    if (graphviz.length) {
      var config = this.config.graphviz;
      // resources
      data.content += '<script src="' + config.vizjs + '"></script>';
      data.content += '<script src="' + config.render + '"></script>';
      data.content += graphviz.map(function(code, index) {
        var graphvizId = getId(index);
        var codeId = graphvizId + '-code';
        return '' +
          '{% raw %}' +
          '<textarea id="' + codeId + '" style="display: none">' + code + '</textarea>' +
          '<script>' +
          '  var viz = new Viz();' +
          '  var code = document.getElementById("' + codeId + '").value;' +
          '  viz.renderSVGElement(code)' +
          '  .then(function(element) {' +
          '    document.getElementById("' + graphvizId + '").append(element)' +
          '  });' +
          '</script>' +
          '{% endraw %}';
      }).join('');
    }
  }
};
