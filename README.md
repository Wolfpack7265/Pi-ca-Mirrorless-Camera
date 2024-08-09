# Pi-ca-Mirrorless-Camera
Interchangeable lens mirrorless camera project, using Raspberry pi HQ camera module

Intro--------------------------------------------------

raspberry pi camera project to produce an open-source, feature-packed camera using the raspberry pi HQ camera module. The idea for this project came from the desire to get a secondary point-and-shoot camera for my daily photography. Instead of buying from the list of overpriced digicams on facebook marketplace, I decided to create something with the features I wanted most!

Sensor-------------------------------------------------

At the heart of the pi-ca is the raspberry pi HQ module, which utlizes Sony's IMX477 Image sensor. The sensor features the following specs for photos:
- 12.3mp resolution
- stacked, back-side illuminated sensor deisgn
- analog and digital gain adjustments
- 1/2.3 size sensor (7.564 mm H vs. 5.476mm V) = 5.5x crop factor
- native 4:3 aspect ratio
- electronic shutter with a max shutter speed of about 1/3000s (300 microseconds)
- sensor flipping and mirroring
- ambient light sensor

For video, it gets even better, with a list of features that even compare to cameras released in 2024:
- 1080p @ up to 240fps
- 4k @ 60fps
- Full sensor readout (4056 x 3040) @ up to 60fps
- up to 12 bit RAW output in full sensor format

full documentation is provided by sony: https://www.sony-semicon.com/files/62/pdf/p-13_IMX477-AACK_Flyer.pdf

Planned Features (v0)-------------------------------------------------

The initial version of this project will be a proof of concept for later versions, and will obviously be missing some polish and usability:
- photo-centric philosophy and design
- 3D-printed case
- C/CS mount for lenses
- LCD screen with UI and menus
- shutter button, maybe buttons for UI navigation
- easy iso, shutter speed adjustments
- focus peaking for manual focus
- real-time exposure histogram
- easily removable/rechargable battery options
- dedicated SD card slot for photo/video storage
- tripod mount (1/4-20), body accessory mounts?
- configuration file/ stored settings

Future/Potential features to be added? (v1+) -------------------------------------------------
- all video features (1080p 240, 4k 60, etc.)
- mode dial?
- mount change to E-mount?
- Contrast Detection Auto focus
- Intervalometer/timelapse settings
- Electronic/digital image stabalization 
- many more!
