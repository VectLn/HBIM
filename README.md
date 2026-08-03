# HBIM
Heritage Building Information Modeling (HBIM)

(base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> C:\dev\open3D\env\Scripts\Activate.ps1                           
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> export AM_I_DOCKER=False
export : The term 'export' is not recognized as the name of a cmdlet, function, script file, or operable program. Check 
the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ export AM_I_DOCKER=False
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (export:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> python -c "import sys; print(sys.executable)"
C:\dev\open3D\env\Scripts\python.exe
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> python -m pip freeze | Out-File -Encoding utf8 "C:\dev\open3D\packages-avant-grounded-sam.txt"
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> python -m pip install --upgrade pip setuptools wheel
Requirement already satisfied: pip in c:\dev\open3d\env\lib\site-packages (23.0.1)
Collecting pip
  Downloading pip-26.2-py3-none-any.whl (1.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 38.4 MB/s eta 0:00:00
Requirement already satisfied: setuptools in c:\dev\open3d\env\lib\site-packages (65.5.0)
Collecting setuptools
  Downloading setuptools-83.0.0-py3-none-any.whl (1.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.0/1.0 MB 66.5 MB/s eta 0:00:00
Collecting wheel
  Downloading wheel-0.47.0-py3-none-any.whl (32 kB)
Requirement already satisfied: packaging>=24.0 in c:\dev\open3d\env\lib\site-packages (from wheel) (26.2)
Installing collected packages: wheel, setuptools, pip
  Attempting uninstall: setuptools
    Found existing installation: setuptools 65.5.0
    Uninstalling setuptools-65.5.0:
      Successfully uninstalled setuptools-65.5.0
  Attempting uninstall: pip
    Found existing installation: pip 23.0.1
    Uninstalling pip-23.0.1:
      Successfully uninstalled pip-23.0.1
Successfully installed pip-26.2 setuptools-83.0.0 wheel-0.47.0
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> python -m pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu124
Looking in indexes: https://download.pytorch.org/whl/cu124
Collecting torch==2.5.1
  Downloading torch-2.5.1%2Bcu124-cp310-cp310-win_amd64.whl (2510.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.5/2.5 GB 29.1 MB/s  0:00:29
Collecting torchvision==0.20.1
  Downloading torchvision-0.20.1%2Bcu124-cp310-cp310-win_amd64.whl (6.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.1/6.1 MB 94.9 MB/s  0:00:00
Collecting filelock (from torch==2.5.1)
  Downloading filelock-3.29.0-py3-none-any.whl.metadata (2.0 kB)
Requirement already satisfied: typing-extensions>=4.8.0 in c:\dev\open3d\env\lib\site-packages (from torch==2.5.1) (4.16.0)
Collecting networkx (from torch==2.5.1)
  Downloading networkx-3.4.2-py3-none-any.whl.metadata (6.3 kB)
Requirement already satisfied: jinja2 in c:\dev\open3d\env\lib\site-packages (from torch==2.5.1) (3.1.6)
Collecting fsspec (from torch==2.5.1)
  Downloading fsspec-2026.4.0-py3-none-any.whl.metadata (10 kB)
Collecting sympy==1.13.1 (from torch==2.5.1)
  Downloading sympy-1.13.1-py3-none-any.whl.metadata (12 kB)
Requirement already satisfied: numpy in c:\dev\open3d\env\lib\site-packages (from torchvision==0.20.1) (2.2.6)
Collecting pillow!=8.3.*,>=5.3.0 (from torchvision==0.20.1)
  Downloading pillow-12.2.0-cp310-cp310-win_amd64.whl.metadata (9.0 kB)
Collecting mpmath<1.4,>=1.1.0 (from sympy==1.13.1->torch==2.5.1)
  Downloading mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
Requirement already satisfied: MarkupSafe>=2.0 in c:\dev\open3d\env\lib\site-packages (from jinja2->torch==2.5.1) (3.0.3)
Downloading sympy-1.13.1-py3-none-any.whl (6.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.2/6.2 MB 53.9 MB/s  0:00:00
Downloading mpmath-1.3.0-py3-none-any.whl (536 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.2/536.2 kB ?  0:00:00
Downloading pillow-12.2.0-cp310-cp310-win_amd64.whl (7.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.1/7.1 MB 36.5 MB/s  0:00:00
Downloading filelock-3.29.0-py3-none-any.whl (39 kB)
Downloading fsspec-2026.4.0-py3-none-any.whl (203 kB)
Downloading networkx-3.4.2-py3-none-any.whl (1.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 91.3 MB/s  0:00:00
Installing collected packages: mpmath, sympy, pillow, networkx, fsspec, filelock, torch, torchvision
Successfully installed filelock-3.29.0 fsspec-2026.4.0 mpmath-1.3.0 networkx-3.4.2 pillow-12.2.0 sympy-1.13.1 torch-2.5.1+cu124 torchvision-0.20.1+cu124
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> python -c "import torch; print('PyTorch:', torch.__version__); print('CUDA PyTorch:', torch.version.cuda); print('GPU disponible:', torch.cuda.is_available()); print('GPU:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'aucun')"
PyTorch: 2.5.1+cu124
CUDA PyTorch: 12.4
GPU disponible: True
GPU: NVIDIA T1000
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> Set-Location -LiteralPath "C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything"
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> 
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> python -m pip install -r requirements.txt
Collecting addict (from -r requirements.txt (line 1))
  Using cached addict-2.4.0-py3-none-any.whl.metadata (1.0 kB)
Collecting diffusers (from -r requirements.txt (line 2))
  Downloading diffusers-0.39.0-py3-none-any.whl.metadata (20 kB)
Collecting gradio (from -r requirements.txt (line 3))
  Downloading gradio-6.22.0-py3-none-any.whl.metadata (17 kB)
Collecting huggingface_hub (from -r requirements.txt (line 4))
  Downloading huggingface_hub-1.26.0-py3-none-any.whl.metadata (16 kB)
Collecting matplotlib (from -r requirements.txt (line 5))
  Downloading matplotlib-3.10.9-cp310-cp310-win_amd64.whl.metadata (52 kB)
Requirement already satisfied: numpy in c:\dev\open3d\env\lib\site-packages (from -r requirements.txt (line 6)) (2.2.6)
Collecting onnxruntime (from -r requirements.txt (line 7))
  Downloading onnxruntime-1.23.2-cp310-cp310-win_amd64.whl.metadata (5.3 kB)
Collecting opencv_python (from -r requirements.txt (line 8))
  Using cached opencv_python-5.0.0.93-cp37-abi3-win_amd64.whl.metadata (20 kB)
Requirement already satisfied: Pillow in c:\dev\open3d\env\lib\site-packages (from -r requirements.txt (line 9)) (12.2.0)
Collecting pycocotools (from -r requirements.txt (line 10))
  Downloading pycocotools-2.0.11-cp310-cp310-win_amd64.whl.metadata (1.3 kB)
Collecting PyYAML (from -r requirements.txt (line 11))
  Downloading pyyaml-6.0.3-cp310-cp310-win_amd64.whl.metadata (2.4 kB)
Requirement already satisfied: requests in c:\dev\open3d\env\lib\site-packages (from -r requirements.txt (line 12)) (2.34.2)
Requirement already satisfied: setuptools in c:\dev\open3d\env\lib\site-packages (from -r requirements.txt (line 13)) (83.0.0)
Collecting supervision (from -r requirements.txt (line 14))
  Downloading supervision-0.29.1-py3-none-any.whl.metadata (14 kB)
Collecting termcolor (from -r requirements.txt (line 15))
  Downloading termcolor-3.3.0-py3-none-any.whl.metadata (6.5 kB)
Collecting timm (from -r requirements.txt (line 16))
  Downloading timm-1.0.28-py3-none-any.whl.metadata (40 kB)
Requirement already satisfied: torch in c:\dev\open3d\env\lib\site-packages (from -r requirements.txt (line 17)) (2.5.1+cu124)
Requirement already satisfied: torchvision in c:\dev\open3d\env\lib\site-packages (from -r requirements.txt (line 18)) (0.20.1+cu124)
Collecting transformers (from -r requirements.txt (line 19))
  Downloading transformers-5.14.1-py3-none-any.whl.metadata (32 kB)
Collecting yapf (from -r requirements.txt (line 20))
  Using cached yapf-0.43.0-py3-none-any.whl.metadata (46 kB)
Collecting nltk (from -r requirements.txt (line 21))
  Downloading nltk-3.10.1-py3-none-any.whl.metadata (3.2 kB)
Collecting fairscale (from -r requirements.txt (line 22))
  Downloading fairscale-0.4.13.tar.gz (266 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Collecting litellm (from -r requirements.txt (line 23))
  Downloading litellm-1.95.0-cp310-cp310-win_amd64.whl.metadata (41 kB)
Requirement already satisfied: importlib_metadata in c:\dev\open3d\env\lib\site-packages (from diffusers->-r requirements.txt (line 2)) (9.0.0)
Requirement already satisfied: filelock in c:\dev\open3d\env\lib\site-packages (from diffusers->-r requirements.txt (line 2)) (3.29.0)
Collecting httpx<1.0.0 (from diffusers->-r requirements.txt (line 2))
  Using cached httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting regex!=2019.12.17 (from diffusers->-r requirements.txt (line 2))
  Downloading regex-2026.7.19-cp310-cp310-win_amd64.whl.metadata (41 kB)
Collecting safetensors>=0.8.0 (from diffusers->-r requirements.txt (line 2))
  Downloading safetensors-0.8.0-cp310-abi3-win_amd64.whl.metadata (4.2 kB)
Requirement already satisfied: click<9.0.0,>=8.4.2 in c:\dev\open3d\env\lib\site-packages (from huggingface_hub->-r requirements.txt (line 4)) (8.4.2)
Requirement already satisfied: fsspec>=2023.5.0 in c:\dev\open3d\env\lib\site-packages (from huggingface_hub->-r requirements.txt (line 4)) (2026.4.0)
Collecting hf-xet<2.0.0,>=1.5.1 (from huggingface_hub->-r requirements.txt (line 4))
  Using cached hf_xet-1.5.2-cp38-abi3-win_amd64.whl.metadata (4.9 kB)
Requirement already satisfied: packaging>=20.9 in c:\dev\open3d\env\lib\site-packages (from huggingface_hub->-r requirements.txt (line 4)) (26.2)
Collecting tqdm>=4.42.1 (from huggingface_hub->-r requirements.txt (line 4))
  Using cached tqdm-4.70.0-py3-none-any.whl.metadata (57 kB)
Requirement already satisfied: typing-extensions>=4.1.0 in c:\dev\open3d\env\lib\site-packages (from huggingface_hub->-r requirements.txt (line 4)) (4.16.0)
Requirement already satisfied: colorama in c:\dev\open3d\env\lib\site-packages (from click<9.0.0,>=8.4.2->huggingface_hub->-r requirements.txt (line 4)) (0.4.6)
Collecting anyio (from httpx<1.0.0->diffusers->-r requirements.txt (line 2))
  Downloading anyio-4.14.2-py3-none-any.whl.metadata (4.6 kB)
Requirement already satisfied: certifi in c:\dev\open3d\env\lib\site-packages (from httpx<1.0.0->diffusers->-r requirements.txt (line 2)) (2026.7.22)
Collecting httpcore==1.* (from httpx<1.0.0->diffusers->-r requirements.txt (line 2))
  Using cached httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Requirement already satisfied: idna in c:\dev\open3d\env\lib\site-packages (from httpx<1.0.0->diffusers->-r requirements.txt (line 2)) (3.18)
Collecting h11>=0.16 (from httpcore==1.*->httpx<1.0.0->diffusers->-r requirements.txt (line 2))
  Using cached h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting brotli>=1.1.0 (from gradio->-r requirements.txt (line 3))
  Downloading brotli-1.2.0-cp310-cp310-win_amd64.whl.metadata (6.3 kB)
Collecting fastapi<1.0,>=0.115.2 (from gradio->-r requirements.txt (line 3))
  Downloading fastapi-0.141.1-py3-none-any.whl.metadata (27 kB)
Collecting gradio-client==2.6.0 (from gradio->-r requirements.txt (line 3))
  Downloading gradio_client-2.6.0-py3-none-any.whl.metadata (7.1 kB)
Collecting groovy~=0.1 (from gradio->-r requirements.txt (line 3))
  Downloading groovy-0.1.2-py3-none-any.whl.metadata (6.1 kB)
Collecting hf-gradio<1.0,>=0.4.1 (from gradio->-r requirements.txt (line 3))
  Downloading hf_gradio-0.4.1-py3-none-any.whl.metadata (428 bytes)
Requirement already satisfied: jinja2<4.0 in c:\dev\open3d\env\lib\site-packages (from gradio->-r requirements.txt (line 3)) (3.1.6)
Requirement already satisfied: markupsafe<4.0,>=2.0 in c:\dev\open3d\env\lib\site-packages (from gradio->-r requirements.txt (line 3)) (3.0.3)
Collecting orjson~=3.0 (from gradio->-r requirements.txt (line 3))
  Downloading orjson-3.11.9-cp310-cp310-win_amd64.whl.metadata (43 kB)
Collecting pandas<4.0,>=1.0 (from gradio->-r requirements.txt (line 3))
  Downloading pandas-2.3.3-cp310-cp310-win_amd64.whl.metadata (19 kB)
Requirement already satisfied: pydantic<=3.0,>=2.0 in c:\dev\open3d\env\lib\site-packages (from gradio->-r requirements.txt (line 3)) (2.13.4)
Collecting pydub<1.0 (from gradio->-r requirements.txt (line 3))
  Downloading pydub-0.25.1-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting python-multipart<1.0,>=0.0.18 (from gradio->-r requirements.txt (line 3))
  Downloading python_multipart-0.0.32-py3-none-any.whl.metadata (2.1 kB)
Collecting pytz>=2017.2 (from gradio->-r requirements.txt (line 3))
  Using cached pytz-2026.3.post1-py2.py3-none-any.whl.metadata (22 kB)
Collecting safehttpx<0.2.0,>=0.1.7 (from gradio->-r requirements.txt (line 3))
  Downloading safehttpx-0.1.7-py3-none-any.whl.metadata (4.2 kB)
Collecting semantic-version~=2.0 (from gradio->-r requirements.txt (line 3))
  Downloading semantic_version-2.10.0-py2.py3-none-any.whl.metadata (9.7 kB)
Collecting starlette<2.0,>=1.0.1 (from gradio->-r requirements.txt (line 3))
  Downloading starlette-1.3.1-py3-none-any.whl.metadata (6.4 kB)
Collecting tomlkit<0.15.0,>=0.12.0 (from gradio->-r requirements.txt (line 3))
  Downloading tomlkit-0.14.0-py3-none-any.whl.metadata (2.8 kB)
Collecting typer<1.0,>=0.12 (from gradio->-r requirements.txt (line 3))
  Downloading typer-0.27.1-py3-none-any.whl.metadata (16 kB)
Collecting uvicorn>=0.14.0 (from gradio->-r requirements.txt (line 3))
  Downloading uvicorn-0.52.1-py3-none-any.whl.metadata (6.6 kB)
Requirement already satisfied: exceptiongroup>=1.0.2 in c:\dev\open3d\env\lib\site-packages (from anyio->httpx<1.0.0->diffusers->-r requirements.txt (line 2)) (1.3.1)
Requirement already satisfied: typing-inspection>=0.4.2 in c:\dev\open3d\env\lib\site-packages (from fastapi<1.0,>=0.115.2->gradio->-r requirements.txt (line 3)) (0.4.2)
Collecting annotated-doc>=0.0.2 (from fastapi<1.0,>=0.115.2->gradio->-r requirements.txt (line 3))
  Downloading annotated_doc-0.0.5-py3-none-any.whl.metadata (6.5 kB)
Collecting python-dateutil>=2.8.2 (from pandas<4.0,>=1.0->gradio->-r requirements.txt (line 3))
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting tzdata>=2022.7 (from pandas<4.0,>=1.0->gradio->-r requirements.txt (line 3))
  Using cached tzdata-2026.3-py2.py3-none-any.whl.metadata (1.4 kB)
Requirement already satisfied: annotated-types>=0.6.0 in c:\dev\open3d\env\lib\site-packages (from pydantic<=3.0,>=2.0->gradio->-r requirements.txt (line 3)) (0.8.0)
Requirement already satisfied: pydantic-core==2.46.4 in c:\dev\open3d\env\lib\site-packages (from pydantic<=3.0,>=2.0->gradio->-r requirements.txt (line 3)) (2.46.4)
Collecting shellingham>=1.3.0 (from typer<1.0,>=0.12->gradio->-r requirements.txt (line 3))
  Downloading shellingham-1.5.4-py2.py3-none-any.whl.metadata (3.5 kB)
Collecting rich>=13.8.0 (from typer<1.0,>=0.12->gradio->-r requirements.txt (line 3))
  Using cached rich-15.0.0-py3-none-any.whl.metadata (18 kB)
Collecting contourpy>=1.0.1 (from matplotlib->-r requirements.txt (line 5))
  Downloading contourpy-1.3.2-cp310-cp310-win_amd64.whl.metadata (5.5 kB)
Collecting cycler>=0.10 (from matplotlib->-r requirements.txt (line 5))
  Using cached cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting fonttools>=4.22.0 (from matplotlib->-r requirements.txt (line 5))
  Downloading fonttools-4.63.0-cp310-cp310-win_amd64.whl.metadata (121 kB)
Collecting kiwisolver>=1.3.1 (from matplotlib->-r requirements.txt (line 5))
  Downloading kiwisolver-1.5.0-cp310-cp310-win_amd64.whl.metadata (5.2 kB)
Collecting pyparsing>=3 (from matplotlib->-r requirements.txt (line 5))
  Using cached pyparsing-3.3.2-py3-none-any.whl.metadata (5.8 kB)
Collecting coloredlogs (from onnxruntime->-r requirements.txt (line 7))
  Downloading coloredlogs-15.0.1-py2.py3-none-any.whl.metadata (12 kB)
Collecting flatbuffers (from onnxruntime->-r requirements.txt (line 7))
  Downloading flatbuffers-25.12.19-py2.py3-none-any.whl.metadata (1.0 kB)
Collecting protobuf (from onnxruntime->-r requirements.txt (line 7))
  Downloading protobuf-7.35.1-cp310-abi3-win_amd64.whl.metadata (595 bytes)
Requirement already satisfied: sympy in c:\dev\open3d\env\lib\site-packages (from onnxruntime->-r requirements.txt (line 7)) (1.13.1)
Requirement already satisfied: charset_normalizer<4,>=2 in c:\dev\open3d\env\lib\site-packages (from requests->-r requirements.txt (line 12)) (3.4.9)
Requirement already satisfied: urllib3<3,>=1.26 in c:\dev\open3d\env\lib\site-packages (from requests->-r requirements.txt (line 12)) (2.7.0)
Collecting defusedxml>=0.7.1 (from supervision->-r requirements.txt (line 14))
  Using cached defusedxml-0.7.1-py2.py3-none-any.whl.metadata (32 kB)
Collecting pydeprecate<0.10,>=0.9 (from supervision->-r requirements.txt (line 14))
  Downloading pydeprecate-0.9.0-py3-none-any.whl.metadata (79 kB)
Collecting scipy>=1.10 (from supervision->-r requirements.txt (line 14))
  Downloading scipy-1.15.3-cp310-cp310-win_amd64.whl.metadata (60 kB)
Requirement already satisfied: networkx in c:\dev\open3d\env\lib\site-packages (from torch->-r requirements.txt (line 17)) (3.4.2)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in c:\dev\open3d\env\lib\site-packages (from sympy->onnxruntime->-r requirements.txt (line 7)) (1.3.0)
Collecting tokenizers<=0.23.0,>=0.22.0 (from transformers->-r requirements.txt (line 19))
  Downloading tokenizers-0.22.2-cp39-abi3-win_amd64.whl.metadata (7.4 kB)
Requirement already satisfied: platformdirs>=3.5.1 in c:\dev\open3d\env\lib\site-packages (from yapf->-r requirements.txt (line 20)) (4.11.0)
Collecting tomli>=2.0.1 (from yapf->-r requirements.txt (line 20))
  Using cached tomli-2.4.1-py3-none-any.whl.metadata (10 kB)
Collecting joblib (from nltk->-r requirements.txt (line 21))
  Downloading joblib-1.5.3-py3-none-any.whl.metadata (5.5 kB)
Collecting fastuuid<1.0,>=0.14.0 (from litellm->-r requirements.txt (line 23))
  Downloading fastuuid-0.14.0-cp310-cp310-win_amd64.whl.metadata (1.1 kB)
Collecting openai<3.0.0,>=2.20.0 (from litellm->-r requirements.txt (line 23))
  Downloading openai-2.52.0-py3-none-any.whl.metadata (40 kB)
Collecting python-dotenv<2.0,>=1.0.0 (from litellm->-r requirements.txt (line 23))
  Downloading python_dotenv-1.2.2-py3-none-any.whl.metadata (27 kB)
Collecting tiktoken<1.0,>=0.8.0 (from litellm->-r requirements.txt (line 23))
  Downloading tiktoken-0.13.0-cp310-cp310-win_amd64.whl.metadata (6.8 kB)
Collecting importlib_metadata (from diffusers->-r requirements.txt (line 2))
  Downloading importlib_metadata-8.9.0-py3-none-any.whl.metadata (4.5 kB)
Collecting aiohttp<4.0,>=3.10 (from litellm->-r requirements.txt (line 23))
  Downloading aiohttp-3.14.3-cp310-cp310-win_amd64.whl.metadata (8.5 kB)
Requirement already satisfied: jsonschema<5.0,>=4.0.0 in c:\dev\open3d\env\lib\site-packages (from litellm->-r requirements.txt (line 23)) (4.26.0)
Collecting aiohappyeyeballs>=2.5.0 (from aiohttp<4.0,>=3.10->litellm->-r requirements.txt (line 23))
  Downloading aiohappyeyeballs-2.7.1-py3-none-any.whl.metadata (5.9 kB)
Collecting aiosignal>=1.4.0 (from aiohttp<4.0,>=3.10->litellm->-r requirements.txt (line 23))
  Downloading aiosignal-1.4.0-py3-none-any.whl.metadata (3.7 kB)
Collecting async-timeout<6.0,>=4.0 (from aiohttp<4.0,>=3.10->litellm->-r requirements.txt (line 23))
  Downloading async_timeout-5.0.1-py3-none-any.whl.metadata (5.1 kB)
Requirement already satisfied: attrs>=17.3.0 in c:\dev\open3d\env\lib\site-packages (from aiohttp<4.0,>=3.10->litellm->-r requirements.txt (line 23)) (26.1.0)
Collecting frozenlist>=1.1.1 (from aiohttp<4.0,>=3.10->litellm->-r requirements.txt (line 23))
  Downloading frozenlist-1.8.0-cp310-cp310-win_amd64.whl.metadata (21 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp<4.0,>=3.10->litellm->-r requirements.txt (line 23))
  Downloading multidict-6.7.1-cp310-cp310-win_amd64.whl.metadata (5.5 kB)
Collecting propcache>=0.2.0 (from aiohttp<4.0,>=3.10->litellm->-r requirements.txt (line 23))
  Downloading propcache-0.5.2-cp310-cp310-win_amd64.whl.metadata (17 kB)
Collecting yarl<2.0,>=1.17.0 (from aiohttp<4.0,>=3.10->litellm->-r requirements.txt (line 23))
  Downloading yarl-1.24.5-cp310-cp310-win_amd64.whl.metadata (107 kB)
Requirement already satisfied: zipp>=3.20 in c:\dev\open3d\env\lib\site-packages (from importlib_metadata->diffusers->-r requirements.txt (line 2)) (4.1.0)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\dev\open3d\env\lib\site-packages (from jsonschema<5.0,>=4.0.0->litellm->-r requirements.txt (line 23)) (2025.9.1)
Requirement already satisfied: referencing>=0.28.4 in c:\dev\open3d\env\lib\site-packages (from jsonschema<5.0,>=4.0.0->litellm->-r requirements.txt (line 23)) (0.37.0)
Requirement already satisfied: rpds-py>=0.25.0 in c:\dev\open3d\env\lib\site-packages (from jsonschema<5.0,>=4.0.0->litellm->-r requirements.txt (line 23)) (0.30.0)
Collecting distro<2,>=1.7.0 (from openai<3.0.0,>=2.20.0->litellm->-r requirements.txt (line 23))
  Downloading distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
Collecting jiter<1,>=0.10.0 (from openai<3.0.0,>=2.20.0->litellm->-r requirements.txt (line 23))
  Downloading jiter-0.16.0-cp310-cp310-win_amd64.whl.metadata (5.3 kB)
Collecting sniffio (from openai<3.0.0,>=2.20.0->litellm->-r requirements.txt (line 23))
  Downloading sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas<4.0,>=1.0->gradio->-r requirements.txt (line 3))
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting markdown-it-py>=2.2.0 (from rich>=13.8.0->typer<1.0,>=0.12->gradio->-r requirements.txt (line 3))
  Downloading markdown_it_py-4.2.0-py3-none-any.whl.metadata (7.4 kB)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\dev\open3d\env\lib\site-packages (from rich>=13.8.0->typer<1.0,>=0.12->gradio->-r requirements.txt (line 3)) (2.20.0)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=13.8.0->typer<1.0,>=0.12->gradio->-r requirements.txt (line 3))
  Using cached mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Collecting humanfriendly>=9.1 (from coloredlogs->onnxruntime->-r requirements.txt (line 7))
  Downloading humanfriendly-10.0-py2.py3-none-any.whl.metadata (9.2 kB)
Collecting pyreadline3 (from humanfriendly>=9.1->coloredlogs->onnxruntime->-r requirements.txt (line 7))
  Downloading pyreadline3-3.5.6-py3-none-any.whl.metadata (4.7 kB)
Using cached addict-2.4.0-py3-none-any.whl (3.8 kB)
Downloading diffusers-0.39.0-py3-none-any.whl (5.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.6/5.6 MB 86.6 MB/s  0:00:00
Downloading huggingface_hub-1.26.0-py3-none-any.whl (780 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 780.4/780.4 kB ?  0:00:00
Using cached hf_xet-1.5.2-cp38-abi3-win_amd64.whl (4.0 MB)
Using cached httpx-0.28.1-py3-none-any.whl (73 kB)
Using cached httpcore-1.0.9-py3-none-any.whl (78 kB)
Downloading gradio-6.22.0-py3-none-any.whl (30.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 30.7/30.7 MB 97.6 MB/s  0:00:00
Downloading gradio_client-2.6.0-py3-none-any.whl (61 kB)
Downloading pyyaml-6.0.3-cp310-cp310-win_amd64.whl (158 kB)
Downloading anyio-4.14.2-py3-none-any.whl (125 kB)
Downloading fastapi-0.141.1-py3-none-any.whl (131 kB)
Downloading groovy-0.1.2-py3-none-any.whl (14 kB)
Downloading hf_gradio-0.4.1-py3-none-any.whl (4.5 kB)
Downloading orjson-3.11.9-cp310-cp310-win_amd64.whl (127 kB)
Downloading pandas-2.3.3-cp310-cp310-win_amd64.whl (11.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.3/11.3 MB 101.7 MB/s  0:00:00
Downloading pydub-0.25.1-py2.py3-none-any.whl (32 kB)
Downloading python_multipart-0.0.32-py3-none-any.whl (30 kB)
Downloading safehttpx-0.1.7-py3-none-any.whl (9.0 kB)
Downloading semantic_version-2.10.0-py2.py3-none-any.whl (15 kB)
Downloading starlette-1.3.1-py3-none-any.whl (73 kB)
Downloading tomlkit-0.14.0-py3-none-any.whl (39 kB)
Downloading typer-0.27.1-py3-none-any.whl (122 kB)
Downloading matplotlib-3.10.9-cp310-cp310-win_amd64.whl (8.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.2/8.2 MB 85.4 MB/s  0:00:00
Downloading onnxruntime-1.23.2-cp310-cp310-win_amd64.whl (13.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.5/13.5 MB 105.6 MB/s  0:00:00
Downloading opencv_python-5.0.0.93-cp37-abi3-win_amd64.whl (44.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.0/44.0 MB 90.4 MB/s  0:00:00
Downloading pycocotools-2.0.11-cp310-cp310-win_amd64.whl (80 kB)
Downloading supervision-0.29.1-py3-none-any.whl (280 kB)
Downloading pydeprecate-0.9.0-py3-none-any.whl (102 kB)
Downloading termcolor-3.3.0-py3-none-any.whl (7.7 kB)
Downloading timm-1.0.28-py3-none-any.whl (2.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.6/2.6 MB 73.0 MB/s  0:00:00
Downloading transformers-5.14.1-py3-none-any.whl (11.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.6/11.6 MB 72.4 MB/s  0:00:00
Downloading tokenizers-0.22.2-cp39-abi3-win_amd64.whl (2.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.7/2.7 MB 80.2 MB/s  0:00:00
Using cached yapf-0.43.0-py3-none-any.whl (256 kB)
Downloading nltk-3.10.1-py3-none-any.whl (1.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 47.2 MB/s  0:00:00
Downloading litellm-1.95.0-cp310-cp310-win_amd64.whl (24.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 24.9/24.9 MB 56.3 MB/s  0:00:00
Downloading aiohttp-3.14.3-cp310-cp310-win_amd64.whl (480 kB)
Downloading async_timeout-5.0.1-py3-none-any.whl (6.2 kB)
Downloading fastuuid-0.14.0-cp310-cp310-win_amd64.whl (156 kB)
Downloading importlib_metadata-8.9.0-py3-none-any.whl (27 kB)
Downloading multidict-6.7.1-cp310-cp310-win_amd64.whl (46 kB)
Downloading openai-2.52.0-py3-none-any.whl (1.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 30.4 MB/s  0:00:00
Downloading distro-1.9.0-py3-none-any.whl (20 kB)
Downloading jiter-0.16.0-cp310-cp310-win_amd64.whl (199 kB)
Downloading python_dotenv-1.2.2-py3-none-any.whl (22 kB)
Downloading tiktoken-0.13.0-cp310-cp310-win_amd64.whl (876 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 876.6/876.6 kB 41.0 MB/s  0:00:00
Downloading yarl-1.24.5-cp310-cp310-win_amd64.whl (97 kB)
Downloading aiohappyeyeballs-2.7.1-py3-none-any.whl (15 kB)
Downloading aiosignal-1.4.0-py3-none-any.whl (7.5 kB)
Downloading annotated_doc-0.0.5-py3-none-any.whl (5.3 kB)
Downloading brotli-1.2.0-cp310-cp310-win_amd64.whl (369 kB)
Downloading contourpy-1.3.2-cp310-cp310-win_amd64.whl (221 kB)
Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)
Using cached defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
Downloading fonttools-4.63.0-cp310-cp310-win_amd64.whl (1.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 40.8 MB/s  0:00:00
Downloading frozenlist-1.8.0-cp310-cp310-win_amd64.whl (43 kB)
Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Downloading kiwisolver-1.5.0-cp310-cp310-win_amd64.whl (73 kB)
Downloading propcache-0.5.2-cp310-cp310-win_amd64.whl (42 kB)
Using cached pyparsing-3.3.2-py3-none-any.whl (122 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached pytz-2026.3.post1-py2.py3-none-any.whl (508 kB)
Downloading regex-2026.7.19-cp310-cp310-win_amd64.whl (277 kB)
Using cached rich-15.0.0-py3-none-any.whl (310 kB)
Downloading markdown_it_py-4.2.0-py3-none-any.whl (91 kB)
Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Downloading safetensors-0.8.0-cp310-abi3-win_amd64.whl (355 kB)
Downloading scipy-1.15.3-cp310-cp310-win_amd64.whl (41.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.3/41.3 MB 51.5 MB/s  0:00:00
Downloading shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached tomli-2.4.1-py3-none-any.whl (14 kB)
Using cached tqdm-4.70.0-py3-none-any.whl (80 kB)
Using cached tzdata-2026.3-py2.py3-none-any.whl (348 kB)
Downloading uvicorn-0.52.1-py3-none-any.whl (79 kB)
Downloading coloredlogs-15.0.1-py2.py3-none-any.whl (46 kB)
Downloading humanfriendly-10.0-py2.py3-none-any.whl (86 kB)
Downloading flatbuffers-25.12.19-py2.py3-none-any.whl (26 kB)
Downloading joblib-1.5.3-py3-none-any.whl (309 kB)
Downloading protobuf-7.35.1-cp310-abi3-win_amd64.whl (439 kB)
Downloading pyreadline3-3.5.6-py3-none-any.whl (85 kB)
Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)
Building wheels for collected packages: fairscale
  Building wheel for fairscale (pyproject.toml) ... done
  Created wheel for fairscale: filename=fairscale-0.4.13-py3-none-any.whl size=332215 sha256=06f8450eec336d3d49e9021abc3773b60b4a22491bc72b6d337ea3c8f5744cfc
  Stored in directory: c:\users\vlin\appdata\local\pip\cache\wheels\78\a4\c0\fb0a7ef03cff161611c3fa40c6cf898f76e58ec421b88e8cb3
Successfully built fairscale
Installing collected packages: pytz, pydub, flatbuffers, brotli, addict, tzdata, tqdm, tomlkit, tomli, termcolor, sniffio, six, shellingham, semantic-version, scipy, safetensors, regex, PyYAML, python-multipart, python-dotenv, pyreadline3, pyparsing, pydeprecate, pycocotools, protobuf, propcache, orjson, opencv_python, multidict, mdurl, kiwisolver, joblib, jiter, importlib_metadata, hf-xet, h11, groovy, frozenlist, fonttools, fastuuid, distro, defusedxml, cycler, contourpy, async-timeout, annotated-doc, aiohappyeyeballs, yarl, yapf, uvicorn, tiktoken, python-dateutil, nltk, markdown-it-py, humanfriendly, httpcore, anyio, aiosignal, starlette, rich, pandas, matplotlib, httpx, fairscale, coloredlogs, aiohttp, typer, supervision, safehttpx, openai, onnxruntime, huggingface_hub, fastapi, tokenizers, timm, gradio-client, diffusers, transformers, litellm, hf-gradio, gradio
  Attempting uninstall: importlib_metadata
    Found existing installation: importlib_metadata 9.0.0
    Uninstalling importlib_metadata-9.0.0:
      Successfully uninstalled importlib_metadata-9.0.0
Successfully installed PyYAML-6.0.3 addict-2.4.0 aiohappyeyeballs-2.7.1 aiohttp-3.14.3 aiosignal-1.4.0 annotated-doc-0.0.5 anyio-4.14.2 async-timeout-5.0.1 brotli-1.2.0 coloredlogs-15.0.1 contourpy-1.3.2 cycler-0.12.1 defusedxml-0.7.1 diffusers-0.39.0 distro-1.9.0 fairscale-0.4.13 fastapi-0.141.1 fastuuid-0.14.0 flatbuffers-25.12.19 fonttools-4.63.0 frozenlist-1.8.0 gradio-6.22.0 gradio-client-2.6.0 groovy-0.1.2 h11-0.16.0 hf-gradio-0.4.1 hf-xet-1.5.2 httpcore-1.0.9 httpx-0.28.1 huggingface_hub-1.26.0 humanfriendly-10.0 importlib_metadata-8.9.0 jiter-0.16.0 joblib-1.5.3 kiwisolver-1.5.0 litellm-1.95.0 markdown-it-py-4.2.0 matplotlib-3.10.9 mdurl-0.1.2 multidict-6.7.1 nltk-3.10.1 onnxruntime-1.23.2 openai-2.52.0 opencv_python-5.0.0.93 orjson-3.11.9 pandas-2.3.3 propcache-0.5.2 protobuf-7.35.1 pycocotools-2.0.11 pydeprecate-0.9.0 pydub-0.25.1 pyparsing-3.3.2 pyreadline3-3.5.6 python-dateutil-2.9.0.post0 python-dotenv-1.2.2 python-multipart-0.0.32 pytz-2026.3.post1 regex-2026.7.19 rich-15.0.0 safehttpx-0.1.7 safetensors-0.8.0 scipy-1.15.3 semantic-version-2.10.0 shellingham-1.5.4 six-1.17.0 sniffio-1.3.1 starlette-1.3.1 supervision-0.29.1 termcolor-3.3.0 tiktoken-0.13.0 timm-1.0.28 tokenizers-0.22.2 tomli-2.4.1 tomlkit-0.14.0 tqdm-4.70.0 transformers-5.14.1 typer-0.27.1 tzdata-2026.3 uvicorn-0.52.1 yapf-0.43.0 yarl-1.24.5
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> 
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> python -m pip install -e .\segment_anything
Obtaining file:///C:/Users/vlin/OneDrive%20-%20University%20of%20Bradford/Desktop/HBIM/Grounded-SAM/Grounded-Segment-Anything/segment_anything
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
Building wheels for collected packages: segment_anything
  Building editable for segment_anything (pyproject.toml) ... done
  Created wheel for segment_anything: filename=segment_anything-1.0-0.editable-py3-none-any.whl size=7138 sha256=9c914c48e6e8f001631449b13ec614690f5148c149a960e78717167d7b4d16ea
  Stored in directory: C:\Users\vlin\AppData\Local\Temp\pip-ephem-wheel-cache-z9ekiydc\wheels\99\43\b5\d2496b0005ad9eba45cada105ac49ea1ef3088d0d99e98ef3c
Successfully built segment_anything
Installing collected packages: segment_anything
Successfully installed segment_anything-1.0
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> python -m pip install --no-build-isolation -e .\GroundingDINO                                                                  
Obtaining file:///C:/Users/vlin/OneDrive%20-%20University%20of%20Bradford/Desktop/HBIM/Grounded-SAM/Grounded-Segment-Anything/GroundingDINO
  Checking if build backend supports build_editable ... done
  Preparing editable metadata (pyproject.toml) ... done
Requirement already satisfied: torch in c:\dev\open3d\env\lib\site-packages (from groundingdino==0.1.0) (2.5.1+cu124)
Requirement already satisfied: torchvision in c:\dev\open3d\env\lib\site-packages (from groundingdino==0.1.0) (0.20.1+cu124)
Requirement already satisfied: transformers in c:\dev\open3d\env\lib\site-packages (from groundingdino==0.1.0) (5.14.1)
Requirement already satisfied: addict in c:\dev\open3d\env\lib\site-packages (from groundingdino==0.1.0) (2.4.0)
Requirement already satisfied: yapf in c:\dev\open3d\env\lib\site-packages (from groundingdino==0.1.0) (0.43.0)
Requirement already satisfied: timm in c:\dev\open3d\env\lib\site-packages (from groundingdino==0.1.0) (1.0.28)
Requirement already satisfied: numpy in c:\dev\open3d\env\lib\site-packages (from groundingdino==0.1.0) (2.2.6)
Requirement already satisfied: opencv-python in c:\dev\open3d\env\lib\site-packages (from groundingdino==0.1.0) (5.0.0.93)
Requirement already satisfied: supervision in c:\dev\open3d\env\lib\site-packages (from groundingdino==0.1.0) (0.29.1)
Requirement already satisfied: pycocotools in c:\dev\open3d\env\lib\site-packages (from groundingdino==0.1.0) (2.0.11)
Requirement already satisfied: defusedxml>=0.7.1 in c:\dev\open3d\env\lib\site-packages (from supervision->groundingdino==0.1.0) (0.7.1)
Requirement already satisfied: matplotlib>=3.6 in c:\dev\open3d\env\lib\site-packages (from supervision->groundingdino==0.1.0) (3.10.9)
Requirement already satisfied: pillow>=9.4 in c:\dev\open3d\env\lib\site-packages (from supervision->groundingdino==0.1.0) (12.2.0)
Requirement already satisfied: pydeprecate<0.10,>=0.9 in c:\dev\open3d\env\lib\site-packages (from supervision->groundingdino==0.1.0) (0.9.0)
Requirement already satisfied: pyyaml>=5.3 in c:\dev\open3d\env\lib\site-packages (from supervision->groundingdino==0.1.0) (6.0.3)
Requirement already satisfied: requests>=2.26 in c:\dev\open3d\env\lib\site-packages (from supervision->groundingdino==0.1.0) (2.34.2)
Requirement already satisfied: scipy>=1.10 in c:\dev\open3d\env\lib\site-packages (from supervision->groundingdino==0.1.0) (1.15.3)
Requirement already satisfied: tqdm>=4.62.3 in c:\dev\open3d\env\lib\site-packages (from supervision->groundingdino==0.1.0) (4.70.0)
Requirement already satisfied: contourpy>=1.0.1 in c:\dev\open3d\env\lib\site-packages (from matplotlib>=3.6->supervision->groundingdino==0.1.0) (1.3.2)
Requirement already satisfied: cycler>=0.10 in c:\dev\open3d\env\lib\site-packages (from matplotlib>=3.6->supervision->groundingdino==0.1.0) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in c:\dev\open3d\env\lib\site-packages (from matplotlib>=3.6->supervision->groundingdino==0.1.0) (4.63.0)
Requirement already satisfied: kiwisolver>=1.3.1 in c:\dev\open3d\env\lib\site-packages (from matplotlib>=3.6->supervision->groundingdino==0.1.0) (1.5.0)
Requirement already satisfied: packaging>=20.0 in c:\dev\open3d\env\lib\site-packages (from matplotlib>=3.6->supervision->groundingdino==0.1.0) (26.2)
Requirement already satisfied: pyparsing>=3 in c:\dev\open3d\env\lib\site-packages (from matplotlib>=3.6->supervision->groundingdino==0.1.0) (3.3.2)
Requirement already satisfied: python-dateutil>=2.7 in c:\dev\open3d\env\lib\site-packages (from matplotlib>=3.6->supervision->groundingdino==0.1.0) (2.9.0.post0)
Requirement already satisfied: six>=1.5 in c:\dev\open3d\env\lib\site-packages (from python-dateutil>=2.7->matplotlib>=3.6->supervision->groundingdino==0.1.0) (1.17.0)
Requirement already satisfied: charset_normalizer<4,>=2 in c:\dev\open3d\env\lib\site-packages (from requests>=2.26->supervision->groundingdino==0.1.0) (3.4.9)
Requirement already satisfied: idna<4,>=2.5 in c:\dev\open3d\env\lib\site-packages (from requests>=2.26->supervision->groundingdino==0.1.0) (3.18)
Requirement already satisfied: urllib3<3,>=1.26 in c:\dev\open3d\env\lib\site-packages (from requests>=2.26->supervision->groundingdino==0.1.0) (2.7.0)
Requirement already satisfied: certifi>=2023.5.7 in c:\dev\open3d\env\lib\site-packages (from requests>=2.26->supervision->groundingdino==0.1.0) (2026.7.22)
Requirement already satisfied: colorama in c:\dev\open3d\env\lib\site-packages (from tqdm>=4.62.3->supervision->groundingdino==0.1.0) (0.4.6)
Requirement already satisfied: huggingface_hub in c:\dev\open3d\env\lib\site-packages (from timm->groundingdino==0.1.0) (1.26.0)
Requirement already satisfied: safetensors in c:\dev\open3d\env\lib\site-packages (from timm->groundingdino==0.1.0) (0.8.0)
Requirement already satisfied: click<9.0.0,>=8.4.2 in c:\dev\open3d\env\lib\site-packages (from huggingface_hub->timm->groundingdino==0.1.0) (8.4.2)
Requirement already satisfied: filelock>=3.10.0 in c:\dev\open3d\env\lib\site-packages (from huggingface_hub->timm->groundingdino==0.1.0) (3.29.0)
Requirement already satisfied: fsspec>=2023.5.0 in c:\dev\open3d\env\lib\site-packages (from huggingface_hub->timm->groundingdino==0.1.0) (2026.4.0)
Requirement already satisfied: hf-xet<2.0.0,>=1.5.1 in c:\dev\open3d\env\lib\site-packages (from huggingface_hub->timm->groundingdino==0.1.0) (1.5.2)
Requirement already satisfied: httpx<1,>=0.23.0 in c:\dev\open3d\env\lib\site-packages (from huggingface_hub->timm->groundingdino==0.1.0) (0.28.1)
Requirement already satisfied: typing-extensions>=4.1.0 in c:\dev\open3d\env\lib\site-packages (from huggingface_hub->timm->groundingdino==0.1.0) (4.16.0)
Requirement already satisfied: anyio in c:\dev\open3d\env\lib\site-packages (from httpx<1,>=0.23.0->huggingface_hub->timm->groundingdino==0.1.0) (4.14.2)
Requirement already satisfied: httpcore==1.* in c:\dev\open3d\env\lib\site-packages (from httpx<1,>=0.23.0->huggingface_hub->timm->groundingdino==0.1.0) (1.0.9)
Requirement already satisfied: h11>=0.16 in c:\dev\open3d\env\lib\site-packages (from httpcore==1.*->httpx<1,>=0.23.0->huggingface_hub->timm->groundingdino==0.1.0) (0.16.0)
Requirement already satisfied: exceptiongroup>=1.0.2 in c:\dev\open3d\env\lib\site-packages (from anyio->httpx<1,>=0.23.0->huggingface_hub->timm->groundingdino==0.1.0) (1.3.1)
Requirement already satisfied: networkx in c:\dev\open3d\env\lib\site-packages (from torch->groundingdino==0.1.0) (3.4.2)
Requirement already satisfied: jinja2 in c:\dev\open3d\env\lib\site-packages (from torch->groundingdino==0.1.0) (3.1.6)
Requirement already satisfied: sympy==1.13.1 in c:\dev\open3d\env\lib\site-packages (from torch->groundingdino==0.1.0) (1.13.1)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in c:\dev\open3d\env\lib\site-packages (from sympy==1.13.1->torch->groundingdino==0.1.0) (1.3.0)
Requirement already satisfied: MarkupSafe>=2.0 in c:\dev\open3d\env\lib\site-packages (from jinja2->torch->groundingdino==0.1.0) (3.0.3)
Requirement already satisfied: regex>=2025.10.22 in c:\dev\open3d\env\lib\site-packages (from transformers->groundingdino==0.1.0) (2026.7.19)
Requirement already satisfied: tokenizers<=0.23.0,>=0.22.0 in c:\dev\open3d\env\lib\site-packages (from transformers->groundingdino==0.1.0) (0.22.2)
Requirement already satisfied: typer in c:\dev\open3d\env\lib\site-packages (from transformers->groundingdino==0.1.0) (0.27.1)
Requirement already satisfied: shellingham>=1.3.0 in c:\dev\open3d\env\lib\site-packages (from typer->transformers->groundingdino==0.1.0) (1.5.4)
Requirement already satisfied: rich>=13.8.0 in c:\dev\open3d\env\lib\site-packages (from typer->transformers->groundingdino==0.1.0) (15.0.0)
Requirement already satisfied: annotated-doc>=0.0.2 in c:\dev\open3d\env\lib\site-packages (from typer->transformers->groundingdino==0.1.0) (0.0.5)
Requirement already satisfied: markdown-it-py>=2.2.0 in c:\dev\open3d\env\lib\site-packages (from rich>=13.8.0->typer->transformers->groundingdino==0.1.0) (4.2.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\dev\open3d\env\lib\site-packages (from rich>=13.8.0->typer->transformers->groundingdino==0.1.0) (2.20.0)
Requirement already satisfied: mdurl~=0.1 in c:\dev\open3d\env\lib\site-packages (from markdown-it-py>=2.2.0->rich>=13.8.0->typer->transformers->groundingdino==0.1.0) (0.1.2)
Requirement already satisfied: platformdirs>=3.5.1 in c:\dev\open3d\env\lib\site-packages (from yapf->groundingdino==0.1.0) (4.11.0)
Requirement already satisfied: tomli>=2.0.1 in c:\dev\open3d\env\lib\site-packages (from yapf->groundingdino==0.1.0) (2.4.1)
Building wheels for collected packages: groundingdino
  Building editable for groundingdino (pyproject.toml) ... done
  Created wheel for groundingdino: filename=groundingdino-0.1.0-0.editable-py3-none-any.whl size=11231 sha256=7907c9cc2002dcd464c41499416192410265d2e613b65a643d3da88ad00bcecb
  Stored in directory: C:\Users\vlin\AppData\Local\Temp\pip-ephem-wheel-cache-zmvd4ztz\wheels\5b\59\66\da7b079d02a34de06604f34ecee58af68844416f234ddca87b
Successfully built groundingdino
Installing collected packages: groundingdino
Successfully installed groundingdino-0.1.0
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> New-Item -ItemType Directory -Force -Path ".\weights"


    Directory: C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything


Mode                 LastWriteTime         Length Name                                                                      
----                 -------------         ------ ----                                                                      
d-----        03/08/2026     18:01                weights                                                                   
                                                                                                                            

(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> Invoke-WebRequest `
>>   -Uri "https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth" `
>>   -OutFile ".\weights\groundingdino_swint_ogc.pth"
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> New-Item -ItemType Directory -Force -Path ".\weights"


    Directory: C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything

                                                                                                                            
Mode                 LastWriteTime         Length Name                                                                      
----                 -------------         ------ ----                                                                      
dar--l        03/08/2026     18:01                weights                                                                   
                                                                                                                            
                                                                                                                            
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> Invoke-WebRequest `  -Uri "https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth" `  -OutFile ".\weights\groundingdino_swint_ogc.pth"
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> Invoke-WebRequest `
>>   -Uri "https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth" `
>>   -OutFile ".\weights\sam_vit_b_01ec64.pth"
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> python -c "import torch, groundingdino, segment_anything; print('Imports OK'); print('CUDA:', torch.cuda.is_available())"
Imports OK
CUDA: True
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> python .\grounded_sam_demo.py `
>>   --config ".\GroundingDINO\groundingdino\config\GroundingDINO_SwinT_OGC.py" `
>>   --grounded_checkpoint ".\weights\groundingdino_swint_ogc.pth" `
>>   --sam_version "vit_b" `
>>   --sam_checkpoint ".\weights\sam_vit_b_01ec64.pth" `
>>   --input_image ".\assets\demo1.jpg" `
>>   --output_dir ".\outputs" `
>>   --box_threshold 0.3 `
>>   --text_threshold 0.25 `
>>   --text_prompt "bear" `
>>   --device "cpu"
Matplotlib is building the font cache; this may take a moment.
C:\dev\open3D\env\lib\site-packages\timm\models\layers\__init__.py:49: FutureWarning: Importing from timm.models.layers is deprecated, please import via timm.layers
  warnings.warn(f"Importing from {__name__} is deprecated, please import via timm.layers", FutureWarning)
C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything\GroundingDINO\groundingdino\models\GroundingDINO\ms_deform_attn.py:31: UserWarning: Failed to load custom C++ ops. Running on CPU mode Only!
  warnings.warn("Failed to load custom C++ ops. Running on CPU mode Only!")
C:\dev\open3D\env\lib\site-packages\torch\functional.py:534: UserWarning: torch.meshgrid: in an upcoming release, it will be required to pass the indexing argument. (Triggered internally at C:\actions-runner\_work\pytorch\pytorch\builder\windows\pytorch\aten\src\ATen\native\TensorShape.cpp:3596.)
  return _VF.meshgrid(tensors, **kwargs)  # type: ignore[attr-defined]
final text_encoder_type: bert-base-uncased
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
config.json: 100%|████████████████████████████████████████████████████████████████████████████████| 570/570 [00:00<?, ?B/s]
C:\dev\open3D\env\lib\site-packages\huggingface_hub\file_download.py:141: UserWarning: `huggingface_hub` cache-system uses symlinks by default to efficiently store duplicated files but your machine does not support them in C:\Users\vlin\.cache\huggingface\hub\models--bert-base-uncased. Caching files will still work but in a degraded version that might require more space on your disk. This warning can be disabled by setting the `HF_HUB_DISABLE_SYMLINKS_WARNING` environment variable. For more details, see https://huggingface.co/docs/huggingface_hub/how-to-cache#limitations.
To support symlinks on Windows, you either need to activate Developer Mode or to run Python as an administrator. In order to activate developer mode, see this article: https://docs.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development
  warnings.warn(message)
tokenizer_config.json: 100%|█████████████████████████████████████████████████████████████| 48.0/48.0 [00:00<00:00, 102kB/s]
vocab.txt: 100%|████████████████████████████████████████████████████████████████████████| 232k/232k [00:00<00:00, 4.75MB/s]
tokenizer.json: 100%|███████████████████████████████████████████████████████████████████| 466k/466k [00:00<00:00, 3.10MB/s]
model.safetensors: downloading bytes: █████████████████████████████████████████████████████████████████|  415MB, 31.2MB/s  
model.safetensors: reconstructing file: 100%|█████████████████████████████████████████████████|  440MB /  440MB, 37.4MB/s  
Loading weights: 100%|████████████████████████████████████████████████████████████████| 199/199 [00:00<00:00, 21402.25it/s]
[transformers] BertModel LOAD REPORT from: bert-base-uncased
Key                                        | Status     |  | 
-------------------------------------------+------------+--+-
cls.predictions.transform.dense.bias       | UNEXPECTED |  | 
cls.predictions.transform.dense.weight     | UNEXPECTED |  | 
cls.seq_relationship.weight                | UNEXPECTED |  | 
cls.predictions.transform.LayerNorm.weight | UNEXPECTED |  | 
cls.predictions.bias                       | UNEXPECTED |  | 
cls.predictions.transform.LayerNorm.bias   | UNEXPECTED |  | 
cls.seq_relationship.bias                  | UNEXPECTED |  | 

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
Traceback (most recent call last):
  File "C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything\grounded_sam_demo.py", line 192, in <module>
    model = load_model(config_file, grounded_checkpoint, bert_base_uncased_path, device=device)
  File "C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything\grounded_sam_demo.py", line 51, in load_model
    model = build_model(args)
  File "C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything\GroundingDINO\groundingdino\models\__init__.py", line 17, in build_model
    model = build_func(args)
  File "C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything\GroundingDINO\groundingdino\models\GroundingDINO\groundingdino.py", line 374, in build_groundingdino
    model = GroundingDINO(
  File "C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything\GroundingDINO\groundingdino\models\GroundingDINO\groundingdino.py", line 112, in __init__
    self.bert = BertModelWarper(bert_model=self.bert)
  File "C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything\GroundingDINO\groundingdino\models\GroundingDINO\bertwarper.py", line 29, in __init__
    self.get_head_mask = bert_model.get_head_mask
  File "C:\dev\open3D\env\lib\site-packages\torch\nn\modules\module.py", line 1931, in __getattr__
    raise AttributeError(
AttributeError: 'BertModel' object has no attribute 'get_head_mask'
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> python -m pip install "transformers==4.40.2" "tokenizers==0.19.1" "huggingface-hub==0.36.0"
Collecting transformers==4.40.2
  Downloading transformers-4.40.2-py3-none-any.whl.metadata (137 kB)
Collecting tokenizers==0.19.1
  Downloading tokenizers-0.19.1-cp310-none-win_amd64.whl.metadata (6.9 kB)
Collecting huggingface-hub==0.36.0
  Downloading huggingface_hub-0.36.0-py3-none-any.whl.metadata (14 kB)
Requirement already satisfied: filelock in c:\dev\open3d\env\lib\site-packages (from transformers==4.40.2) (3.29.0)
Requirement already satisfied: numpy>=1.17 in c:\dev\open3d\env\lib\site-packages (from transformers==4.40.2) (2.2.6)
Requirement already satisfied: packaging>=20.0 in c:\dev\open3d\env\lib\site-packages (from transformers==4.40.2) (26.2)
Requirement already satisfied: pyyaml>=5.1 in c:\dev\open3d\env\lib\site-packages (from transformers==4.40.2) (6.0.3)
Requirement already satisfied: regex!=2019.12.17 in c:\dev\open3d\env\lib\site-packages (from transformers==4.40.2) (2026.7.19)
Requirement already satisfied: requests in c:\dev\open3d\env\lib\site-packages (from transformers==4.40.2) (2.34.2)
Requirement already satisfied: safetensors>=0.4.1 in c:\dev\open3d\env\lib\site-packages (from transformers==4.40.2) (0.8.0)
Requirement already satisfied: tqdm>=4.27 in c:\dev\open3d\env\lib\site-packages (from transformers==4.40.2) (4.70.0)
Requirement already satisfied: fsspec>=2023.5.0 in c:\dev\open3d\env\lib\site-packages (from huggingface-hub==0.36.0) (2026.4.0)
Requirement already satisfied: typing-extensions>=3.7.4.3 in c:\dev\open3d\env\lib\site-packages (from huggingface-hub==0.36.0) (4.16.0)
Requirement already satisfied: colorama in c:\dev\open3d\env\lib\site-packages (from tqdm>=4.27->transformers==4.40.2) (0.4.6)
Requirement already satisfied: charset_normalizer<4,>=2 in c:\dev\open3d\env\lib\site-packages (from requests->transformers==4.40.2) (3.4.9)
Requirement already satisfied: idna<4,>=2.5 in c:\dev\open3d\env\lib\site-packages (from requests->transformers==4.40.2) (3.18)
Requirement already satisfied: urllib3<3,>=1.26 in c:\dev\open3d\env\lib\site-packages (from requests->transformers==4.40.2) (2.7.0)
Requirement already satisfied: certifi>=2023.5.7 in c:\dev\open3d\env\lib\site-packages (from requests->transformers==4.40.2) (2026.7.22)
Downloading transformers-4.40.2-py3-none-any.whl (9.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.0/9.0 MB 56.0 MB/s  0:00:00
Downloading tokenizers-0.19.1-cp310-none-win_amd64.whl (2.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 130.5 MB/s  0:00:00
Downloading huggingface_hub-0.36.0-py3-none-any.whl (566 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 566.1/566.1 kB ?  0:00:00
Installing collected packages: huggingface-hub, tokenizers, transformers
  Attempting uninstall: huggingface-hub
    Found existing installation: huggingface_hub 1.26.0
    Uninstalling huggingface_hub-1.26.0:
      Successfully uninstalled huggingface_hub-1.26.0
  Attempting uninstall: tokenizers
    Found existing installation: tokenizers 0.22.2
    Uninstalling tokenizers-0.22.2:
      Successfully uninstalled tokenizers-0.22.2
  Attempting uninstall: transformers
    Found existing installation: transformers 5.14.1
    Uninstalling transformers-5.14.1:
      Successfully uninstalled transformers-5.14.1
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
gradio 6.22.0 requires huggingface-hub<2.0,>=1.16.0, but you have huggingface-hub 0.36.0 which is incompatible.
litellm 1.95.0 requires tokenizers<1.0,>=0.21.0, but you have tokenizers 0.19.1 which is incompatible.
Successfully installed huggingface-hub-0.36.0 tokenizers-0.19.1 transformers-4.40.2
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> python -c "import transformers, tokenizers, huggingface_hub; print(transformers.__version__); print(tokenizers.__version__); print(huggingface_hub.__version__)"
The cache for model files in Transformers v4.22.0 has been updated. Migrating your old cache. This is a one-time only operation. You can interrupt this and resume the migration later on by calling `transformers.utils.move_cache()`.
0it [00:00, ?it/s]
4.40.2
0.19.1
0.36.0
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> python .\grounded_sam_demo.py `
>>   --config ".\GroundingDINO\groundingdino\config\GroundingDINO_SwinT_OGC.py" `
>>   --grounded_checkpoint ".\weights\groundingdino_swint_ogc.pth" `
>>   --sam_version "vit_b" `
>>   --sam_checkpoint ".\weights\sam_vit_b_01ec64.pth" `
>>   --input_image ".\assets\demo1.jpg" `
>>   --output_dir ".\outputs" `
>>   --box_threshold 0.3 `
>>   --text_threshold 0.25 `
>>   --text_prompt "bear" `
>>   --device "cpu"
C:\dev\open3D\env\lib\site-packages\timm\models\layers\__init__.py:49: FutureWarning: Importing from timm.models.layers is deprecated, please import via timm.layers
  warnings.warn(f"Importing from {__name__} is deprecated, please import via timm.layers", FutureWarning)
C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything\GroundingDINO\groundingdino\models\GroundingDINO\ms_deform_attn.py:31: UserWarning: Failed to load custom C++ ops. Running on CPU mode Only!
  warnings.warn("Failed to load custom C++ ops. Running on CPU mode Only!")
C:\dev\open3D\env\lib\site-packages\torch\functional.py:534: UserWarning: torch.meshgrid: in an upcoming release, it will be required to pass the indexing argument. (Triggered internally at C:\actions-runner\_work\pytorch\pytorch\builder\windows\pytorch\aten\src\ATen\native\TensorShape.cpp:3596.)
  return _VF.meshgrid(tensors, **kwargs)  # type: ignore[attr-defined]
final text_encoder_type: bert-base-uncased
C:\dev\open3D\env\lib\site-packages\huggingface_hub\file_download.py:942: FutureWarning: `resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.
  warnings.warn(
C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything\grounded_sam_demo.py:52: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  checkpoint = torch.load(model_checkpoint_path, map_location="cpu")
_IncompatibleKeys(missing_keys=[], unexpected_keys=['label_enc.weight', 'bert.embeddings.position_ids'])
C:\dev\open3D\env\lib\site-packages\transformers\modeling_utils.py:1051: FutureWarning: The `device` argument is deprecated and will be removed in v5 of Transformers.
  warnings.warn(
C:\dev\open3D\env\lib\site-packages\torch\_dynamo\eval_frame.py:632: UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. In version 2.5 we will raise an exception if use_reentrant is not passed. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
  return fn(*args, **kwargs)
C:\dev\open3D\env\lib\site-packages\torch\utils\checkpoint.py:87: UserWarning: None of the inputs have requires_grad=True. Gradients will be None
  warnings.warn(
C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything\GroundingDINO\groundingdino\models\GroundingDINO\transformer.py:863: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
  with torch.cuda.amp.autocast(enabled=False):
C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything\segment_anything\segment_anything\build_sam.py:105: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  state_dict = torch.load(f)
(env) (base) PS C:\Users\vlin\OneDrive - University of Bradford\Desktop\HBIM\Grounded-SAM\Grounded-Segment-Anything> 