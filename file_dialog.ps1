#--------------------------------------
# �t�@�C���I���_�C�A���O��\��
#--------------------------------------
function show_file_dialog() {
    # �A�Z���u���̃��[�h
    Add-Type -assemblyName System.Windows.Forms

    # �C���X�^���X����
    $FileDialog = New-Object System.Windows.Forms.OpenFileDialog

    # �t�B���^�ݒ�
    $FileDialog.Filter = "CSV Files|*.csv|All Files|*.*"

    # �\��
    if ($FileDialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK) {
        Write-Output $FileDialog.FileName
    }

    $FileDialog.Dispose()
}


#--------------------------------------
# �t�H���_�I���_�C�A���O��\��
#--------------------------------------
function show_folder_dialog{
    # �A�Z���u���̃��[�h
    Add-Type -assemblyName System.Windows.Forms

    # �C���X�^���X����
    $FolderDialog = New-Object System.Windows.Forms.FolderBrowserDialog

    # �\��
    if ($FolderDialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK) {
        Write-Host $FolderDialog.SelectedPath
    }

    $FolderDialog.Dispose()
}

show_file_dialog
show_folder_dialog