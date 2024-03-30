#!/bin/bash 

set -e 
echo "Deployment Started..." 
cd yourfolder
git pull

composer install
npm install
npm run build
php artisan migrate --force
php artisan optimize
echo "Deployment Finished"