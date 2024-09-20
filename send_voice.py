import requests

def send_voice(file):
    # AmiVoiceのAPIキーを設定(マイページで確認できます)
    APP_KEY = "2D37CA6298044B8ABA356500804316062808AC94306A0503E76E3DFADA73B5BC5104B76AA4684F"

    # 認識対象の音声ファイルパス
    # AUDIO_FILE = "output.wav"

    # エンドポイントのURL
    URL = "https://acp-api.amivoice.com/v1/recognize"

    # 音声ファイルを開く
    with open(file, "rb") as f:
        audio_data = f.read()

    # リクエストのパラメータを設定
    params = {
        "d": "-a-general"
    }
    files = {
        "u": (None, APP_KEY),
        "a": (file, audio_data)
    }

    # POSTリクエストを送信
    response = requests.post(URL, params=params, files=files)

    # レスポンスを処理
    if response.status_code == 200:
        result = response.json()
        # print("認識結果:", result["text"])
    else:
        print("エラー:", response.status_code, response.text)
    
    return result["text"]