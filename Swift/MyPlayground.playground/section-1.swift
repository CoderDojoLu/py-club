// Playground - noun: a place where people can play

import UIKit
import Metal

var str = "Hello, playground"
var myButton = UIButton()

var myURL = NSURL(string: "https://www.circl.lu/index.html")

if myURL != nil {
    myURL!.lastPathComponent
}

myURL?.lastPathComponent

if let myOtherURL = NSURL(string: "http://localhost.lu/index.html") {
    myOtherURL.lastPathComponent
}

myButton.setTitle("New title", forState: .Normal)

myButton.currentTitle!
myButton.currentTitleColor

