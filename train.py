#!/usr/bin/python3

import imgsrch

print("Creating instance")
e = imgsrch.Engine(5, 8)

print("Train kmeantree")
e.train("dataset", 3000000)

print("Index collection")
e.indexDirectory("dataset")

print("Write")
e.write("engine.xml")

print("Done")
