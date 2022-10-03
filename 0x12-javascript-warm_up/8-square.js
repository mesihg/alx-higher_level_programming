#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    let stringX = '';
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      stringX += 'X';
    }
    console.log(stringX);
  }
}
