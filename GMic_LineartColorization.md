 
# G'MIC Linear  Colorization

### Installation
We need a newer version of `gmic` which contains the function `fx_colorize_lineart_smart`: 2.4.5 which is on ubuntu repos does not have it, but [2.9.2 on github releases](https://github.com/dtschump/gmic/releases) does.
  * Download and decompress <https://github.com/dtschump/gmic/archive/v.2.9.2.tar.gz>
  * Build using CMake
	```bash
	cd gmic
	mkdir build
	cd build
	cmake ..
	make -j8
	./gmic -version
	```

### Function signatures
All functions' code and descriptions are in the [gmic/src/gmic_stdlib.gmic](https://github.com/dtschump/gmic/blob/master/src/gmic_stdlib.gmic) file.

The arguments are listed in the comment above the function:
```
Parameter Name = type(default value, min value, max value)
```

This appears to be the signature for the colorization function.
```
#@gui Colorize Lineart [Smart Coloring] : fx_colorize_lineart_smart, fx_colorize_lineart_smart_preview(0)
#@gui : Colorize Mode = choice("Generate Random-Colors Layer","Extrapolate Color Spots on Transparent Top Layer",
#@gui : "Auto-Clean Bottom Color Layer")
#@gui : sep = separator()
#@gui : note = note{"<small><b>Global geometry parameters:</b></small>"}
#@gui : Contour Detection (%) = float(95,0,100)
#@gui : Discard Contour Guides = bool(0)
#@gui : note = note{"<small>Add strokes with a saturated color having value 255 (e.g. pure red) on your lineart
#@gui : allows to guide the colorization algorithm with virtual contours.</small>"}
#@gui : Output Region Delimiters = _bool(0)
#@gui : sep = separator()
#@gui : note = note{"<small><b>For <i>Random colors</i> mode only:</b></small>"}
#@gui : Make Hue Depends on Region Size = float(1,0,1)
#@gui : Maximal Color Saturation = int(24,0,255)
#@gui : Minimal Color Intensity = int(200,0,255)
#@gui : sep = separator()
#@gui : note = note{"<small><b>For <i>color spots</i> mode only:</b></small>"}
#@gui : Color Shading (%) = int(0,0,100)
#@gui : sep = separator()
#@gui : note = note{"<small><b>Connection parameters:</b></small>"}
#@gui : End Point Rate (%) = float(75,0,100)
#@gui : End Point Connectivity = int(2,1,5)
#@gui : Spline Max Length (px) = float(60,0,256)
#@gui : Segment Max Length (px) = float(20,0,256)
#@gui : Spline Max Angle (deg) = float(90,0,180)
#@gui : Spline Roundness = float(1,0,2)
#@gui : Minimal Region Area = float(10,0,100)
#@gui : Allow Self Intersections = bool(1)
#@gui : sep = separator()
#@gui : Preview Type = choice(0,"Colored geometry","Colored regions","Colored lineart")
#@gui : sep = separator()
#@gui : note = note("<small>Authors: <i>David Tschumperlé</i>, <i>Sébastien Fourey</i> and
#@gui : <i>David Revoy</i>.      Latest Update: <i>2018/11/09</i>.</small>")
```


### Executing functions

We can execute GMIC functions from console
```bash
gmic input_image -functionname arg0,arg1,arg2,arg3 -o output_image
```

Testing with the `fx_autofill_lineart`, which is a primitive version of colorization, but has limited arguments:
```
gmic sombulus_archive/68.jpeg -fx_autofill_lineart 90,1,12,2  -o[-1] 68__autofil_lineart.png
```

`fx_colorize_lineart_smart` has around 15 arguments:
```
./gmic ../../Automatic-Flat-Colouring/sombulus_archive/68.jpeg -fx_colorize_lineart_smart 0,95,1,1,0,24,200,0,75,2,60,20,90,1,10,1 -o 68__colorize_lineart_smart.png
```
The arguments `0,95,1,1,0,24,200,0,75,2,60,20,90,1,10,1`:
* `0` for *Colorize Mode = choice("Generate Random-Colors Layer","Extrapolate Color Spots on Transparent Top Layer", "Auto-Clean Bottom Color Layer")*
* `95` for *Contour Detection (%) = float(95,0,100)*
* `1` for *Discard Contour Guides = bool(0)*
* ....

Unfortunately, this combination of parameters/inputs yields an empty output.
Maybe we can find the proper arguments via experimentation.
