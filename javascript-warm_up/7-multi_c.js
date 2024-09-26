#!/usr/bin/node
String.prototype.repeat = String.prototype.repeat || function(n){
	n= n || 1;
	return Array(n+1).join(this);
}
console.log("C is fun \n".repeat(x))
