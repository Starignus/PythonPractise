# Alternative Network Setting

If you don't have access to a guest account for the Imperial-WPA network or you would like to connect your Raspberry Pi  to any eduroam network, we have prepared a step by step guide to help you.

  + [Imperial WPA](#step-1:-setting-the-wifi-from-imperial-college-network-with-your-credentials)
  + [eduroam](#alternative-step-1:-setting-wifi-from-eduroam-network)

**Note:** In this guide you will have to type your password in clear and then encrypt it. If you are working with your teammates, especially, be careful. However we have provided an option that involves typing the password only once.

### Step 1: Setting the WiFi from Imperial College network with your credentials

1. To set up the WiFi we need to modify a configuration file. First we back up the configuration file *wpa_supplicant.conf*, to do so we enter the command:

```bash
$ sudo cp /etc/wpa_supplicant/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf_backup
```

2. Then we edit the *wpa_supplicant.conf*. The default text editor installed in the RPi is _nano_. To edit a file with the nano editor is sufficient to enter the command ```nano /path/to/file```. Therefore to edit *wpa_supplicant.conf* we enter the following command with admin user permission:
```bash
$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

This file should just have the next line at the beginning:
```bash
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
```

3. Then we add to the content of *wpa_supplicant.conf* the lines after # IC (**the configuration is case sensitive, so make sure you do not have typos**):

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
**Note:** This is the Imperial College configuration if you want to connect to the eduroam network follow the Alternative Guide

4. Now we have to replace "COLLEGE_USERNAME" with a valid college username and "YOUR_PASSWORD" with the account's password. If you are not comfortable in writing your password in plain text while working with your team, leave the field blank and follow the steps in Section 2 to encrypt your password before setting it up in the *wpa_supplicant.conf*.

5. (Optional) If you have replaced your password in the previous step you can check if the connection works by rebooting your RPi. One the system starts again the RPi should connect automatically to the WiFi.

### Alternative Step 1: Setting WiFi from eduroam network

To connect to the eduroam network we will need to execute steps 1 and 2 of the previous section on how to modify the settings for the Imperial College network. Then in step 3 the informations we need to enter are slightly different:

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

4. You will have to replace "COLLEGE_USERNAME" with a valid username. You can change "@ic.ac.uk" with any domain that has accredited access to the eduroam network (e.g "@network.rca.ac.uk"). Replace "YOUR_PASSWORD" with the password related to that account. If you are not comfortable in writing your password in plain text while working with your team, leave the field blank and follow step 3 to encrypt your password before setting it up in the *wpa_supplicant.conf*.

5. (Optional) If you have replaced your password in the previous step you can check if the connection works by rebooting your RPi. One the system starts again the RPi should connect automatically to the WiFi.

### Step 2: Encrypting Your Password

1. In order not to store the password in a plain text we substitute our password with an **encrypted** one using  a **MD4 hash generator**. You can generate the hash with the following Linux command:

```bash
$ echo -n 'YOUR_PASSWORD' | iconv -t utf16le | openssl md4
```

You will have to substitute 'YOUR_PASSWORD' with the password related to the account in the *wpa_supplicant.conf*. This will be the only time you'll have to type it in plain text. Ask your teammates to look away from the screen if you are not comfortable in them seeing your password.

2. The previous command will display the encrypted password on your terminal like this:
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

3. Then we open again the *wpa_supplicant.conf* with:

```bash
$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```
4. In the password field replace "YOUR_PASSWORD" with the string you generated as hexadecimal characters, adding the 'hash:' prefix as shown in the example bellow:

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
5. The last security step to perform is to remove the bash history (the one that stores all the commands we had typed on the terminal). Therefore, we enter the following commands:
```bash
$ history -w
$ history -c
```
6. Then we reboot the RPi to check that the password was properly set up with:
```bash
$ reboot
```
7. And you are done!
