from flask_restful import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask import request
from db import db
from socketio_instance import socketio

songs =[
    {
        "title": "hey jude",
        "artist": "the beatles",
        "picture": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FHey_Jude_%2528Beatles_album%2529&psig=AOvVaw0IY2v_JY1hB97p1h53bxfE&ust=1731162081085000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLDc1Lr3zIkDFQAAAAAdAAAAABAE",
        "lyrics": [
            [
                { "lyrics": "Hey" },
                { "lyrics": "Jude", "chords": "F" },
                { "lyrics": "don't" },
                { "lyrics": "make" },
                { "lyrics": "it" },
                { "lyrics": "bad", "chords": "C" }
            ],
            [
                { "lyrics": "Take" },
                { "lyrics": "a" },
                { "lyrics": "sad", "chords": "C7" },
                { "lyrics": "song", "chords": "C4/7" },
                { "lyrics": "and" },
                { "lyrics": "make" },
                { "lyrics": "it" },
                { "lyrics": "better", "chords": "F" }
            ],
            [
                { "lyrics": "Remember", "chords": "Bb" },
                { "lyrics": "to" },
                { "lyrics": "let" },
                { "lyrics": "her" },
                { "lyrics": "into" },
                { "lyrics": "your" },
                { "lyrics": "heart", "chords": "F" }
            ],
            [
                { "lyrics": "Then" },
                { "lyrics": "you" },
                { "lyrics": "can" },
                { "lyrics": "start", "chords": "C" },
                { "lyrics": "to" },
                { "lyrics": "make", "chords": "C7" },
                { "lyrics": "it" },
                { "lyrics": "better", "chords": "F" }
            ]
        ]
    },
    {
        "title": "ואיך שלא",  
        "artist": "אריאל זילבר",
        "picture":'https://www.google.com/url?sa=i&url=https%3A%2F%2Fhe.wikipedia.org%2Fwiki%2F%25D7%2590%25D7%25A8%25D7%2599%25D7%2590%25D7%259C_%25D7%2596%25D7%2599%25D7%259C%25D7%2591%25D7%25A8&psig=AOvVaw2ZVXovCSdyZl_y9NNsPpqd&ust=1731162295381000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCPDwqqD4zIkDFQAAAAAdAAAAABAE',
        "lyrics": [
            [
                { "lyrics": "ואיך" },
                { "lyrics": "שלא", "chords": "Em" },
                { "lyrics": "אפנה" },
                { "lyrics": "לראות", "chords": "Em/D" }
            ],
            [
                { "lyrics": "תמיד" },
                { "lyrics": "איתה", "chords": "Cmaj7" },
                { "lyrics": "ארצה" },
                { "lyrics": "להיות", "chords": "G" }
            ],
            [
                { "lyrics": "שומרת" },
                { "lyrics": "לי", "chords": "Em" },
                { "lyrics": "היא" },
                { "lyrics": "אמונים", "chords": "Em/D" }
            ],
            [
                { "lyrics": "לא" },
                { "lyrics": "מתרוצצת", "chords": "Cmaj7" },
                { "lyrics": "בגנים", "chords": "G" }
            ],
            [
                { "lyrics": "ובלילות", "chords": "E" },
                { "lyrics": "ובלילות", "chords": "Em/D" }
            ],
            [
                { "lyrics": "עולות" },
                { "lyrics": "עולות", "chords": "Cmaj7" },
                { "lyrics": "בי" },
                { "lyrics": "מנגינות", "chords": "G" }
            ],
            [
                { "lyrics": "וזרם" },
                { "lyrics": "דק", "chords": "E" },
                { "lyrics": "קולח", "chords": "Em/D" }
            ],
            [
                { "lyrics": "ותפילותי", "chords": "Cmaj7" },
                { "lyrics": "לרוח" },
                { "lyrics": "נענות", "chords": "G" }
            ]
        ]
    }
]
# class AllSongs(Resource):
class GetSongs(Resource):
    @jwt_required()
    def get(self):

        return songs, 200
    

@socketio.on('user_connected')
def handle_connect(data):

    socketio.emit('server_response', data)
    

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")
    



    # @jwt_required()
    # def get(self):
    #     print({"hey_jude":hey_jude,"veech_shelo":veech_shelo})
    #     return {"hey_jude":hey_jude,"veech_shelo":veech_shelo},200