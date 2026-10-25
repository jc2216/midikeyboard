# midikeyboard

## Intro
- This project was built for HackClub HalfLife because I really want a 3D printer.
- This is a MIDI Keyboard that will play notes when you press on the capacitive keys and the switches. Cool lights will also happen through the LEDs. The function of the rotary encoder is currently to be determined until I write the complete firmware. I decided to not use the potentiometer because I didn't really want to source anything outside of Aliexpress.

## Features
- Waveshare Esp-32 S3 Zero
- LED
- Kailh Choc Low-Profile Switches
- Rotary Encoder

## Schematic

<img width="541" height="663" alt="Screenshot 2026-10-25 at 6 24 29 PM" src="https://github.com/user-attachments/assets/68b7411c-2b22-4ea1-8cf2-d31a821b8d93" />

- There are 3 switches, 8 capacitive touch keys, 1 rotary encoder, 3 LEDs, and 1 esp-32. The capacitive touch buttons are wired to pins on the esp-32.

## PCB

<img width="497" height="454" alt="Screenshot 2026-10-25 at 6 24 41 PM" src="https://github.com/user-attachments/assets/2e8ef418-8789-4cfc-9d8b-a1ad048c4663" />

- I drew some funny pictures on the front and the back.
- It's basically the schematic but in 3D.
- Creating footprints for the capacitive touch keys took a long time, but basically, you have to keep merging the graphic elements with the pads for each individual pad.
- Routing kind of sucked, too, because the blue lines kept crossing each other. Had to change the schematic to get it to work.

## Enclosure

<img width="484" height="502" alt="Screenshot 2026-10-25 at 6 24 16 PM" src="https://github.com/user-attachments/assets/0384be98-5404-4033-8e37-39bac3a50c7a" />

- I cadded up an enclosure for the PCB so that it's easier to hold and there's more protection.
- I'm not sure if this is the right way to CAD the enclosure but it looks okay for now.
- There are holes for M3 screws to fasten the two components.
- Need to check: the PCB may wobble in the enclosure. May need to tighten up clearance.

## Firmware
- Currently, very in progress.
- I got really confused with the firmware and CircuitPython and KMK.
- I decided to just get the template code from the guide, and then change the pin numbers to reflect my schematic.
- Will be working on firmware during build week.
- I also don't really know how to upload the firmware to the microcontroller, so will also figure that out during firmware (it's probably easier when I have the physical board anyway).


