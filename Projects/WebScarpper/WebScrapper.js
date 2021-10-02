const request = require('request');
const cheerio = require('cheerio'); //node Scrapper.js

request("Put URL here", cb);

function cb(error, response, html) {
    if (error) {
        console.error('error:', error);
    } else {
        handlehtml(html);

    }
}
function handlehtml(html) {
    let selTool = cheerio.load(html);

    let contentArr = selTool("Put Identifier here");

    for (let i = 0; i < contentArr.length; i++) {
        let data = selTool(contentArr[i]).text();
        console.log(data);

    } }