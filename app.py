from flask import Flask,redirect,url_for,render_template,request
import wave

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/send')
def next():
    return render_template('page3.html')

@app.route('/done')
def done():
    def encode():
        audio = wave.open("sample.wav",mode="rb")
        frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
        string = str(request.form["enctxt"])
        string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
        bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
        for i, bit in enumerate(bits):
            frame_bytes[i] = (frame_bytes[i] & 254) | bit
        frame_modified = bytes(frame_bytes)
        for i in range(0,10):
            print(frame_bytes[i])
        newAudio =  wave.open('sampleStego.wav', 'wb')
        newAudio.setparams(audio.getparams())
        newAudio.writeframes(frame_modified)

        newAudio.close()
        audio.close()
        #print(" |---->succesfully encoded inside sampleStego.wav")
    
        import socket

        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        #print("Waiting for any incoming connections ... ")
        conn, addr = s.accept()
        #print(addr, "Has connected to the server")
        filename = input(str("Please enter the filename of the file : "))
        file = open(filename , 'rb')
        file_data = file.read(10000000024)
        conn.send(file_data)
        #print("Data has been transmitted successfully")
    encode()

    
    return render_template('page4.html')

@app.route('/doned')
def doned():
    def decode():
        import socket
        s = socket.socket()
        host = request.form("enctxt")
        port = 8080
        s.connect((host,port))
        print("Connected ... ")
        filename = input(str("Please enter a filename for the incoming file : "))
        file = open(filename, 'wb')
        file_data = s.recv(10000000024)
        file.write(file_data)
        file.close()
        #print("File has been received successfully.")
        #print("\nDecoding Starts..")
        audio = wave.open("sampl.wav", mode='rb')
        frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
        decoded = string.split("###")[0]
        #print("Sucessfully decoded: "+decoded)
        audio.close()

    return render_template('page5.html')


if __name__=='__main__':
    app.run(debug=True)