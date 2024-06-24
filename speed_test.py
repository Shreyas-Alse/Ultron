import speedtest
from brain import respond

st= speedtest.Speedtest()

def test_speed():
    respond('Tell that you are running an internet speed test in very short')
    download= str(st.download())
    upload = str(st.upload())
    result = 'Download speed: ' + download + 'Upload speed:' + upload
    content= 'Tell me about my internet speed' + result
    respond(content)
