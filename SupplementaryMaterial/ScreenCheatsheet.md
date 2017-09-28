# Screen Cheasheet

### Getting in
|Description| Screen Command|
|:-------------|:-----------|
|start a new screen session with session name | ``` screen -S <name>``` |
| list running sessions/screens | ``` screen -ls``` |
| attach to a running session | ```screen -x``` |
| attach to session name | ```screen -r <name>``` |
| the “ultimate attach” |	```screen -dRR``` (Attaches to a screen session. If the session is attached elsewhere, detaches that other display. If no session exists, creates one. If multiple sessions exist, uses the first one.)

### Escape key
All screen commands are prefixed by an escape key, by default ```C-a``` (that's Control-a, sometimes written ^a). To send a literal C-a to the programs in screen, use ```C-a a```. This is useful when working with screen within screen. For example C-a a n will move screen to a new window on the screen within screen.

### Getting out
|Description| Screen Command|
|:-------------|:-----------|
| detach | ```C-a d``` |
| detach and logout (quick exit) | ```C-a D D```|
| exit screen | ```C-a ``` Exit all of the programs in screen (not recommended) |
| force-exit screen | ```C-a C-\```(not recommended) |
| getting out of the screen session | ```exit``` |

### Window Management
|Description| Screen Command|
|:-------------|:-----------|
| create new window | ```C-a c``` |
| change to last-visited active window |  ```C-a C-a``` (commonly used to flip-flop between two windows) |
| change to window by number | ```C-a <number>``` (only for windows 0 to 9) |
| change to window by number or name | ```C-a ' <number or title>``` |
| change to next window in list | ```C-a n``` or ```C-a <space>``` |
| change to previous window in list | ```C-a p``` or ```C-a <backspace>``` |
| see window list     | ```C-a "``` (allows you to select a window to change to) |
| show window bar       | ```C-a w``` (if you don't have window bar) |
| kill current window   | ```C-a k``` (not recommended) |
| kill all windows   | ```C-a \``` (not recommended) |
| rename current window | ```C-a A``` |

### Split screen
|Description| Screen Command|
|:-------------|:-----------|
| split display horizontally  |```C-a S``` |
| split display vertically    |```C-a``` or ```C-a V``` (for the vanilla vertical screen patch) |
| jump to next display region |```C-a tab``` |
| remove current region       |```C-a X``` |
| remove all regions but the current one |```C-a Q``` |

### Clipboard and Navigation
|Description| Screen Command|
|:-------------|:-----------|
|freely navigate buffer |	```C-a [``` or ```C-a <esc>```
|toggle selection to copy |	space
|paste |	```C-a ]```

### Help
|Description| Screen Command|
|:-------------|:-----------|
|help	| ```C-a ? ``` (lists keybindings)|

### Misc
|Description| Screen Command|
|:-------------|:-----------|
|redraw window |```C-a C-l```
|monitor window for activity|	```C-a M```
|monitor window for silence|	```C-a _```
|enter digraph (for producing non-ASCII characters)|	```C-a C-v```
|lock (password protect) session|	```C-a x```
|enter screen command|	```C-a :```
|enable logging in the screen session|	```C-a H```

### Scrollback-buffer
In copy mode, one can navigate the scrollback buffer in various ways:

|Description| Screen Command|
|:-------------|:-----------|
|half page up |	```C-u```		
|half page down |	```C-d```
|back |	```C-b```
|forward | ```C-f```
|cursor left/down/up/right |	```h/j/k/l```


For further information you can visit the [GNU screen website](http://aperiodic.net/screen/start).
