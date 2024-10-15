#--------------------------------------
# ファイル選択ダイアログを表示
#--------------------------------------
function show_file_dialog() {
    # アセンブリのロード
    Add-Type -assemblyName System.Windows.Forms

    # インスタンス生成
    $FileDialog = New-Object System.Windows.Forms.OpenFileDialog

    # フィルタ設定
    $FileDialog.Filter = "CSV Files|*.csv|All Files|*.*"

    # 表示
    if ($FileDialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK) {
        Write-Output $FileDialog.FileName
    }

    $FileDialog.Dispose()
}


#--------------------------------------
# フォルダ選択ダイアログを表示
#--------------------------------------
function show_folder_dialog{
    # アセンブリのロード
    Add-Type -assemblyName System.Windows.Forms

    # インスタンス生成
    $FolderDialog = New-Object System.Windows.Forms.FolderBrowserDialog

    # 表示
    if ($FolderDialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK) {
        Write-Host $FolderDialog.SelectedPath
    }

    $FolderDialog.Dispose()
}

show_file_dialog
show_folder_dialog