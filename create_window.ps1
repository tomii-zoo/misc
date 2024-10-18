# �E�B���h�E��\��
function show_window($title) {
    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing

    # �E�B���h�E�ݒ�
    $form = New-Object System.Windows.Forms.Form
    $form.Text = $title
    $form.Size = New-Object System.Drawing.Size(420,200)

    # ���x���z�u
    $lbl = New-Object System.Windows.Forms.Label
    $lbl.Location = New-Object System.Drawing.Point(20,33)
    $lbl.Text = '�C���X�g�[����t�H���_�F'
    $lbl.AutoSize = $True
    $form.Controls.Add($lbl)

    # �e�L�X�g�{�b�N�X�z�u
    $box = New-Object System.Windows.Forms.TextBox
    $box.Location = New-Object System.Drawing.Point(150,30)
    $box.Size = New-Object System.Drawing.Size(240,30)
    $box.Text = 'C:\Test'
    $Form.Controls.Add($box)

    # �{�^���z�u
    $btn = New-Object System.Windows.Forms.Button
    $btn.Location = New-Object System.Drawing.Point(100,100)
    $btn.Size = New-Object System.Drawing.Size(200,30)
    $btn.Text = '�C���X�g�[��'
    $btn.Add_Click({
        $install_dir = $box.Text

        # �m�F���b�Z�[�W���o��
        $result = [System.Windows.Forms.MessageBox]::Show("${install_dir} `n `n�ɃC���X�g�[�����܂��B`n��낵���ł����H", "�m�F", "YesNo", "Question","button1")
        if ($result -eq [System.Windows.Forms.DialogResult]::Yes) {
            $form.Close()
        }
    })
    $form.AcceptButton = $btn
    $form.Controls.Add($btn)

    $form.ShowDialog()
}

show_window '�E�B���h�E�^�C�g��'