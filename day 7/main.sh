#!/bin/bash

for itm in $(grep '\->' input.txt | awk '{print $1}'); do if [ "$(grep -c $itm input.txt)" -eq "1" ]; then echo $itm; fi; done
