<?php
// -*- coding: utf-8 -*-
// (c) 2016 Andreas Motl <andreas@terkin.org>
/*
======================================
Kotori telemetry demo program for PHP4
======================================

Documentation
-------------
https://getkotori.org/docs/handbook/acquisition/runtime/php.html#demo


Synopsis
--------
Run demonstration program from the command line::

    # Send fixed measurements "temperature" => 42.84, "humidity" => 83 for demonstration purposes
    php4 -f terkin-demo.php4 run demo

    # Send a periodic, slowly oscillating sawtooth signal
    php4 -f terkin-demo.php4 run sawtooth

*/

// Put this file into the folder of your PHP program
include("terkin-http.php4");

// When running from the command line, use some example programs
// for submitting telemetry data for demonstration purposes.
if (php_sapi_name() == "cli") {

    $telemetry = new TelemetryNode(
        "http://localhost:24642/api",
        array(
            "realm"     => "mqttkit-1",
            "network"   => "testdrive",
            "gateway"   => "area-42",
            "node"      => "node-1",
        )
    );

    if ($argc > 2) {
        $command = $argv[1];
        $subcommand = $argv[2];
    }

    if ($command == "run") {

        if ($subcommand == "demo") {
            // Emit single sample of a sawtooth signal
            $data = array("temperature" => 42.84, "humidity" => 83);
            var_dump($telemetry->transmit($data));

        } else if ($subcommand == "sawtooth") {
            //date_default_timezone_set("Europe/Berlin");
            // Emit sample of a sawtooth signal each second, periodically
            while (true) {
                $data = array("second" => intval(strftime("%S")));
                var_dump($telemetry->transmit($data));
                sleep(1);
            }
        }
    }

}
?>
