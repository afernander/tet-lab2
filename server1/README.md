# EC2 Machine: `server1`

This file will explain how to use `server1`.

This server uses HTTP to work. The following resources are available:

## Resources
<hr>

**PATH.** `/`

**USAGE.** ```/?initValue=FLOAT&ir=FLOAT&months=INT```

**CONTENT-TYPE.** `text/plain`

**DESCRIPTION.** This generates the repayment table according to setted parameters.
- `initValue` is the initial capital of debt.
- `ir` is the monthly effective interest rate to apply.
- `months` is the total periods to pay.

**EXAMPLE.**

![command example](https://user-images.githubusercontent.com/52968530/129489979-fd2c6106-6598-4333-a204-990cd7f2e651.png)

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


