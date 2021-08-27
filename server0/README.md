# EC2 Machine: `server0`

This file will explain how to use `server0`.

This server uses HTTP to work. The following resources are available:

## Resources
<hr>

**PATH.** `/`

**USAGE.** ```/?value=FLOAT&actualIrType=STR&newIrType=STR```

**CONTENT-TYPE.** `text/plain`

**DESCRIPTION.** This resource changes interest rate type for another one
- `value_%` is the interest rate percentage value (number only).
- `actualIrType` is the actual type of interest rate. The possible values are: EM, EA, NMV, NAV.
- `newIrType` is the target type of interest rate. The possible values are: EM, EA, NMV, NAV.

**EXAMPLE.**


<hr>

**PATH.** `/help`

**USAGE.** `/help`

**CONTENT-TYPE.** `text/plain`

**DESCRIPTION.** This returns the server available resources (and how to use it).

<hr>

**PATH.** `/ping`

**USAGE.** `/ping`

**CONTENT-TYPE.** `text/plain`

**DESCRIPTION.** This tests the server connection.

<hr>
