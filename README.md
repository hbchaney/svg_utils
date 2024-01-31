# SVG Line Trimmer

utility for removing excess lines when laser cutting along svg paths 

### how to use: 

- first ensure python above 3.10+ is installed, this module uses cases
- pip install svgpathtools (used to read and write the svgs)
- convert all objects that you want to paths (any non path objects will not be used)
- clone this repo using `git clone https://github.com/hbchaney/svg_utils.git`
- run the below script replacing the examples in `{}`  

`py line_trimmer.py {input_file.svg} {output_file.svg}`
