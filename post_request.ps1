#---------------------------------
# HTTPのPOSTリクエスト送信
#---------------------------------
function post() {
	$param = @{
		Uri             = 'https://httpbin.org/post'
		SessionVariable = 'Session'
		Method          = 'POST'
		Body            = @{
			User     = 'jdoe'
			Password = 'P@S$w0rd!'
		}
	}

	Invoke-WebRequest @param
}

#---------------------------------
# HTTPのGETリクエスト送信
#---------------------------------
function get() {
	$param = @{
		Uri             = 'https://httpbin.org/get'
		SessionVariable = 'Session'
		Method          = 'GET'
	}

	Invoke-WebRequest @param
}

post
get