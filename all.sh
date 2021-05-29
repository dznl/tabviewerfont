#!/bin/bash
source ~/.bash_aliases
python3 fontdozenalizer/addglyphs.py CascadiaCode.ttf CascadiaCodeEnriched.ttf
bash addfeatures.sh CascadiaCodeEnriched.ttf CascadiaTablature.ttf
rm "CascadiaTablature.ttf"
git add "CascadiaTablature.ttf.ttx"

replac CascadiaCode CascadiaTablature -- "CascadiaTablature.ttf.ttx" --now
replac 'Cascadia Code' 'Cascadia Tablature' -- "CascadiaTablature.ttf.ttx" --now

ttx -o "CascadiaTablature.ttf" "CascadiaTablature.ttf.ttx"
