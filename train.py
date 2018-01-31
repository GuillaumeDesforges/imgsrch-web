#!/usr/bin/python3

import imgsrch

print("Creating instance")
e = imgsrch.Engine(5, 4)

print("Train kmeantree")
e.train("dataset", 150000)

print("Index collection")
e.indexDirectory("dataset")

print("Write")
e.write("engine_5_4_150000.xml")

print("Done")
