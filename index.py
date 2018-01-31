#!/usr/bin/python3

import imgsrch

print("Creating instance")
e = imgsrch.Engine()

print("Read")
e.read("engine.xml")

print("Index collection")
e.indexDirectory("dataset")

print("Write")
e.write("engine_index.xml")

