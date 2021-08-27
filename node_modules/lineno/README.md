# lineno [![NPM version][npm-image]][npm-url] [![Build Status][travis-image]][travis-url] [![Build Status][appveyor-image]][appveyor-url]

Get the current line number.

## Insall

Install with [npm](https://www.npmjs.com/)

```
npm install lineno
```

## Usage

```js
const Lineno = require('lineno');

const lineno = new Lineno(__filename);

console.log(lineno.get()); // print the current line number

console.log(lineno.filename); // print the file path
```

## APIs

### lineno.get() => number

returns the current line number.

### Lineno.filename => string

is the file path specified as a constructor argument.


## License

Copyright (C) 2016 Takayuki Sato

This program is free software under [MIT](https://opensource.org/licenses/MIT) License.
See the file LICENSE in this distribution for more details.


[npm-image]: http://img.shields.io/badge/npm-v0.1.0-blue.svg
[npm-url]: https://www.npmjs.org/package/lineno
[travis-image]: https://travis-ci.org/sttk/lineno.svg?branch=master
[travis-url]: https://travis-ci.org/sttk/lineno
[appveyor-image]: https://ci.appveyor.com/api/projects/status/github/sttk/lineno?branch=master&svg=true
[appveyor-url]: https://ci.appveyor.com/project/sttk/lineno

