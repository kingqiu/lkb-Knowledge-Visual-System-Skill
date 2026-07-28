#!/usr/bin/env bash
# Adapt an already-complete image-model draft to the exact 3:4 delivery frame.
# The brand lock-up must already be natively generated in the image; this script
# deliberately never adds, replaces, or overlays any visible graphic or text.
# Usage: finalize_knowledge_card.sh input-image output.png
set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 input-image output.png" >&2
  exit 2
fi

input_path=$1
output_path=$2

if [ ! -f "$input_path" ]; then
  echo "Input not found: $input_path" >&2
  exit 2
fi
if [ -e "$output_path" ]; then
  echo "Refusing to overwrite existing output: $output_path" >&2
  exit 2
fi
# Pad a narrow source to 3:4 before cropping. This preserves titles and hero diagrams
# when an image model returns 2:3 or 9:16 instead of the required 3:4 frame.
ffmpeg -hide_banner -loglevel error -i "$input_path" \
  -vf "pad='max(iw,ih*3/4)':'max(ih,iw/(3/4))':(ow-iw)/2:(oh-ih)/2:color=0xF5F0EA,crop='if(gte(iw/ih,3/4),ih*3/4,iw)':'if(gte(iw/ih,3/4),ih,iw/(3/4))':(iw-ow)/2:(ih-oh)/2,scale=1080:1440:flags=lanczos" \
  -frames:v 1 "$output_path"

dimensions=$(sips -g pixelWidth -g pixelHeight "$output_path")
echo "$dimensions"
echo "PASS: formatted at 1080×1440 without adding any overlay."
