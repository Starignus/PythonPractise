#Backup RPi Image

It is useful and advisable to backup a working copy of your RPi image. For example, make a backup copy after setting up WiFi. The next time the WiFi is not working, you can reformat the SD card and reinsert this backup copy to revert back to previous version. After this, your RPi will connect to the WiFi right away like before. Here are the steps:

## For Backing up:

##### For Windows and Mac OS

1. Download Win 32 Disk Imager if none installed on your computer [here]( https://sourceforge.net/projects/win32diskimager/)
2. Insert the SDCard into your computer (e.g. via card reader or SD card slot if your computer has one).
3. Open Win 32 Disk Imager. Select a location and give a file name for the backup image.
4. Select the right drive.
5. Click Read.
6. Once done, keep this backup copy safe. Please note that the size of the backup is the same size of your SD Card. SO please be mindful that it will take a considerable amount of disk space.

## For replacing the image on the SD Card

##### For Windows and Mac OS

1. Download SDFormatter if none installed [here](https://www.sdcard.org/downloads/formatter_4/).
2. Download Win 32 Disk Imager if none installed [here](https://sourceforge.net/projects/win32diskimager/) or Etcher For Mac [here](https://www.etcher.io).
3. Use SDFormatter to format the SD card. Please be careful and make sure you select the correct drive letter.
4. Use Win 32 Disk Imager or Etcher to re-image the backed up image into the SD card. I.e. select the file name, the drive letter of the SD card, and then click Write. Please be careful that the correct drive letter is selected. If you wish to install a fresh Raspbian OS, you can download it [here](www.raspberrypi.org).
5. Once this is done, a new image has been rewritten on your SD Card!
