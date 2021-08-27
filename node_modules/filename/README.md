# [filename](https://github.com/hex7c0/filename)

[![NPM version](https://img.shields.io/npm/v/filename.svg)](https://www.npmjs.com/package/filename)
[![Linux Status](https://img.shields.io/travis/hex7c0/filename.svg?label=linux-osx)](https://travis-ci.org/hex7c0/filename)
[![Windows Status](https://img.shields.io/appveyor/ci/hex7c0/filename.svg?label=windows)](https://ci.appveyor.com/project/hex7c0/filename)
[![Dependency Status](https://img.shields.io/david/hex7c0/filename.svg)](https://david-dm.org/hex7c0/filename)
[![Coveralls](https://img.shields.io/coveralls/hex7c0/filename.svg)](https://coveralls.io/r/hex7c0/filename)

Tiny module for get script filename

## Installation

Install through NPM

```bash
npm install filename
```
or
```bash
git clone git://github.com/hex7c0/filename.git
```

## API

inside nodejs script
```js
var filename = require('filename');

var name = filename();
// equal
var name = filename(__filename);
```

### filename([path])

#### path

 - `path` - **String** Path to normalize *(default "module.parent.filename")*

## Examples

Take a look at my [examples](examples)

### [License GPLv3](LICENSE)
