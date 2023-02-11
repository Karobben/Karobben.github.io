var assign = require('deep-assign');
var renderer = require('./lib/renderer');

hexo.config.graphviz = assign({
  vizjs: 'https://unpkg.com/viz.js@2.1.2/viz.js',
  render: 'https://unpkg.com/viz.js@2.1.2/full.render.js',
}, hexo.config.graphviz);

hexo.extend.filter.register('before_post_render', renderer.render, 9);
