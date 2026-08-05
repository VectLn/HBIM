3D segmentation using 2D VLM based on https://arxiv.org/pdf/2601.02029

python -m venv C:\dev\open3D\env

C:\dev\open3D\env\Scripts\Activate.ps1

python -m pip install open3d

python -m pip install --upgrade pip setuptools wheel

python -m pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu124

python -m pip install -r requirements.txt

python -m pip install "transformers==4.40.2" "tokenizers==0.19.1" "huggingface-hub==0.36.0"

python -m pip install -e .\segment_anything

python -m pip install --no-build-isolation -e .\GroundingDINO

New-Item -ItemType Directory -Force -Path ".\weights"

Invoke-WebRequest -Uri "https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth" -OutFile ".\weights\groundingdino_swint_ogc.pth"

Invoke-WebRequest -Uri "https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth" -OutFile ".\weights\sam_vit_b_01ec64.pth"

python .\grounded_sam_demo.py --config ".\GroundingDINO\groundingdino\config\GroundingDINO_SwinT_OGC.py" --grounded_checkpoint ".\weights\groundingdino_swint_ogc.pth" --sam_version "vit_b" --sam_checkpoint ".\weights\sam_vit_b_01ec64.pth" --input_image ".\assets\demo1.jpg" --output_dir ".\outputs" --box_threshold 0.3 --text_threshold 0.25 --text_prompt "bear" --device "cpu"