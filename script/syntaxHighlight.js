const hljs = require('highlight.js');

const code = process.argv[2];
const highlight = hljs.highlight(code, { language: 'python' }).value;
console.log(highlight);