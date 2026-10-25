# Practical 20: Windows IoT Core UWP demonstration

[Back to all practicals](../README.md)

**Source:** original PDF pages 98-100. [View original pages and images](source.pdf) | [Searchable extracted text](source-text.txt)

## Files

- [MainPage.xaml.cs](MainPage.xaml.cs)
- [MainPage.xaml](MainPage.xaml)

## Hardware and prerequisites

A compatible Windows IoT Core lab board/image and a Visual Studio UWP environment; this is a legacy Windows exercise.

## Run

Read the [shared setup guide](../SETUP.md) first. Install this folder's requirements on the Pi where present.

Create a UWP Blank App named HelloIoT using the lab-supported SDK. Replace MainPage.xaml and MainPage.xaml.cs. Keep generated project, App.xaml and manifest files; deploy using the lab instructions.

## Corrections and source gaps

Normalized the namespace to HelloIoT and formatting; added a minimal matching XAML page because InitializeComponent needs generated XAML support. The PDF supplies no full project or actual screenshots in its Input IMAGE placeholders. Do not assume that an image for an older Pi supports Raspberry Pi 4; confirm the lab board/image first.

All editable programs are cleaned or adapted study versions, not byte-for-byte copies. Compare with source.pdf. The original results and diagrams are reference material; no new hardware output screenshots were generated.

Some practicals share a page in the merged book. Boundary pages are included in both neighboring folders so no content is cut off.
