Here is a basic Nano cheat sheet with sample commands formatted.

### Opening a File
To open a file with Nano, use the following command:
```cmd
nano filename.txt
```
To open a file with nano and show numbers: 
```cmd
nano -l filename.txt
```
To open a file with nano and go to the line directly: 
```cmd
nano +10 filename.txt
```

### Basic Navigation
- **Ctrl + A**: Move to the beginning of the line.
- **Ctrl + E**: Move to the end of the line.
- **Ctrl + Y**: Scroll up one page.
- **Ctrl + V**: Scroll down one page.
- **Ctrl + Home** : Go to the beginning of the file.
- **Ctrl + End** : Go the end of the file.

### Editing
- **Ctrl + K**: Cut the current line and store it in the cutbuffer.
- **Ctrl + U**: Paste the cutbuffer contents into the text.
- **Alt + 6**: Copy the current line. 
- **Ctrl + O**: Save the file. You'll be prompted to confirm or change the file name.
- **Ctrl + X**: Exit Nano. If you haven't saved your changes, you'll be prompted to do so.

### Searching and Replacing
- **Ctrl + W**: Search for text. After pressing, enter the text you want to search for and press Enter.
- **Ctrl + \\**: Search and replace. Enter the search term, press Enter, then type the replacement text and press Enter.
- **Ctrl + _ (Shift+-)** Search the line number and go.

### Deleting
- **Ctrl + d**: Delete the character of the current position.
- **Ctrl + H** : Delete character before cursor.
- **Ctrl + Del**: Delete word to the right
- **Alt + Del**: Delete current line 

### Help
- **Ctrl + G**: Display the help screen.

### Example: Editing a File
To edit a file named `example.txt`, follow these steps:

1. Open the file with Nano:
    ```
    nano example.txt
    ```

2. Move to the line you wish to edit using the arrow keys.

3. To add or edit text, simply start typing at the cursor's position.

4. To save changes, press **Ctrl + O**, then Enter.

5. To exit Nano, press **Ctrl + X**.

Nano is a straightforward text editor, making it suitable for beginners and those needing to edit text files without the complexity of more advanced text editors.

### Delete Multiple Lines 

1. Go toe the first line that you want to delete
2. Mark the starting point by pressing ``CTRL + ^`` (press CTRL and Shift + 6 at the same time). This will set the starting point for your selection.
3. Use the arrow keys to move the cursor down to the last line you want to delete. The text will be highlighted as you move.
4. Press ``CTRL + K`` to cut (delete) the selected block of lines.
   
### Nano CHEAT SHEET
- https://www.cheatsheet.wtf/Nano/
- https://www.nano-editor.org/dist/latest/cheatsheet.html
