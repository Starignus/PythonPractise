# Setting up your Raspberry Pi 3 Model B

The goal of this session is to set up our Raspberry Pis, so they can run "headless". This means that we will be able to control the RPi remotely from our laptops, without the need to connect the RPi to a screen, keyboard and mouse each time we use it. This initial setup, therefore, reduces the time we spend in setting up our Rpi each time we use it and minimizes the cabling, this, will be fundamental when our Pi will be inserted in our Pixel.

We will use the [SSH](https://en.wikipedia.org/wiki/Secure_Shell) protocol to connect from our laptop to the RPi over the Imperial/eduroam WiFi network. It let us establish a secure network communication on an unsecured network. To achieve this we will rely on remot3.it services as we will later explain. 

[//]: # (TODO: remind them not to type directly their password for imperial WPA)

To setup our RPi we will use the terminal. If you are new to the terminal can be a bit overwhelming at first, don't panic and follow the steps carefully!
We have created a [cheat sheet](...) to help you out.

### Step 1: General Setup for Raspberry Pi

At first we will setup the RPi using peripherals. Each team should get the following equipment:

[//]: # (TODO: review materials list)

 * monitor
  * HDMI-DVI cable
  * power cable
  * keyboard
  * mouse
  * SD card

[//]: # (TODO: add image)
<img src="" alt="provided-material" style="width: 400px;">

**1.1** Connect mouse and keyboard using the USB ports on the Rpi. Connect the display with provided HDMI-DVI cable plugging it in the HDMI port of the RPi.

[//]: # (TODO: add image)
<img src="" alt="pheriperals-setup" style="width: 400px;">

**1.2** Insert the micro-SD card in the back of the RPi

[//]: # (TODO: add image)
<img src="" alt="SD-slot" style="width: 400px;">

**1.3** Using Y-cable, power the Rpi up by plugging in the charger.

**1.4** The Rpi will start the setup and it will ask you which operating system you want to install. From the menu select to install Raspbian.

**1.5** Once the operating system starts, click on the __terminal__ icon next to the menu to open it.

[//]: # (TODO: add image)
<img src="" alt="terminal-icon" style="width: 400px;">

**Note:** Now we will start running some commands in the terminal.  We will run them as a **root user**, the root has the permission to modify files or default settings as administrator. By default on Raspbian (the operating system of our RPIs) the **root user** is **pi** and the **root password** associated to the root user is **raspberry**.
To operate as a root user in the terminal every command is preceded by the ```sudo``` command.

**1.6** Type the following command and press 'Enter' to open the configuration menu of the RPi:

``` bash
$ sudo raspi-config
```

The terminal will show a menu. The options can be navigated with the vertical keys of your keyboard, to accept the options press 'Enter', to finish press the lateral keys of the keyboard.

<img src="raspi-config.png" alt="screen" style="width: 400px;"/>

**1.7** First we set up the keyboard to prevent any problem when we will change the root password. We access the option: __4 Localisation Options --> Change Keyboard Layout__. Then we choose generic 105 key, and then UK. Then we can choose the default options that the menu is prompting.

[//]: # (TODO: add image, modify the text at 1.7 if required)

<img src="" alt="localisation-options" style="width: 400px;">


**1.8** We go back to the main menu and change the timezone from the __4 Localisation Options__ menu.

[//]: # (TODO: add images, modify the text at 1.7 if required)
<img src="Internationalisation.png" alt="screen" style="width: 400px;">

**1.9** Now we will change the root user password. This increases the security of the connection we will establish from our laptop to the RPi. Since you are sharing this RPi with your teammates choose a password together. To change the password we go back to the main menu and  we choose the first option: __1 Change User Password__.

[//]: # (TODO: add a more verbose explanation)
<img src="" alt="change-password" style="width: 400px;">

We have set the new password. Do not reboot the RPi yet.

**1.10** Now we will check that the SSH is enabled. We need to enable it to connect with the RPi remotely. From the main menu we access: __5 Interfacing Options --> P2 SSH__.

<img src="ssh-menu.png" alt="screen" style="width: 400px;">

And we press "Enable".

[//]: # (TODO: add image)
<img src="" alt="enable-ssh" style="width: 400px;">

**1.11** Exit the menu, you will re-enter the terminal. Reboot the RPi by entering:
``` bash
$ reboot
```

### Step 2: Setting WiFi from Imperial College network

At the moment there is no IP address assigned to our RPi. Therefore to set up the WiFi, to do so we need to modify a configuration file.

**2.1**  First we back up the configuration file *wpa_supplicant.conf*, to do so we enter the command:

```bash
$ sudo cp /etc/wpa_supplicant/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf_backup
```

**2.2** Then we edit the *wpa_supplicant.conf*. The default text editor installed in the RPi is _nano_. To edit a file with the nano editor is sufficient to enter the command ```nano /path/to/file```. Therefore to edit *wpa_supplicant.conf* we enter the following command with admin user permission:
```bash
$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

This file should just have the next line at the beginning:
```bash
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
```

**2.3** Then we add to the content of *wpa_supplicant.conf* the lines after # IC (**the configuration is case sensitive, so make sure you do not have typos**):

```bash
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1


# IC
network={
        ssid="Imperial-WPA"
        proto=RSN
        key_mgmt=WPA-EAP
        pairwise=CCMP
        auth_alg=OPEN
        eap=PEAP
        identity="ic\COLLEGE_USERNAME"
        password="YOUR_PASSWORD"
}
```
**Note:** This is the Imperial College configuration if you want to connect to the eduroam network follow the Alternative Step 2

**2.4** Now we have to replace "COLLEGE_USERNAME" with a valid college username and "YOUR_PASSWORD" with the account's password. If you are not comfortable in writing your password in plain text while working with your team, leave the field blank and follow step 3 to encrypt your password before setting it up in the *wpa_supplicant.conf*.

[//]: # (TODO: use guest account, and the optional add your college credentials)

**2.5** (Optional) If you have replaced your password in the previous step you can check if the connection works by rebooting your RPi. One the system starts again the RPi should connect automatically to the WiFi.

### Alternative Step 2: Setting WiFi from eduroam network

If you are not able to connect to the Imperial-WPA network you can also use the eduroam one. We will need to execute steps 2.1 and 2.2 of the previous section on how to modify the settings for the Imperial College network. Then in step 2.3 the informations we need to enter are slightly different:

```bash
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1


# eduroam
network={
        ssid="eduroam"
        proto=RSN
        key_mgmt=WPA-EAP
        pairwise=CCMP
        auth_alg=OPEN
        eap=PEAP
        identity="COLLEGE_USERNAME@ic.ac.uk"
        password="YOUR_PASSWORD"
}
```

**Note:** If you want your RPi to be able to connect to different networks you can include multiple network={⋯} entries.

**2.4a** You will have to replace "COLLEGE_USERNAME" with a valid username. You can change "@ic.ac.uk" with any domain that has accredited access to the eduroam network (e.g "@network.rca.ac.uk"). Replace "YOUR_PASSWORD" with the password related to that account. If you are not comfortable in writing your password in plain text while working with your team, leave the field blank and follow step 3 to encrypt your password before setting it up in the *wpa_supplicant.conf*.

**2.5** (Optional) If you have replaced your password in the previous step you can check if the connection works by rebooting your RPi. One the system starts again the RPi should connect automatically to the WiFi.

### Step 3: Encrypting Your Password

**3.1** In order not to store the password in a plain text we substitute our password with an **encrypted** one using  a **MD4 hash generator**. You can generate the hash with the following Linux command:

```bash
$ echo -n 'YOUR_PASSWORD' | iconv -t utf16le | openssl md4
```

You will have to substitute 'YOUR_PASSWORD' with the password related to the account in the *wpa_supplicant.conf*. This will be the only time you'll have to type it in plain text. Ask your teammates to look away from the screen if you are not comfortable in them seeing your password.

**3.2** The previous command will display the encrypted password on your terminal like this:
```bash
$ (stdin)= a6c71eedc2eacbca84003336a4a62a1c
```
We copy the string that was generated in your terminal screen (i.e. 'a6c71eedc2eacbca84003336a4a62a1c' in the example).

**Note:** Also you can save the hash from your password in a file and then read its content:
```bash
$ echo -n 'YOUR_PASSWORD' | iconv -t utf16le | openssl md4 > hash.txt
$ cat hash.txt
```
The first command creates the encrypted password and stores it in the __hash.txt__ file.
The second command reads the content of the __hash.txt__ file.
In general we use the ```cat``` command to read and concatenate files.

**3.2** Then we open again the *wpa_supplicant.conf* with:

```bash
$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```
**3.3** In the password field replace "YOUR_PASSWORD" with the string you generated as hexadecimal characters, adding the 'hash:' prefix as shown in the example bellow:

```bash
# IC
network={
        ssid="Imperial-WPA"
        proto=RSN
        key_mgmt=WPA-EAP
        pairwise=CCMP
        auth_alg=OPEN
        eap=PEAP
        identity="ic\COLLEGE_USERNAME"
        password=hash:a6c71eedc2eacbca84003336a4a62a1c
}
```
**3.4** The last security step to perform is to remove the bash history (the one that stores all the commands we had typed on the terminal). Therefore, we enter the following commands:
```bash
$ history -w
$ history -c
```
**3.4** Then we reboot the RPi to check that the password was properly set up with:
```bash
$ reboot
```

### Step 4: Installing Python

To install Linux packages in our RPi system we use the command: ```sudo apt-get install name_of_package``` in the terminal. Each installation could take some minutes.

**4.1: Updating operative system**
```bash
sudo apt-get update
```
**4.2: Installing C lib needed by Python:**
```bash
sudo apt-get -y install libffi-dev
sudo apt-get -y install libssl-dev
```
**4.3: Installing Python:**

```bash
sudo apt-get -y install build-essential python-dev python-openssl
sudo apt-get -y install python-setuptools
sudo apt-get -y remove --purge python-pip
sudo apt-get -y install python-pip
sudo pip install --upgrade pip
```
###Step 5: Remote connection to your Raspberry Pi
**remot3.it** services connect you easily and securely to your Pi from a mobile app, browser window and a terminal. remot3.it is based on weaved. Control remote computers using tcp hosts such as SSH. You will be able to connect to your RPi from laptop or desktop at home. The free remot3.it account allows for multiple registered services and 8 hours connections on up to 1 concurrent service(s).

**5.1** First, we need to install weaved to be able to connect our RPi. To install it:
```bash
sudo apt-get -y install weavedconnectd
```

**5.2** To configure weaved in our RPi, first we need to open an account on the [remot3.it](https://www.remot3.it/web/index.html) website. You can register from your laptop or desktop. You could also use the credentials of a weaved account, if you have one already.

**5.3** Once you have an account, from your Rpi terminal we will open the weaved installer to link your RPi to your remot3.it account:
```bash
sudo weavedinstaller
```
[//]: # (TODO: change structure, first register for an account on their laptops online and then setup weaved, Homework)

**5.4** Enter your remot3.it account username and password. Next, you will see this menu:

<img src="Pi-installer-menu.png" alt="menu1" style="width: 300px;"/>

**5.5** Then enter a name for your RPi (e.g. "myPI"). You can make it up, but remember to make a name easy for you to identify a specific RPi in case you have more than one attached to the weaved service:

<img src="remot3-piname.png" alt="menu0" style="width: 300px;"/>

**5.6** Initially you won’t have any Weaved services installed, so the upper part is empty.  Enter **1** to attach Weaved to an existing TCP service (host) on your Raspberry Pi.  You should now see the following screen:

<img src="Pi-installer-menu-02.png" alt="menu2" style="width: 300px;"/>

**5.7** Enter **1** for SSH.

**5.8** Next, we accept the default port (**y**).

<img src="Pi-installer-menu-03.png" alt="menu3" style="width: 300px;"/>

**5.9** The installer confirms your choice and asks you to give this connection a name:

<img src="Pi-installer-menu-04.png" alt="menu4" style="width: 300px;"/>

**5.10** You will now return to the main menu, where you can see your Weaved Service Connection installed, then enter **3** to exit.

<img src="Pi-installer-menu-051.png" alt="menu5" style="width: 300px;"/>

Your RPi is now ready to run headless, we just have to connect with it over ssh on our laptop to control it from the terminal. We have created two access guide one for Linux and Mac Users and the other for Windows.

### Accessing from your computer (Linux or Mac OS X)

1. We will now see how to access using your laptop to your RPi from the terminal. First, if you login to your remot3.it account,  you will get a list of your devices:

<img src="remot3-logged_in.png" alt="remot31" style="width: 400px;"/>

2. In your case you will have just one item. When you click on the name of you device, a pop-up will open:  

<img src="remot3-first_pop-up.png" alt="remot32" style="width: 400px;"/>

3. Click on the name of your ssh service and then "Confirm".

4. A second pop-up will appear:

<img src="remot3-third_pop-up.png" alt="remot33" style="width: 400px;"/>

We copy the command after *For pi username*, in this example it is: ```ssh -l pi proxy54.yoics.net -p 30015```. For you it will be different.

5. Then, paste the command in your laptop or desktop terminal (If you are using a Mac or Linux all will work, but for windows you have to [install a SSH and Telnet client](http://www.chiark.greenend.org.uk/~sgtatham/putty/)).

6. The terminal is going to show you this message:

<img src="authenticity-check.png" alt="remot34" style="width: 400px;"/>

Type yes.

7. Then, you will be prompted to enter a password, you should enter the password of the root user of your RPi. If you didn't change it previously, by default is **raspberry**

You will see on your laptop's terminal that now you are user pi. You are connected from your laptop to your RPi!! You don't need the display and mouse anymore!

### Accessing from your computer (Windows)

If your computer operative  system is Windows, to access remotely you will need to install PuTTY, which  is a free implementation of SSH and Telnet for Windows and Unix platforms. Feel free to explore other softwares! 

1. To download it click [here]( http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).

<img src="Putty.JPG" alt="weaved" style="width: 400px;"/>

2. Once downloaded, proceed with the standard installation.

3. Once installed double click on the **putty.exe** and you will see a window that looks like the one below:

<img src="PuttyConnect.JPG" alt="weaved" style="width: 400px;"/>

4. Then, if you login to your remot3.it account,  you will get a list of the services linked to your devices:

<img src="remot3-logged_in.png" alt="weaved" style="width: 400px;"/>

5. In your case you will have just one item. When you click on the name of you device, a pop-up will open:  

<img src="remot3-first_pop-up.png" alt="remot32" style="width: 400px;"/>

6. Click on the name of your ssh service and then "Confirm".

7. A second pop-up will appear:

<img src="remot3-third_pop-up.png" alt="remot33" style="width: 400px;"/>

5. Insert the server address and port obtained from remot3.it into Putty and connect!

6. When asked for username and password, please use your RPi username and password to log-in. (Please note, this is not weaved username and password).

<img src="pi_login_windows.png" alt="remot33" style="width: 400px;"/>

To exit your putty session, type "exit" and enter.

### Virtual terminal: Screen

Remember you can be connected to your RPi for up to 8 hours using **remot3.it**, after that time you have to connect again to your account and do the same access procedure we explained in the previous sections. Therefore we will show you how a *virtual terminal* can help you when you are working remotely on your RPi.

**Screen** is a full-screen software program allows you to use multiple windows (virtual VT100 terminals) in Unix. It offers a user to open several separate terminal instances inside a one single terminal window manager.

The screen application is very useful, if you are dealing with multiple programs from a command line interface and for separating programs from the terminal shell. It also allows you to share your sessions with others users and detach/attach terminal sessions.

##### When to use Screen?

One of the advantages of *Screen*, is that you can detach it. Then, you can restore it without losing anything you have done on the *Screen*. One of the typical scenario where *Screen* is of great help is when you are in the middle of SSH session and you want to download a file, update the operative, or transfer a big file to your RPi. The process could be 2 hours long. If you disconnect the SSH session, or suddenly the connection lost by accident, then the download process will stop. You have to start from the beginning again. To avoid that, we can use screen and detach it.

###### Installing Screen
Screen allows you to use multiple windows (virtual VT100 terminals) in Unix. If your local computer crashes, or you are connected remotely and lose the connection, the processes or login sessions you establish through screen don't get lost. To install Screen you can enter the following command on the RPi terminal:

```bash
sudo apt-get -y install screen
```
###### How to use Screen

* When you are in your terminal, you can create a *screen* or virtual terminal e.g. we will name the screen *mysession*:

<img src="Screen_terminal.png" alt="screen1" style="width: 400px;"/>

* Then you will be automatically attached to the *mysession* screen, that from now on we will call just *screen*. You can  now execute commands and work in the terminal without worrying to loose your work:

<img src="Screen_new_attached.png" alt="screen2" style="width: 400px;"/>

* You can detach from the *screen* by pressing “Ctrl-A” and “d“. Once detached we will be on our RPi terminal outside any *screen* session. To check the list of *active screens*:

<img src="Screen_list.png" alt="screen3" style="width: 400px;"/>

* We get a list with all the screen IDs. If we want to attach to a particular *screen* we can enter ```screen -r name_of_terminal``` like in the example below:

<img src="Screen_attaching.png" alt="screen4" style="width: 400px;"/>

[//]: # (TODO: remove visrtual terminals and ass screen cheatsheet)

###### Basic commands to work with the virtual terminals

|Screen command| Description|
|:-------------|:-----------|
| ```screen -S name_of_terminal```    | Assigning name to the virtual terminal or screen session.|
|```screen -ls``` | List all the virtual sessions or screens opened. |
|```screen -X -S name_of_terminal quit```| Kill an specific virtual terminal.|
|```screen -r name_of_terminal```| Attach to the virtual terminal or screen.|
| Press “Ctrl-A” and “d“ | Detach from virtual terminal  or screen.|
| Press "Ctrl-A” and “K” | This command will leave and kill the virtual terminal or screen |
| Press “Ctrl-A” and “n“ | Switching to the next virtual terminal or screen.|
|Press “Ctrl-A” and “p“ | Switching to the previous virtual terminal or screen|

For more examples go to the [link](http://www.tecmint.com/screen-command-examples-to-manage-linux-terminals/) or ask the instructors.

To know more about more advance details of how connect remotely go to the [advance guide](Advance_remoteconection.md):

## Some useful tips and troubleshooting guides

### Backup RPi Image

It is useful and advisable to backup a working copy of your RPi image. For example, make a backup copy after setting up WiFi and update the library, the next time the WiFi is not working, you can reformat the SD card and reinsert this backup copy to revert back to previous version. After this, your RPi get to connect back to WiFi right away like before. Here are the steps:

#### For Backing up:

##### For Windows and Mac OS

1. Download Win 32 Disk Imager if none installed on your computer [here]( https://sourceforge.net/projects/win32diskimager/)
2. Insert the SDCard into your computer (e.g. via card reader or SD card slot if your computer has one).
3. Open Win 32 Disk Imager. Select a location and give a file name for the backup image.
4. Select the right drive.
5. Click Read.
6. Once done, keep this backup copy safe. Please note that the size of the backup is the same size of your SD Card. SO please be mindful that it will take a considerable amount of disk space.

##### For replacing the image on the SD Card

#### For Windows and Mac OS

1. Download SDFormatter if none installed [here](https://www.sdcard.org/downloads/formatter_4/).
2. Download Win 32 Disk Imager if none installed [here](https://sourceforge.net/projects/win32diskimager/) or Etcher For Mac [here](https://www.etcher.io).
3. Use SDFormatter to format the SD card. Please be careful and make sure you select the correct drive letter.
4. Use Win 32 Disk Imager or Etcher to re-image the backed up image into the SD card. I.e. select the file name, the drive letter of the SD card, and then click Write. Please be careful that the correct drive letter is selected. If you wish to install a fresh Raspbian OS, you can download it [here](www.raspberrypi.org).
5. Once this is done, a new image has been rewritten on your SD Card!
