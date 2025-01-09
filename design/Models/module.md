---
id: 01JGM4FZBFYFM27TMXGAS1Q0TD
created: 2025-01-02T11:29
updated: 2025-01-09T11:15
modified: 2025-01-09T11:15:08-07:00
---

## What will the module contain

### One controller core, if necessary....

### Devices, Possibly
Together (device controller):
   * controller
   * State machine
   * I/O

Class : Group Purpose (may be multiple layers, or concrete instances)

picture that goes into the design more in depth: [VonNeumannDesignPatternDiagram_20kView](VonNeumannDesignPatternDiagram_20kView.drawio)

prototype deviceController class:  [deviceController](deviceController.py)

What kind of validation for a device?

methods = dir(class)

"""
methods:
 * Check that all the methods defined in the interface exist in the concrete class (no private methods allowed, protected allowed: single underscore - as of 1/9/25, not supported.
 * Check that all the methods in the extended interface device class exist in the concrete device class
instance variables - Check that instance variables are correct - like: 
 * deviceControllerID within appropriate range
 * deviceClassID's within appropriate range
 * deviceID's are within appropriate range. (CRUD)
 * concreteDeviceID (FS/DB - which one included) within range, and matches deviceID(CRUD) and deviceClassID and deviceControllerID
 * if main controller exists, it's ID is valid
 """ 





