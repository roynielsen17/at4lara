---
id: 01JHGPET1VPYBY2C3VHEJVCFM9
created: 2025-01-13T13:42
updated: 2025-01-20T17:10
modified: 2025-01-17T08:46:55-07:00
---

C create
R read
U update
D delete

Like all devices, it will take a data model structure (defined by the Model README), and address and instruction and the device controller will act on that information to manipulate a concrete CRUD device, if it is available.  The data models may be passed between devices may include JSON as a first data schema and later possibly YAML.

There may be a possibility for an option to perform a write through to a default CRUD device.  Also if the intended device is not available (ie network down).  Definitely not initial target features.

Initial CRUD devices would include Filesystem and Database devices.
