# Audio_Steg
This software was developed as a hackathon project and bagged the SECOND prize in the hackathon. The hackathon was BUILDING TECH FOR THE ARMY and was judged by SMEs with an Army background.

Our software takes a text input from the user and encrypts it using the AES Encryption Algorithm.
This encrypted text is the steganographed in the sample.wav file, which can be de-steganographed and decrypted only at the receiver's end.
In order to ensure the integrity of the file, a digital signature is added to it.
The receiver has the same software running, which on receiving the audio de-steganographs it obtaints the encrypted message. The encrypted message is then decrypted by the receiver and the original text is diplayed to the receiver.

The sending and reception of the file between users is done using the TCP Protocol. The sender and receiver hosts are connected wirelessly via this TCP Protocol and inter change the client-server roles in order to send and receive files.

The front-end was built using HTML, CSS and Flask. Here are the screenshots of the front-end:
<img width="960" alt="image" src="https://user-images.githubusercontent.com/92619272/207442428-33dba81a-b76d-421b-940a-e467a7016bf3.png">

<img width="247" alt="image" src="https://user-images.githubusercontent.com/92619272/207442219-bb1ff54d-0dca-4d62-9b41-917eda214a6a.png">

<img width="844" alt="image" src="https://user-images.githubusercontent.com/92619272/207442524-ea863020-4742-4a7b-b7fb-e840eaf77397.png">

