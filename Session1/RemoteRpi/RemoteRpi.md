# Remote connection to your Raspberry Pi

**remot3.it** services allow you to connect easily and securely to your Pi from a mobile app, browser window and a terminal. It allows you to control remote computers (our RPi) using tcp hosts such as SSH. You will be able to connect to your RPi from laptop or desktop at home. The free remot3.it account allows for multiple registered services and 8 hours connections on up to 1 concurrent service(s).

1. To configure weaved in our RPi, first we need to open an account on the [remot3.it](https://www.remot3.it/web/index.html) website. You can register from your laptop or desktop. You could also use the credentials of a weaved account, if you have one already.

2. Once you have an account, from your RPi terminal we need to install weaved (which is the precursor on which remot3.it is based) to be able to connect our RPi. To install it:
```bash
sudo apt-get -y install weavedconnectd
```
3. Then we will open the weaved installer to link your RPi to your remot3.it account:
```bash
sudo weavedinstaller
```
4. Enter your remot3.it account username and password. Next, you will see this menu:

<img src="img/Pi-installer-menu.png" alt="menu1" style="width: 300px;"/>

5. Then enter a name for your RPi (e.g. "myPI"). You can make it up, but remember to make a name easy for you to identify a specific RPi in case you have more than one attached to the weaved service:

<img src="img/remot3-piname.png" alt="menu0" style="width: 300px;"/>

6. Initially you won’t have any Weaved services installed, so the upper part is empty.  Enter **1** to attach Weaved to an existing TCP service (host) on your Raspberry Pi.  You should now see the following screen:

<img src="img/Pi-installer-menu-02.png" alt="menu2" style="width: 300px;"/>

7. Enter **1** for SSH.

8. Next, we accept the default port (**y**).

<img src="img/Pi-installer-menu-03.png" alt="menu3" style="width: 300px;"/>

9. The installer confirms your choice and asks you to give this connection a name:

<img src="img/Pi-installer-menu-04.png" alt="menu4" style="width: 300px;"/>

10. You will now return to the main menu, where you can see your Weaved Service Connection installed, then enter **3** to exit.

<img src="img/Pi-installer-menu-051.png" alt="menu5" style="width: 300px;"/>

Your RPi is now ready to run headless, we just have to connect with it over ssh on our laptop to control it from the terminal. We have created two access guide one for Linux and Mac Users and the other for Windows.

## Accessing from your computer (Linux or Mac OS X)

1. We will now see how to access using your laptop to your RPi from the terminal. First, if you login to your remot3.it account,  you will get a list of your devices:

<img src="img/remot3-logged_in.png" alt="remot31" style="width: 400px;"/>

2. In your case you will have just one item. When you click on the name of you device, a pop-up will open:  

<img src="img/remot3-first_pop-up.png" alt="remot32" style="width: 400px;"/>

3. Click on the name of your ssh service and then "Confirm".

4. A second pop-up will appear:

<img src="img/remot3-third_pop-up.png" alt="remot33" style="width: 400px;"/>

We copy the command after *For pi username*, in this example it is: ```ssh -l pi proxy54.yoics.net -p 30015```. For you it will be different.

5. Then, paste the command in your laptop or desktop terminal (If you are using a Mac or Linux all will work, but for windows you have to [install a SSH and Telnet client](http://www.chiark.greenend.org.uk/~sgtatham/putty/)).

6. The terminal is going to show you this message:

<img src="img/authenticity-check.png" alt="remot34" style="width: 400px;"/>

Type yes.

7. Then, you will be prompted to enter a password, you should enter the password of the root user of your RPi. If you didn't change it previously, by default is **raspberry**

You will see on your laptop's terminal that now you are user pi. You are connected from your laptop to your RPi!! You don't need the display and mouse anymore!

## Accessing from your computer (Windows)

If your computer operative  system is Windows, to access remotely you will need to install PuTTY, which  is a free implementation of SSH and Telnet for Windows and Unix platforms.

1. To download it click [here]( http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).

<img src="img/Putty.JPG" alt="weaved" style="width: 400px;"/>

2. Once downloaded, proceed with the standard installation.

3. Once installed double click on the **putty.exe** and you will see a window that looks like the one below:

<img src="img/PuttyConnect.JPG" alt="weaved" style="width: 400px;"/>

4. Then, if you login to your remot3.it account,  you will get a list of the services linked to your devices:

<img src="img/remot3-logged_in.png" alt="weaved" style="width: 400px;"/>

5. In your case you will have just one item. When you click on the name of you device, a pop-up will open:  

<img src="img/remot3-first_pop-up.png" alt="remot32" style="width: 400px;"/>

6. Click on the name of your ssh service and then "Confirm".

7. A second pop-up will appear:

<img src="img/remot3-third_pop-up.png" alt="remot33" style="width: 400px;"/>

5. Insert the server address and port obtained from remot3.it into Putty and connect!

6. When asked for username and password, please use your RPi username and password to log-in. (Please note, this is not weaved username and password).

<img src="img/pi_login_windows.png" alt="remot33" style="width: 400px;"/>

To exit your putty session, type "exit" and enter.

## Virtual terminal: Screen

Remember you can be connected to your RPi for up to 8 hours using **remot3.it**, after that time you have to connect again to your account and do the same access procedure we explained in the previous sections. Therefore we will show you how a *virtual terminal* can help you when you are working remotely on your RPi.

**Screen** is a full-screen software program allows you to use multiple windows (virtual VT100 terminals) in Unix. It offers a user to open several separate terminal instances inside a one single terminal window manager.

The screen application is very useful, if you are dealing with multiple programs from a command line interface and for separating programs from the terminal shell. It also allows you to share your sessions with others users and detach/attach terminal sessions.

#### When to use Screen?

One of the advantages of *Screen*, is that you can detach it. Then, you can restore it without losing anything you have done on the *Screen*. One of the typical scenario where *Screen* is of great help is when you are in the middle of SSH session and you want to download a file, update the operative, or transfer a big file to your RPi. The process could be 2 hours long. If you disconnect the SSH session, or suddenly the connection lost by accident, then the download process will stop. You have to start from the beginning again. To avoid that, we can use screen and detach it.

#### Installing Screen
Screen allows you to use multiple windows (virtual VT100 terminals) in Unix. If your local computer crashes, or you are connected remotely and lose the connection, the processes or login sessions you establish through screen don't get lost. To install Screen you can enter the following command on the RPi terminal:

```bash
sudo apt-get -y install screen
```
###### How to use Screen

* When you are in your terminal, you can create a *screen* or virtual terminal e.g. we will name the screen *mysession*:

<img src="img/Screen_terminal.png" alt="screen1" style="width: 400px;"/>

* Then you will be automatically attached to the *mysession* screen, that from now on we will call just *screen*. You can  now execute commands and work in the terminal without worrying to loose your work:

<img src="img/Screen_new_attached.png" alt="screen2" style="width: 400px;"/>

* You can detach from the *screen* by pressing “Ctrl-A” and “d“. Once detached we will be on our RPi terminal outside any *screen* session. To check the list of *active screens*:

<img src="img/Screen_list.png" alt="screen3" style="width: 400px;"/>

* We get a list with all the screen IDs. If we want to attach to a particular *screen* we can enter ```screen -r name_of_terminal``` like in the example below:

<img src="img/Screen_attaching.png" alt="screen4" style="width: 400px;"/>

###### Basic commands to work with Screen

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

To know more about more advance details of how connect remotely go to the [advanced guide](Advance_remoteconection.md):
