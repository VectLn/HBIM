$stopwatch = [System.Diagnostics.Stopwatch]::StartNew()

Write-Host "--- [1/4] Etape 1 : Execution de 2DRenderer.py ---"
python 2DRenderer.py

Write-Host "`n--- [2/4] Etape 2 : Execution de Grounded-SAM (views 000 a ...) ---"
0..29 | ForEach-Object {
    $view_id = "{0:D3}" -f $_
    $img_path = ".\images\view_${view_id}.png"
    
    if (Test-Path $img_path) {
        Write-Host "Traitement de view_${view_id}.png..."
        python .\Grounded-Segment-Anything\grounded_sam_demo.py `
            --config ".\Grounded-Segment-Anything\GroundingDINO\groundingdino\config\GroundingDINO_SwinT_OGC.py" `
            --grounded_checkpoint ".\Grounded-Segment-Anything\weights\groundingdino_swint_ogc.pth" `
            --sam_version "vit_b" `
            --sam_checkpoint ".\Grounded-Segment-Anything\weights\sam_vit_b_01ec64.pth" `
            --input_image $img_path `
            --output_dir ".\masks" `
            --box_threshold 0.3 `
            --text_threshold 0.25 `
            --text_prompt "sign . traffic_light . streetlight . window . table . car . tree" `
            --device "cpu"
    } else {
        Write-Host "Avertissement : $img_path introuvable."
    }
}

Write-Host "`n--- [3/4] Etape 3 : Execution de voting.py ---"
python voting.py

$stopwatch.Stop()
Write-Host ("`nTemps total d'execution : {0:hh\:mm\:ss\.fff}" -f $stopwatch.Elapsed)

Write-Host "`n--- [4/4] Etape 4 : Execution de colorPointCloud.py ---"
python colorPointCloud.py

Write-Host "`nPipeline execute avec succes."
