# Baloo extension for ULauncher

This extension search for files in the Baloo indexes (on KDE/Plasma) for instant results.

![alt text](https://github.com/briceio/ulauncher-baloo/blob/master/overview.png?raw=true)

## Usage

**The default trigger keyword is "?".**

The query syntax is the one offered by Baloo.

For example, to search for all the files/folders containing "draft", type "? draft".

## File location (focus in your file manager)

If instead of opening your file in your default application, you want to locate it in your default file manager, press Alt+RETURN.

## Index setup

To benefit from this extension you have to check that baloo is enabled (balooctl) and that your indexes are correctly setup.

This can be done two ways:
- Using Plasma general settings (sub settings Search / File Search)
- Using balooctl (https://community.kde.org/Baloo)

## Extension settings

### Keyword

Change the search keyword trigger. 

Default is "?".

### Limits results

Override the limit results of ULauncher for the results on this extension. 

Default is 10.

### Icons path

The icons path to use in the search results. You have to define a path where the MIME-types icons of your theme are kept. Use the 64x64 icons for better visual quality.

For eg. MIME-type icons are named: "application-x-blender.svg" or "text-css.svg". 

Default is: /usr/share/icons/breath2-dark/mimetypes/64

### Tags

If enabled, you can inject tags to filter out the results by types. 

| Tag | Filter |
|-|-|
| #f | Folders |
| #img | Images |
| #audio | Audio files |
| #video | Video files |
| #doc | Documents  |
| #pres | Presentations |
| #ss | Spreadsheets |
| #txt | Text files |
| #z | Archives |

Ex: To search for any folders containing "client", type:

```? clients #f```