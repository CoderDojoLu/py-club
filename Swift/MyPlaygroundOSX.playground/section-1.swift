// Playground - noun: a place where people can play

import Cocoa

var str = "Hello, playground"

if str == "Hello, playground" {
    println("foo")
}

str.lastPathComponent
str.uppercaseString
str.lowercaseString

var words = str.componentsSeparatedByString(" ")


var obj : AnyObject

obj = NSDate()

obj.dateByAddingTimeInterval(3600)

obj = NSColor(red: 1, green: 0, blue: 0, alpha: 1)
obj.greenComponent

if obj is NSDate {
    println("Yay it is")
    obj.dateByAddingTimeInterval(360014)
}
