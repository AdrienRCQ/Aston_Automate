#!/bin/bash
echo "Reload Systemd in progress"


sudo systemctl daemon-reload
sudo systemctl enable aston_automate-backend.service
sudo systemctl enable aston_automate-frontend.service
sudo systemctl start aston_automate-backend.service
sudo systemctl start aston_automate-frontend.service

echo "Reload is over !!!"