# nagios-telemetry-plugin

## Install

The following steps assume you already have an existing Nagios environment setup and will describe how to install the plugin only. These instructions are to be installed on each Nagios client.

1. `apt-get install -y python`
2. `sudo pip install -r requirements.txt`
3. Place telemetry.py in `/usr/lib/nagios/plugins`
3. Edit `/usr/local/nagios/etc/commands.cfg`

Some example commands:

`command[check_cpu_times]=/usr/lib/nagios/plugins/telemetry.py --cpu_times user`
`command[check_virtual_memory]=/usr/lib/nagios/plugins/telemetry.py --virtual_memory total`

4. `service xinetd restart`
5. Define the new command in /etc/nagios/objects/commands.cfg

`define command{
        command_name    telemetry
        command_line    $USER1$/check_nrpe -H $HOSTADDRESS$ -c telemetry
        }`

These instructions are done on the Nagios monitoring server:

1. Define a new service in `/usr/local/nagios/etc/services.cfg`

```
define service{
        use                     generic-service
        host_name               grokA
        service_description     Perf data
        check_command           check_nrpe!check_cpu_times!--cpu_times!user

}

define service {
        use                     generic-service
        host_name               grokA
        service_description     Virtual Memory total
        check_command           check_nrpe!check_virtual_memory!--virtual_memory!total
}
```

## Usage

`python telemetry --help`
