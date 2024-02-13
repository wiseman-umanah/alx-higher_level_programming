#!/usr/bin/node
const Rectangle = require("./4-rectangle");

class Square extends Rectangle{
	constructor(size){
		super()
		this.width = size
		this.height = size
	}
	charPrint(c=null){
		let i, j
		if (c === null){
			c = "X"
		}
		for (i = 0; i < this.height; i++){
			for(j = 0; j < this.width; j++)
				process.stdout.write(c)
			console.log("")
		}
	}
}

module.exports = Square