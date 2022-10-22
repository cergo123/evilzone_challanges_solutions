// Copy this and in the challange page
// Right click > inspect > console
// Paste this code and press enter
// You will get the flag
// Copy the flag fully starting from Encryption_3...


var d = '04 2f 22 33 38 31 35 28 2e 2f 1e 72 1e 32 2e 2d 34 35 28 2e 2f 1e 27 2d 20 26 1e 72 72 79 79 70 72 72 76'

// Parsing
d = d.trim().split('\n').map((x) => x.split(' ').map((x) => parseInt(x, 16)) );

// filter for ascii-only
d = d.filter((x) =>  !x.slice(1).some((y) => (x[0] ^ y)&0x80));

// Display
d.map((x) => {
    console.log(`%s\n\n`, x.join(' '));
    var hex = x.map((x) => (x > 15 ? '': '0') + x.toString(16)).join(' ');
    var str = [];
    // brute-force assuming the first character is upper-case
    for (var i= 0x40; i < 0x60; i++) {
        console.log('%s\n\n', x.join(' '));
        str.push(x.map((y) => String.fromCharCode(y ^ x[0] ^ i)).join(''));
    }

    // only keep strings that actually starts with upper-case characters
    str = str.filter((s) => /^[A-Z]/.test(s));
    console.log('%s\n\n', str.join(' '));

    // filter out escape codes (other than \n), including invalid characters (\u00XX)
    str = str.map((s) => JSON.stringify(s)).filter((s) => !/\\[^n]/.test(s));
    console.log(`%s\n\n`, hex);
    console.log(`%s\n\n`, str.join(' '));
    return hex + '\n' + str.join('\n');

}).join('\n\n')