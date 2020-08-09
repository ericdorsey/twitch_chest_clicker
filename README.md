### What
A Twitch "bonus channel points chest" clicker using pyautogui

https://help.twitch.tv/s/article/channel-points-guide?language=en_US

![Twitch Chest](chest.png)

Why not have Python automatically click while watching [Twitch Chess streams](https://www.twitch.tv/directory/game/Chess)?

#### Issues / Troubleshooting
##### Performance
`pyautogui` performs much better (both in terms of speed and accuracy of image finding) with OpenCV installed. Thus, OpenCV is a requirement of this script:

```
pip3 install opencv-python
```

##### Image Size Matching
If screen resolution differs and/or browser zoom differs the `chest.png` image might need to be replaced (as size won't match).

##### Main Screen Only
`pyautogui` currently can only find images on the main screen in Windows. 

https://github.com/asweigart/pyautogui/issues/9

### Links
https://stackoverflow.com/questions/43702511/why-pyautogui-locateonscreen-only-returns-none/52121440#52121440
