# Personal Config-Files

I like to setup my computers mostly the same, running Ubuntu Linux with i3 wm. But I am simply bored with setting them up, hence the use of ansible.

There are also some helper scripts contained here to ensure that 

- shortcut-script.py - is a small watchdog script for my macro keyboard so I can have some tasks on a special keyboard itself.
- scan2paperless - modified paperless scan script so I do not have to perform the bothersome tasks of scanning, then saving, then opening a browser, then uploading to paperless, etc.
- post2paperless - dependency for scan2paperless, actual upload logic.

Most of these resources are harvested form the internet and adjusted from my own purposes. Some noteworthy features about this configuration are:
- Designed for focus: All program must stay in foreground, no tabs are allowed, no virtual desktops. 
- Some Windows Shortcuts: Win+L works, language switching using Win+Space works as well as it does on a Windows desktop. This is to ensure my muscle memory does not trip me up.
- i3 config is mostly dwm inspired(Alt+P and Ctrl+Shift+C work way more faster for me than)

TODO:
- rewrite ansible to pyinfra
- remove dependency on username
