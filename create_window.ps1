# ウィンドウを表示
function show_window($title) {
    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing

    # ウィンドウ設定
    $form = New-Object System.Windows.Forms.Form
    $form.Text = $title
    $form.Size = New-Object System.Drawing.Size(420,200)

    # ラベル配置
    $lbl = New-Object System.Windows.Forms.Label
    $lbl.Location = New-Object System.Drawing.Point(20,33)
    $lbl.Text = 'インストール先フォルダ：'
    $lbl.AutoSize = $True
    $form.Controls.Add($lbl)

    # テキストボックス配置
    $box = New-Object System.Windows.Forms.TextBox
    $box.Location = New-Object System.Drawing.Point(150,30)
    $box.Size = New-Object System.Drawing.Size(240,30)
    $box.Text = 'C:\Test'
    $Form.Controls.Add($box)

    # ボタン配置
    $btn = New-Object System.Windows.Forms.Button
    $btn.Location = New-Object System.Drawing.Point(100,100)
    $btn.Size = New-Object System.Drawing.Size(200,30)
    $btn.Text = 'インストール'
    $btn.Add_Click({
        $install_dir = $box.Text

        # 確認メッセージを出す
        $result = [System.Windows.Forms.MessageBox]::Show("${install_dir} `n `nにインストールします。`nよろしいですか？", "確認", "YesNo", "Question","button1")
        if ($result -eq [System.Windows.Forms.DialogResult]::Yes) {
            $form.Close()
        }
    })
    $form.AcceptButton = $btn
    $form.Controls.Add($btn)

    $form.ShowDialog()
}

show_window 'ウィンドウタイトル'