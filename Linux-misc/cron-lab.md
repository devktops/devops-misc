# CRONTAB

## Lab for crontab scheduling

### 1. Create a file with the following content
```bash
#!/bin/bash
DATESTRING=$(date +%Y%m%d-%H%M%S)
CONTENTS="Writing message to file at $DATESTRING"
FILENAME="/home/ubuntu/lab/output/message-$DATESTRING.txt"
echo $CONTENTS > $FILENAME
```

### 2. Make the file executable and make directory for output
```bash
chmod +x message.sh
mkdir /home/ubuntu/lab/output
```

### 3. Edit crontab file
crontab -e

### 4. Add the following line to the file
```bash
* * * * * bin/bash /home/ubuntu/lab/message.sh
```

### 5. Save the file

### 6. Check the crontab file
crontab -l

### 7. Check the output file
ls -lah /home/ubuntu/lab/output

### 8. Check the content of the output file
```bash
cat /home/ubuntu/lab/output/message-*.txt
```

## Understanding the crontab file

### 1. The crontab file is a simple text file that contains a list of commands meant to be run at specified times. It is edited using the crontab command.

### 2. Each user can have their own crontab, and though these are files in /var/spool/, they are not intended to be edited directly.

### 3. The commands in the crontab file (and their run times) are checked by the cron daemon, which executes them in the system background.

### 4. The crontab file is read by the cron daemon, and the format is as follows:
```bash
#m  h dom mon dow  command
```
### 5. The first five fields are the time and date fields, and the command field is the command to be run at the specified time.

### 6. The time and date fields are as follows:
- m: Minute (0-59)
- h: Hour (0-23)
- dom: Day of the month (1-31)
- mon: Month (1-12)
- dow: Day of the week (0-6 with 0=Sunday)

### 7. The command field is the command to be run. It is executed using the shell environment of the user who owns the crontab.

### 8. The command can be any command or script that can be run from the command line.

### 9. The crontab file can also include comments, which are indicated by a hash symbol (#) at the beginning of the line.

### 10. The crontab file can also include environment variables, which are defined at the beginning of the file.



### 11. The crontab file can also include a MAILTO variable, which specifies the email address to which the output of the cron job should be sent.

### 12. The crontab file can also include a PATH variable, which specifies the search path for the cron job.

### 13. The crontab file can also include a HOME variable, which specifies the home directory for the cron job.

```bash
#m  h dom mon dow  command
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO="kt@devktops.com"
HOME=/home/ubuntu
* * * * * bin/bash /home/ubuntu/lab/message.sh
```

## DB Backup bash script
```bash
#!/bin/bash
# /home/ubuntu/lab/backup.sh
DATESTRING=$(date +%Y%m%d-%H%M%S)
DBNAME="mydb"
DBUSER="localuser"
DBPASS="toor123TOOR"
DBHOST="localhost"
BACKUPDIR="/var/backups/mysql"
BACKUPFILE="$BACKUPDIR/$DBNAME-$DATESTRING.sql.gz"

echo "Backing up $DBNAME to $BACKUPFILE"
mysqldump -u $DBUSER -h $DBHOST -p$DBPASS $DBNAME | gzip > $BACKUPFILE
echo "Backup complete"

# # Upload the backup to aws s3
# aws s3 cp $BACKUPFILE s3://mybucket/$DBNAME-$DATESTRING.sql.gz

# Remove the old backup file and keep only the last 3 files
cd $BACKUPDIR
ls -t | tail -n +4 | xargs rm --
```

### add the following line to the crontab file
```bash
0 3 * * * /home/ubuntu/lab/backup.sh

0 3 * * * /home/ubuntu/lab/backup.sh > /home/ubuntu/lab/output/backup.log 2>&1

0 3 * * * /home/ubuntu/lab/backup.sh > /dev/null 2>&1
```

## References link for crontab scheduling:
- https://crontab.guru/
- https://crontab.guru/examples.html